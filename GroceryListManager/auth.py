# =============================================================================
# FILE: auth.py
# PURPOSE:
#   This file handles all authentication-related logic:
#   - Validating usernames (format rules)
#   - Hashing passwords securely (never storing plain text passwords)
#   - Registering new users
#   - Logging in existing users
#   - Live username availability checking for the registration form
#
# HOW IT CONNECTS TO OTHER FILES:
#   - main.py imports and calls functions from this file for login/register.
#   - This file imports database.py to check/create users in the database.
#
# STANDARD LIBRARY MODULES USED:
#   - hashlib  : Python's built-in module for cryptographic hashing.
#   - secrets  : Python's built-in module for generating secure random values.
#   - re       : Python's built-in module for regular expressions (pattern matching).
#   - database : Our own database.py file (imported as a module).
# =============================================================================

import hashlib   # for hashing passwords (making them unreadable)
import secrets   # for generating a secure random salt
import re        # for checking username format using patterns
import database  # our database.py file - used to check/create users


# =============================================================================
# FUNCTION: validate_username()
#
# PURPOSE:
#   Checks whether a username string follows all the required rules.
#   This is called both when the user types (live validation) and when
#   they click Register (final validation).
#
# USERNAME RULES:
#   1. Cannot be empty.
#   2. Must be at least 4 characters long.
#   3. Cannot be more than 20 characters long.
#   4. Must start with an English letter (a-z or A-Z).
#   5. Can only contain letters, digits (0-9), and underscores (_).
#   6. No spaces or special characters allowed.
#
# PARAMETERS:
#   username : The username string to validate. Type hint ': str' means
#              this parameter should be a string.
#
# HOW THE REGEX WORKS:
#   re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*", username)
#   - r"..."        : Raw string (backslashes are not escape characters here).
#   - [A-Za-z]      : First character must be a letter (a-z or A-Z).
#   - [A-Za-z0-9_]* : Remaining characters (0 or more) can be letters, digits, or _.
#   - fullmatch     : The ENTIRE string must match, not just part of it.
#   Examples that pass:  arjun123, Siddhi_K, user2026
#   Examples that fail:  123arjun (starts with digit), arjun k (has space)
#
# RETURNS:
#   A tuple (bool, str):
#   (True,  "Username is valid.")       - if username passes all rules.
#   (False, "Error message here.")      - if username fails any rule.
#
# CALLED FROM:
#   register_user() in this file (auth.py) - before creating an account.
#   check_username_live() in this file     - for real-time registration feedback.
# =============================================================================
def validate_username(username: str):
    username = username.strip()   # remove leading/trailing spaces

    # Rule 1: Username cannot be empty
    if not username:
        return False, "Username is required."

    # Rule 2: Minimum 4 characters
    if len(username) < 4:
        return False, "Username must contain at least 4 characters."

    # Rule 3: Maximum 20 characters
    if len(username) > 20:
        return False, "Username cannot exceed 20 characters."

    # Rule 4 & 5: Must start with a letter, only letters/digits/underscore allowed.
    # re.fullmatch checks the ENTIRE string against the pattern.
    if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*", username):
        return False, (
            "Start with a letter. Use only letters, numbers, and underscores."
        )

    # All rules passed
    return True, "Username is valid."


# =============================================================================
# CONSTANT: MIN_PASSWORD_LENGTH
#
# PURPOSE:
#   Defines the minimum number of characters required for a password.
#   Using a constant (instead of writing 6 everywhere) means we only
#   need to change this one line if we want to update the minimum length.
#
# USED IN:
#   register_user() in this file.
# =============================================================================
MIN_PASSWORD_LENGTH = 6


# =============================================================================
# FUNCTION: _generate_salt()
#
# PURPOSE:
#   Creates a random 32-character string called a "salt".
#   A salt is mixed into the password before hashing to make it unique.
#
# WHY IS A SALT NEEDED?
#   Without a salt, two users with the same password would have the same hash.
#   An attacker could use a "rainbow table" (a list of pre-computed hashes)
#   to find the original password. Adding a unique salt for each user makes
#   every hash completely different, even for the same password.
#
# HOW IT WORKS:
#   secrets.token_hex(16) generates 16 random bytes and converts them to
#   a 32-character hexadecimal (0-9, a-f) string.
#   Example output: "a3f8b2c1d4e5f6a7b8c9d0e1f2a3b4c5"
#
# PARAMETERS:
#   None.
#
# RETURNS:
#   A 32-character random hexadecimal string.
#
# CALLED FROM:
#   register_user() in this file - one new salt is generated per registration.
#
# NOTE:
#   The underscore (_) prefix means this is a private/internal function.
#   It is meant to be used only within this file.
# =============================================================================
def _generate_salt() -> str:
    return secrets.token_hex(16)   # 16 bytes = 32 hex characters


# =============================================================================
# FUNCTION: _hash_password()
#
# PURPOSE:
#   Converts a plain-text password into a secure hash using PBKDF2-HMAC-SHA256.
#   This is the main password hashing function used for all NEW accounts.
#
# WHAT IS HASHING?
#   Hashing is a one-way process. You can convert "mypassword" into a hash,
#   but you CANNOT convert the hash back to "mypassword".
#   This means even if someone steals the database, they cannot see passwords.
#
# WHAT IS PBKDF2-HMAC-SHA256?
#   - PBKDF2 = Password-Based Key Derivation Function 2
#   - HMAC   = Hash-based Message Authentication Code
#   - SHA256 = Secure Hash Algorithm with 256-bit output
#   - 260,000 iterations = the hashing is repeated 260,000 times.
#     This makes brute-force attacks (guessing millions of passwords) very slow.
#   - This algorithm is recommended by NIST (National Institute of Standards
#     and Technology) for secure password storage.
#
# PARAMETERS:
#   password : The plain-text password string entered by the user.
#   salt     : The unique random salt generated by _generate_salt().
#
# RETURNS:
#   A long hexadecimal string (the hash). This is what gets stored in the database.
#   Example: "e3b0c44298fc1c149afbf4c8996fb92427ae41e4..."
#
# CALLED FROM:
#   register_user() in this file - to hash the password before saving.
#   login_user() in this file    - to hash the entered password for comparison.
#
# NOTE:
#   The underscore (_) prefix means this is a private/internal function.
# =============================================================================
def _hash_password(password: str, salt: str) -> str:
    # hashlib.pbkdf2_hmac() is Python's built-in PBKDF2 implementation.
    # "sha256" = the hashing algorithm to use.
    # password.encode("utf-8") = convert the password string to bytes.
    # salt.encode("utf-8") = convert the salt string to bytes.
    # iterations=260_000 = repeat the hash 260,000 times for security.
    dk = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt.encode("utf-8"),
        iterations=260_000,
    )
    return dk.hex()   # convert bytes to a readable hex string


# =============================================================================
# FUNCTION: _hash_password_legacy()
#
# PURPOSE:
#   Hashes a password using the OLD SHA-256 method (used before the upgrade).
#   This exists only to support users who registered BEFORE we upgraded to PBKDF2.
#   When a user registered before the migration logs in, their password is
#   verified using this older method because their hash was stored with SHA-256.
#
# HOW THE OLD METHOD WORKED:
#   Combined salt + password into one string, then applied SHA-256 once.
#   This is less secure than PBKDF2 (only 1 iteration instead of 260,000).
#
# PARAMETERS:
#   password : The plain-text password string.
#   salt     : The salt stored in the database for this legacy user.
#
# RETURNS:
#   A SHA-256 hex digest string.
#
# CALLED FROM:
#   login_user() in this file - only when user["hash_algo"] == "sha256".
#
# NOTE:
#   New users will NEVER use this function. Only pre-migration accounts.
# =============================================================================
def _hash_password_legacy(password: str, salt: str) -> str:
    combined = (salt + password).encode("utf-8")   # combine salt + password as bytes
    return hashlib.sha256(combined).hexdigest()    # one SHA-256 hash, returned as hex


# =============================================================================
# ── AUTH OPERATIONS ───────────────────────────────────────────────────────────
# =============================================================================


# =============================================================================
# FUNCTION: register_user()
#
# PURPOSE:
#   The main registration function. Validates all inputs, hashes the password,
#   and creates a new user account in the database.
#   This is the function called when the user clicks "Register".
#
# PARAMETERS:
#   username         : The username string from the registration form.
#   password         : The password string from the registration form.
#   confirm_password : The confirm password string from the registration form.
#
# WHAT IT DOES STEP BY STEP:
#   1. Strip whitespace from all inputs.
#   2. Call validate_username() to check username format rules.
#   3. Check if password is empty.
#   4. Check if password is at least MIN_PASSWORD_LENGTH (6) characters.
#   5. Check if password and confirm_password match.
#   6. Call database.username_exists() to check for duplicate usernames.
#   7. Generate a random salt using _generate_salt().
#   8. Hash the password using _hash_password() with the new salt.
#   9. Call database.create_user() to save the new account.
#   10. Return success message.
#
# RETURNS:
#   A tuple (bool, str):
#   (True,  "Account created! Welcome, username.") - on success.
#   (False, "Error message.")                       - if any validation fails.
#
# CALLED FROM:
#   RegisterScreen._do_register() in main.py - when Register button is clicked.
#
# CALLS:
#   validate_username() in this file.
#   database.username_exists() in database.py.
#   _generate_salt() in this file.
#   _hash_password() in this file.
#   database.create_user() in database.py.
# =============================================================================
def register_user(username: str, password: str, confirm_password: str):
    # Step 1: Remove leading/trailing whitespace from all inputs
    username         = username.strip()
    password         = password.strip()
    confirm_password = confirm_password.strip()

    # Step 2: Validate username format (length, characters, etc.)
    ok, msg = validate_username(username)   # returns (True/False, message)
    if not ok:
        return False, msg   # fail immediately with the validation error

    # Step 3: Password cannot be empty
    if not password:
        return False, "Password is required."

    # Step 4: Password must be at least 6 characters
    if len(password) < MIN_PASSWORD_LENGTH:
        return False, f"Password must be at least {MIN_PASSWORD_LENGTH} characters."

    # Step 5: Password and confirm password must match exactly
    if password != confirm_password:
        return False, "Passwords do not match."

    # Step 6: Check if username is already taken (case-insensitive check in database)
    if database.username_exists(username):   # calls database.py
        return False, f"Username '{username}' is already taken."

    # Step 7: Generate a unique random salt for this user
    salt = _generate_salt()

    # Step 8: Hash the password with the salt using PBKDF2
    hashed = _hash_password(password, salt)

    # Step 9: Save the new user to the database
    # We pass the hash and salt, NEVER the plain password
    success = database.create_user(username, hashed, salt)   # calls database.py
    if not success:
        # This is a fallback - the database UNIQUE INDEX caught a duplicate
        # that we missed in step 6 (shouldn't normally happen).
        return False, f"Username '{username}' is already taken."

    # Step 10: All successful!
    return True, f"Account created! Welcome, {username}."


# =============================================================================
# FUNCTION: login_user()
#
# PURPOSE:
#   Verifies a user's credentials (username + password) against the database.
#   If correct, returns the user's data so the dashboard can load.
#   Supports both legacy SHA-256 accounts and new PBKDF2 accounts.
#
# PARAMETERS:
#   username : The username string from the login form.
#   password : The password string from the login form.
#
# HOW LOGIN WORKS (IMPORTANT CONCEPT):
#   We NEVER store plain passwords. Instead, we:
#   1. Find the user in the database using their username.
#   2. Get their stored salt and hash.
#   3. Hash the ENTERED password using the same salt and algorithm.
#   4. Compare the two hashes. If they match, the password is correct.
#   This is called "hash comparison" and is the standard secure way to verify passwords.
#
# WHY WE SHOW "Invalid username or password" FOR BOTH ERRORS:
#   If we showed "Username not found" vs "Wrong password", attackers could
#   figure out which usernames exist. Showing one generic message for both
#   cases is a security best practice called "security through obscurity".
#
# PARAMETERS:
#   username : Username string entered in the login form.
#   password : Password string entered in the login form.
#
# RETURNS:
#   (True,  user_dict) - if credentials are correct. user_dict has all user data.
#   (False, "Error message") - if login fails for any reason.
#
# CALLED FROM:
#   LoginScreen._do_login() in main.py - when Login button is clicked.
#
# CALLS:
#   database.get_user_by_username() in database.py - to find the user.
#   _hash_password() in this file      - for PBKDF2 accounts.
#   _hash_password_legacy() in this file - for old SHA-256 accounts.
# =============================================================================
def login_user(username: str, password: str):
    # Remove leading/trailing whitespace
    username = username.strip()
    password = password.strip()

    # Both fields must be filled in
    if not username or not password:
        return False, "Please enter both username and password."

    # Look up the user in the database (case-insensitive username search)
    user = database.get_user_by_username(username)   # calls database.py
    if user is None:
        # User not found - use generic message (don't reveal which field is wrong)
        return False, "Invalid username or password."

    # Check which hashing algorithm was used for this account.
    # Legacy accounts (created before the migration) used plain SHA-256.
    # New accounts use PBKDF2-HMAC-SHA256.
    algo = user.get("hash_algo", "sha256")   # default to sha256 if column missing

    if algo == "pbkdf2":
        # Hash the entered password the PBKDF2 way using the stored salt
        expected_hash = _hash_password(password, user["password_salt"])
    else:
        # Hash the entered password the old SHA-256 way
        expected_hash = _hash_password_legacy(password, user["password_salt"])

    # Compare the hash of the entered password with the stored hash.
    # If they are equal, the entered password is correct.
    if expected_hash != user["password_hash"]:
        return False, "Invalid username or password."   # wrong password

    # Login successful - return the full user dictionary
    return True, user


# =============================================================================
# FUNCTION: check_username_live()
#
# PURPOSE:
#   Provides instant feedback as the user types their username on the
#   registration form. Called automatically every time a character is
#   typed in the username field (via trace_add in main.py).
#
# PARAMETERS:
#   username : The username string as currently typed by the user.
#
# RETURNS:
#   A tuple (status, message):
#   ("empty", "")                         - username is empty (no hint shown yet)
#   ("error", "Validation error message") - username fails format rules
#   ("taken", "Username is already taken.") - username exists in database
#   ("ok",    "Username is available")    - username is valid and available
#
# CALLED FROM:
#   RegisterScreen._on_username_change() in main.py.
#   This method is triggered automatically by:
#   self.user_var.trace_add("write", self._on_username_change)
#   meaning it runs every time the user types a character in the username field.
#
# CALLS:
#   validate_username() in this file - to check format rules.
#   database.username_exists() in database.py - to check availability.
# =============================================================================
def check_username_live(username: str):
    username = username.strip()

    # If the field is empty, show nothing (user hasn't started typing yet)
    if not username:
        return "empty", ""

    # Check format rules first (length, characters, etc.)
    ok, msg = validate_username(username)   # calls validate_username()
    if not ok:
        return "error", msg   # show the format error in red

    # If format is valid, check if the username already exists in the database
    if database.username_exists(username):   # calls database.py
        return "taken", "Username is already taken."

    # Username is valid format AND available in the database
    return "ok", "Username is available"
