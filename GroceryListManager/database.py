# =============================================================================
# FILE: database.py
# PURPOSE:
#   This file handles EVERYTHING related to the SQLite database.
#   It creates the database file, creates tables, and provides functions
#   to insert, read, update and delete users and grocery items.
#
# HOW IT CONNECTS TO OTHER FILES:
#   - auth.py imports this file to check usernames and create/find users.
#   - main.py imports this file to read/write grocery items and stats.
#   - _migrate.py imports this file to get the database file path.
#
# STANDARD LIBRARY MODULES USED:
#   - sqlite3  : Python's built-in module to work with SQLite databases.
#   - os       : Used to build the correct file path for the database file.
# =============================================================================

import sqlite3
import os

# =============================================================================
# DB_PATH  (Module-level variable)
#
# PURPOSE:
#   Stores the full file path to the database file "grocery_manager.db".
#   os.path.dirname(__file__) gives us the folder where database.py lives.
#   os.path.abspath makes sure the path is absolute (not relative).
#   os.path.join combines the folder path with the filename.
#
# RESULT:
#   DB_PATH = "E:\3rd year\APC\APC project\GroceryListManager\grocery_manager.db"
#   (or wherever the project folder is on your computer)
#
# USED BY:
#   get_connection(), _migrate.py
# =============================================================================
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "grocery_manager.db")


# =============================================================================
# FUNCTION: get_connection()
#
# PURPOSE:
#   Opens and returns a connection to the SQLite database file.
#   This is the ONLY place where the database connection is created.
#   Every other function calls this to get a connection.
#
# PARAMETERS:
#   None.
#
# WHAT IT DOES STEP BY STEP:
#   1. sqlite3.connect(DB_PATH) - Opens the database file (creates it if missing).
#   2. timeout=10 - If the database is locked, wait up to 10 seconds before failing.
#   3. PRAGMA foreign_keys = ON - Tells SQLite to enforce foreign key rules.
#   4. PRAGMA journal_mode = WAL - Enables Write-Ahead Logging for better
#      performance. Prevents "database is locked" errors when multiple
#      operations happen quickly.
#   5. conn.row_factory = sqlite3.Row - Makes database rows behave like
#      dictionaries, so we can access columns by name (e.g. row["username"])
#      instead of by position (e.g. row[1]).
#
# RETURNS:
#   A sqlite3.Connection object ready to use.
#
# CALLED FROM:
#   Every database function in this file:
#   initialise_database(), create_user(), get_user_by_username(),
#   username_exists(), update_theme_preference(), add_grocery_item(),
#   get_grocery_items(), get_item_by_id(), update_grocery_item(),
#   delete_grocery_item(), mark_purchased(), get_dashboard_stats(),
#   export_items_to_csv()
# =============================================================================
def get_connection():
    conn = sqlite3.connect(DB_PATH, timeout=10)
    conn.execute("PRAGMA foreign_keys = ON")   # enforce foreign key constraints
    conn.execute("PRAGMA journal_mode = WAL")  # prevent database lock errors
    conn.row_factory = sqlite3.Row             # allow column access by name
    return conn


# =============================================================================
# FUNCTION: _row_to_dict()
#
# PURPOSE:
#   Converts a sqlite3.Row object into a plain Python dictionary.
#   The underscore (_) at the start means this is a private/internal helper.
#
# WHY IS THIS NEEDED?
#   When we call conn.close(), sqlite3.Row objects can become invalid
#   because they hold an internal reference to the connection.
#   By converting rows to plain dictionaries BEFORE closing the connection,
#   we can safely use the data even after the connection is closed.
#
# PARAMETERS:
#   row : A sqlite3.Row object returned by a database query.
#         Can also be None (when a query returns no results).
#
# RETURNS:
#   A Python dictionary with column names as keys, or None if row is None.
#   Example: {"id": 1, "username": "Siddhi", "theme_preference": "light"}
#
# CALLED FROM:
#   get_user_by_username(), get_grocery_items(), get_item_by_id()
# =============================================================================
def _row_to_dict(row):
    if row is None:
        return None       # if no result was found, return None
    return dict(row)      # convert Row object to a regular dictionary


# =============================================================================
# FUNCTION: initialise_database()
#
# PURPOSE:
#   Creates the database tables and indexes when the application first runs.
#   If the tables already exist, nothing changes (CREATE TABLE IF NOT EXISTS).
#   This is the SETUP function called once at application startup.
#
# PARAMETERS:
#   None.
#
# WHAT IT CREATES:
#   TABLE: users
#     - id               : Auto-incrementing unique number for each user (Primary Key).
#     - username         : The user's chosen name (stored as typed, e.g. "Siddhi").
#     - password_hash    : The scrambled (hashed) password. NEVER the real password.
#     - password_salt    : A random string mixed into the password before hashing.
#     - hash_algo        : Which hashing algorithm was used ('pbkdf2' or 'sha256').
#     - theme_preference : The user's preferred theme ('light' or 'dark').
#
#   INDEX: uix_users_username_lower
#     - A UNIQUE INDEX on LOWER(username).
#     - This means "Siddhi" and "siddhi" and "SIDDHI" are all considered the same.
#     - Prevents two users from registering with the same name in different cases.
#
#   TABLE: grocery_items
#     - id             : Auto-incrementing unique number for each item (Primary Key).
#     - user_id        : Foreign Key linking this item to the user who created it.
#     - name           : Name of the grocery item (e.g. "Rice").
#     - quantity       : How much (e.g. 5.0).
#     - unit           : Unit of measurement (e.g. "Kilogram (kg)").
#     - price_per_unit : Cost per unit (e.g. 60.0).
#     - category       : Type of item (e.g. "Grains").
#     - purchased      : 0 = Pending, 1 = Purchased.
#     - created_at     : Date and time the item was added.
#
#   FOREIGN KEY:
#     user_id REFERENCES users(id) ON DELETE CASCADE means:
#     If a user is deleted, all their grocery items are automatically deleted too.
#
# RETURNS:
#   Nothing (None).
#
# CALLED FROM:
#   App.__init__() in main.py - runs once when the application starts.
# =============================================================================
def initialise_database():
    conn = get_connection()   # open a connection to the database file
    cursor = conn.cursor()    # cursor is used to execute SQL commands

    # Create the users table.
    # "IF NOT EXISTS" means: only create if it doesn't already exist.
    # This makes the function safe to call multiple times.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id               INTEGER PRIMARY KEY AUTOINCREMENT,
            username         TEXT    NOT NULL,
            password_hash    TEXT    NOT NULL,
            password_salt    TEXT    NOT NULL,
            hash_algo        TEXT    NOT NULL DEFAULT 'pbkdf2',
            theme_preference TEXT    NOT NULL DEFAULT 'light'
        )
    """)

    # Create a unique index on LOWER(username).
    # This enforces case-insensitive uniqueness at the database level.
    # Even if Python misses a duplicate, the database will catch it.
    cursor.execute("""
        CREATE UNIQUE INDEX IF NOT EXISTS uix_users_username_lower
        ON users (LOWER(username))
    """)

    # Create the grocery_items table.
    # user_id is a Foreign Key - it links each item to the user who created it.
    # ON DELETE CASCADE means items are auto-deleted if the user is deleted.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS grocery_items (
            id             INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id        INTEGER NOT NULL,
            name           TEXT    NOT NULL,
            quantity       REAL    NOT NULL,
            unit           TEXT    NOT NULL,
            price_per_unit REAL    NOT NULL,
            category       TEXT    NOT NULL,
            purchased      INTEGER NOT NULL DEFAULT 0,
            created_at     TEXT    NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        )
    """)

    conn.commit()   # save all changes permanently to the database file
    conn.close()    # close the connection to free up resources


# =============================================================================
# ── USER OPERATIONS ──────────────────────────────────────────────────────────
# The functions below handle creating and finding user accounts.
# =============================================================================


# =============================================================================
# FUNCTION: create_user()
#
# PURPOSE:
#   Inserts a new user account into the 'users' table in the database.
#   If the username already exists (even with different capitalisation),
#   the database's UNIQUE INDEX will raise an error and the function returns False.
#
# PARAMETERS:
#   username      : The chosen username string (e.g. "Siddhi").
#   password_hash : The hashed (scrambled) password string from auth.py.
#   password_salt : The random salt string used during hashing from auth.py.
#   hash_algo     : Which algorithm was used. Default is 'pbkdf2' for new users.
#                   Legacy users have 'sha256'.
#
# WHAT IT DOES:
#   1. Opens a database connection.
#   2. Tries to INSERT a new row into the users table.
#   3. If the INSERT succeeds, commits (saves) and returns True.
#   4. If the INSERT fails because the username already exists
#      (IntegrityError from the UNIQUE INDEX), it rolls back and returns False.
#   5. The 'finally' block ALWAYS closes the connection, even if an error occurred.
#      This is important - it prevents "database is locked" errors.
#
# RETURNS:
#   True  - if the user was successfully created.
#   False - if the username is already taken.
#
# CALLED FROM:
#   register_user() in auth.py - after all validations pass.
#
# CALLS:
#   get_connection() to open the database.
#
# EXCEPTION HANDLING:
#   sqlite3.IntegrityError is raised when the UNIQUE INDEX is violated
#   (i.e., a duplicate username). We catch this and return False instead
#   of crashing the application.
# =============================================================================
def create_user(username, password_hash, password_salt, hash_algo="pbkdf2"):
    conn = get_connection()   # open database connection
    try:
        # SQL INSERT statement - inserts one row into the users table.
        # The '?' placeholders prevent SQL injection attacks.
        # We never put variables directly into SQL strings.
        conn.execute(
            "INSERT INTO users (username, password_hash, password_salt, hash_algo) "
            "VALUES (?, ?, ?, ?)",
            (username, password_hash, password_salt, hash_algo)
        )
        conn.commit()    # save the new user to the database permanently
        return True      # successfully created
    except sqlite3.IntegrityError:
        # This error means the username already exists in the database.
        # The UNIQUE INDEX on LOWER(username) caught the duplicate.
        conn.rollback()  # undo any partial changes
        return False     # username is taken
    finally:
        # 'finally' runs no matter what - success or error.
        # This ensures the connection is ALWAYS closed properly.
        conn.close()


# =============================================================================
# FUNCTION: get_user_by_username()
#
# PURPOSE:
#   Searches the database for a user with the given username.
#   The search is case-insensitive: "Siddhi", "siddhi", "SIDDHI" all match.
#   Used during login to find the user's stored password hash.
#
# PARAMETERS:
#   username : The username string typed by the user at login.
#
# WHAT IT DOES:
#   1. Opens a database connection.
#   2. Runs a SELECT query using LOWER() on both sides to ignore case.
#   3. fetchone() gets the first matching row (or None if not found).
#   4. _row_to_dict() converts the Row to a dictionary before closing.
#   5. Closes the connection.
#
# RETURNS:
#   A dictionary of the user's data if found.
#   Example: {"id": 1, "username": "Siddhi", "password_hash": "abc...",
#             "password_salt": "xyz...", "hash_algo": "pbkdf2",
#             "theme_preference": "light"}
#   None - if no user with that username exists.
#
# CALLED FROM:
#   login_user() in auth.py - to find the user and compare password hashes.
#
# CALLS:
#   get_connection(), _row_to_dict()
# =============================================================================
def get_user_by_username(username):
    conn = get_connection()   # open database connection
    # LOWER(username) = LOWER(?) makes the search case-insensitive.
    # So "Siddhi" matches "siddhi" matches "SIDDHI".
    row = conn.execute(
        "SELECT * FROM users WHERE LOWER(username) = LOWER(?)", (username,)
    ).fetchone()   # fetchone() returns one row, or None if not found
    conn.close()
    return _row_to_dict(row)   # convert to dict before connection closes


# =============================================================================
# FUNCTION: username_exists()
#
# PURPOSE:
#   Checks whether a username is already registered in the database.
#   Used during registration for live validation and final duplicate check.
#   Comparison is case-insensitive.
#
# PARAMETERS:
#   username : The username string to check.
#
# RETURNS:
#   True  - if the username already exists in the database.
#   False - if the username is available (not yet taken).
#
# CALLED FROM:
#   register_user() in auth.py - to check before creating a new account.
#   check_username_live() in auth.py - to show real-time availability feedback.
#
# CALLS:
#   get_connection()
# =============================================================================
def username_exists(username):
    conn = get_connection()   # open database connection
    # We only need to know IF a user exists, so we select just the 'id' column.
    # This is faster than selecting all columns with SELECT *.
    row = conn.execute(
        "SELECT id FROM users WHERE LOWER(username) = LOWER(?)", (username,)
    ).fetchone()
    conn.close()
    return row is not None   # True if a row was found, False if not


# =============================================================================
# FUNCTION: update_theme_preference()
#
# PURPOSE:
#   Saves the user's chosen theme ('light' or 'dark') to the database.
#   This is called whenever the user clicks the Dark Mode / Light Mode button.
#   Next time they log in, their saved theme is automatically loaded.
#
# PARAMETERS:
#   user_id : The integer ID of the logged-in user.
#   theme   : A string, either 'light' or 'dark'.
#
# WHAT IT DOES:
#   Runs an SQL UPDATE to change the theme_preference column for the given user.
#
# RETURNS:
#   Nothing (None).
#
# CALLED FROM:
#   Dashboard._toggle_theme() in main.py - when the user clicks the theme button.
#
# CALLS:
#   get_connection()
# =============================================================================
def update_theme_preference(user_id, theme):
    conn = get_connection()   # open database connection
    # UPDATE SQL: changes only the theme_preference column for one specific user.
    # WHERE id = ? ensures only that user's row is updated.
    conn.execute(
        "UPDATE users SET theme_preference = ? WHERE id = ?", (theme, user_id)
    )
    conn.commit()    # save the change permanently
    conn.close()


# =============================================================================
# ── GROCERY ITEM OPERATIONS ───────────────────────────────────────────────────
# The functions below handle adding, reading, updating and deleting grocery items.
# =============================================================================


# =============================================================================
# FUNCTION: add_grocery_item()
#
# PURPOSE:
#   Inserts a new grocery item into the 'grocery_items' table.
#   Every item is linked to the user who created it via user_id.
#   This ensures users can only see their own items.
#
# PARAMETERS:
#   user_id        : ID of the logged-in user (links this item to that user).
#   name           : Name of the grocery item (e.g. "Rice").
#   quantity       : How much of the item (e.g. 5.0).
#   unit           : Unit of measurement (e.g. "Kilogram (kg)").
#   price_per_unit : Cost per unit in rupees (e.g. 60.0).
#   category       : Type of item (e.g. "Grains").
#   purchased      : True = item is purchased, False = item is pending.
#
# WHAT IT DOES:
#   1. Gets the current date and time as a string for created_at.
#   2. Converts 'purchased' (True/False) to 1 or 0 using int().
#      SQLite stores booleans as integers: 1 = True, 0 = False.
#   3. Inserts the new row into grocery_items.
#   4. cursor.lastrowid gives the auto-generated ID of the new row.
#
# RETURNS:
#   The integer ID (primary key) of the newly inserted grocery item row.
#
# CALLED FROM:
#   Dashboard._add_item() in main.py - when the user clicks the Add button.
#
# CALLS:
#   get_connection(), datetime.now() from the datetime module.
# =============================================================================
def add_grocery_item(user_id, name, quantity, unit, price_per_unit, category, purchased):
    from datetime import datetime
    # Get current timestamp like "2026-10-26 14:30:00" for the created_at column
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    conn = get_connection()   # open database connection
    # INSERT SQL: inserts a new row with all the item details.
    # int(purchased) converts True -> 1 and False -> 0 for SQLite storage.
    cursor = conn.execute(
        """INSERT INTO grocery_items
               (user_id, name, quantity, unit, price_per_unit, category, purchased, created_at)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        (user_id, name, quantity, unit, price_per_unit, category, int(purchased), created_at)
    )
    new_id = cursor.lastrowid   # get the auto-generated ID of the new row
    conn.commit()    # save the new item permanently
    conn.close()
    return new_id    # return the new item's ID


# =============================================================================
# FUNCTION: get_grocery_items()
#
# PURPOSE:
#   Retrieves grocery items from the database for a specific user.
#   Can optionally filter by search text, category, and purchased status.
#   This is called every time the table needs to be refreshed.
#
# PARAMETERS:
#   user_id  : ID of the logged-in user. Only their items are returned.
#   search   : Optional text to search for in item names (case-insensitive).
#              Default is "" (empty string = no search filter).
#   category : Optional category to filter by (e.g. "Grains").
#              Default is "All" which means no category filter.
#   status   : Optional status filter. Can be "All", "Purchased", or "Pending".
#              Default is "All" which returns all items.
#
# HOW THE DYNAMIC SQL QUERY WORKS:
#   We start with a base query and add extra conditions based on the filters.
#   This is called "building a query dynamically".
#   Example with all filters:
#     SELECT * FROM grocery_items
#     WHERE user_id = ?
#     AND LOWER(name) LIKE ?      -- for search
#     AND category = ?            -- for category filter
#     AND purchased = 1           -- for "Purchased" status
#     ORDER BY created_at DESC
#
# RETURNS:
#   A list of dictionaries, one dictionary per grocery item.
#   Each dictionary has keys: id, user_id, name, quantity, unit,
#   price_per_unit, category, purchased, created_at.
#   Returns an empty list [] if no items match.
#
# CALLED FROM:
#   Dashboard.refresh_table() in main.py - to populate the table display.
#   export_items_to_csv() in database.py - to get all items for CSV export.
#
# CALLS:
#   get_connection(), _row_to_dict()
# =============================================================================
def get_grocery_items(user_id, search="", category="All", status="All"):
    # Start with the base query - always filter by user_id for security.
    # This ensures User A can NEVER see User B's items.
    query = "SELECT * FROM grocery_items WHERE user_id = ?"
    params = [user_id]   # list of values to replace the ? placeholders

    # If search text is provided, add a LIKE filter for name search.
    # LIKE '%rice%' matches any name containing "rice" (case-insensitive).
    if search:
        query += " AND LOWER(name) LIKE ?"
        params.append(f"%{search.lower()}%")   # % means "any characters here"

    # If a specific category is selected (not "All"), add a category filter.
    if category != "All":
        query += " AND category = ?"
        params.append(category)

    # If status filter is selected, add a purchased filter.
    # purchased=1 means "Purchased", purchased=0 means "Pending".
    if status == "Purchased":
        query += " AND purchased = 1"
    elif status == "Pending":
        query += " AND purchased = 0"

    # ORDER BY created_at DESC means newest items appear at the top.
    query += " ORDER BY created_at DESC"

    conn = get_connection()
    # Execute the query with the params list. fetchall() returns all matching rows.
    rows = [_row_to_dict(r) for r in conn.execute(query, params).fetchall()]
    conn.close()
    return rows   # list of dictionaries, one per grocery item


# =============================================================================
# FUNCTION: get_item_by_id()
#
# PURPOSE:
#   Fetches a single grocery item from the database using its ID.
#   Also checks that the item belongs to the given user (security check).
#   This is used to populate the form when the user clicks a row in the table.
#
# PARAMETERS:
#   item_id : The integer ID (primary key) of the grocery item to fetch.
#   user_id : The ID of the logged-in user. Used to verify ownership.
#
# SECURITY NOTE:
#   The WHERE clause includes "AND user_id = ?" to ensure a user cannot
#   access another user's item even if they somehow know its ID.
#
# RETURNS:
#   A dictionary with the item's data if found and owned by the user.
#   None if the item doesn't exist or belongs to a different user.
#
# CALLED FROM:
#   Dashboard._on_row_select() in main.py - when a table row is clicked.
#
# CALLS:
#   get_connection(), _row_to_dict()
# =============================================================================
def get_item_by_id(item_id, user_id):
    conn = get_connection()
    row = conn.execute(
        # Both item_id AND user_id must match - prevents cross-user access.
        "SELECT * FROM grocery_items WHERE id = ? AND user_id = ?",
        (item_id, user_id)
    ).fetchone()   # fetchone() returns one row or None
    conn.close()
    return _row_to_dict(row)   # convert to dict before closing


# =============================================================================
# FUNCTION: update_grocery_item()
#
# PURPOSE:
#   Updates the details of an existing grocery item in the database.
#   All fields (name, quantity, unit, price, category, purchased) can change.
#   The item's ID stays the same - only its data changes.
#
# PARAMETERS:
#   item_id        : The ID of the item to update.
#   user_id        : The logged-in user's ID (security check).
#   name           : New name for the item.
#   quantity       : New quantity.
#   unit           : New unit of measurement.
#   price_per_unit : New price per unit.
#   category       : New category.
#   purchased      : New purchased status (True or False).
#
# SECURITY NOTE:
#   WHERE id=? AND user_id=? means only the owner can update their own item.
#
# RETURNS:
#   Nothing (None).
#
# CALLED FROM:
#   Dashboard._update_item() in main.py - when user clicks the Update button.
#
# CALLS:
#   get_connection()
# =============================================================================
def update_grocery_item(item_id, user_id, name, quantity, unit,
                        price_per_unit, category, purchased):
    conn = get_connection()
    # UPDATE SQL: changes specific columns for one specific item.
    # SET name=?, quantity=? etc. replaces the old values with new ones.
    # WHERE id=? AND user_id=? ensures only the right item is updated.
    conn.execute(
        """UPDATE grocery_items
           SET name=?, quantity=?, unit=?, price_per_unit=?, category=?, purchased=?
           WHERE id=? AND user_id=?""",
        (name, quantity, unit, price_per_unit, category, int(purchased), item_id, user_id)
    )
    conn.commit()    # save the updated data permanently
    conn.close()


# =============================================================================
# FUNCTION: delete_grocery_item()
#
# PURPOSE:
#   Permanently deletes a grocery item from the database.
#   The user must confirm this action in the UI before this function is called.
#
# PARAMETERS:
#   item_id : The ID of the item to delete.
#   user_id : The logged-in user's ID (security check - only owner can delete).
#
# SECURITY NOTE:
#   WHERE id=? AND user_id=? ensures a user cannot delete another user's item.
#
# RETURNS:
#   Nothing (None).
#
# CALLED FROM:
#   Dashboard._delete_item() in main.py - after the user confirms the delete dialog.
#
# CALLS:
#   get_connection()
# =============================================================================
def delete_grocery_item(item_id, user_id):
    conn = get_connection()
    # DELETE SQL: removes the row from the table permanently.
    # Both item_id and user_id must match for the deletion to happen.
    conn.execute(
        "DELETE FROM grocery_items WHERE id = ? AND user_id = ?",
        (item_id, user_id)
    )
    conn.commit()    # commit the deletion
    conn.close()


# =============================================================================
# FUNCTION: mark_purchased()
#
# PURPOSE:
#   Updates the 'purchased' column of a grocery item to 1 (Purchased)
#   or 0 (Pending). This is a targeted update - only the purchased status
#   changes, nothing else.
#
# PARAMETERS:
#   item_id   : The ID of the grocery item to update.
#   user_id   : The logged-in user's ID (security check).
#   purchased : True  -> sets purchased = 1 (item is bought).
#               False -> sets purchased = 0 (item is pending).
#
# RETURNS:
#   Nothing (None).
#
# CALLED FROM:
#   Dashboard._mark_purchased() in main.py - "Purchased" button.
#   Dashboard._mark_pending() in main.py   - "Pending" button.
#
# CALLS:
#   get_connection()
# =============================================================================
def mark_purchased(item_id, user_id, purchased: bool):
    conn = get_connection()
    # UPDATE SQL: only changes the 'purchased' column.
    # int(purchased) converts True->1 or False->0 for SQLite.
    conn.execute(
        "UPDATE grocery_items SET purchased = ? WHERE id = ? AND user_id = ?",
        (int(purchased), item_id, user_id)
    )
    conn.commit()
    conn.close()


# =============================================================================
# FUNCTION: get_dashboard_stats()
#
# PURPOSE:
#   Calculates and returns the four summary statistics shown on the
#   dashboard cards: total items, purchased count, pending count,
#   and estimated total cost.
#
# PARAMETERS:
#   user_id : The logged-in user's ID. Statistics are only for this user's items.
#
# WHAT IT CALCULATES:
#   total          : COUNT(*) of all grocery items for this user.
#   purchased      : COUNT(*) of items where purchased = 1.
#   pending        : total - purchased (calculated in Python, not SQL).
#   estimated_cost : SUM(quantity * price_per_unit) for all items.
#                    Example: Rice 5kg x Rs60 = Rs300
#                             Milk 2L  x Rs60 = Rs120
#                             Total = Rs420
#
# RETURNS:
#   A tuple of 4 values: (total, purchased, pending, estimated_cost)
#   Example: (3, 1, 2, 420.0)
#
# CALLED FROM:
#   Dashboard.refresh_stats() in main.py - to update the dashboard cards.
#
# CALLS:
#   get_connection()
# =============================================================================
def get_dashboard_stats(user_id):
    conn = get_connection()
    cur = conn.cursor()   # cursor used to run multiple queries

    # COUNT(*) counts all rows for this user
    total = cur.execute(
        "SELECT COUNT(*) FROM grocery_items WHERE user_id = ?", (user_id,)
    ).fetchone()[0]   # [0] gets the first (and only) column value

    # Count only items where purchased = 1
    purchased = cur.execute(
        "SELECT COUNT(*) FROM grocery_items WHERE user_id = ? AND purchased = 1", (user_id,)
    ).fetchone()[0]

    # Pending is simply total minus purchased (no extra SQL needed)
    pending = total - purchased

    # SUM(quantity * price_per_unit) calculates total estimated grocery bill.
    # Returns None if there are no items, so we default to 0.0.
    cost_row = cur.execute(
        "SELECT SUM(quantity * price_per_unit) FROM grocery_items WHERE user_id = ?",
        (user_id,)
    ).fetchone()[0]
    estimated_cost = cost_row if cost_row else 0.0   # handle None when no items exist

    conn.close()
    return total, purchased, pending, estimated_cost   # return as a tuple


# =============================================================================
# FUNCTION: export_items_to_csv()
#
# PURPOSE:
#   Exports all grocery items for a user to a CSV (Comma-Separated Values) file.
#   The user can open this file in Microsoft Excel or Google Sheets.
#
# PARAMETERS:
#   user_id  : The logged-in user's ID. Only their items are exported.
#   filepath : The full file path where the CSV file should be saved.
#              This path comes from the file dialog shown to the user.
#
# WHAT IT DOES:
#   1. Calls get_grocery_items() to fetch all items for the user.
#   2. Opens the file at 'filepath' for writing.
#   3. Writes a header row (column names).
#   4. For each grocery item, calculates estimated cost and writes a data row.
#
# CSV FORMAT EXAMPLE:
#   ID, Name, Quantity, Unit, Price/Unit, Estimated Cost, Category, Purchased, Created At
#   1,  Rice, 5.0,      kg,   60.0,       300.0,          Grains,   No,        2026-10-26 10:00:00
#
# RETURNS:
#   Nothing (None). Writes directly to the file.
#
# CALLED FROM:
#   Dashboard._export_csv() in main.py - when user clicks "Export to CSV".
#
# CALLS:
#   get_grocery_items() to fetch the items.
#   csv.writer() from Python's built-in csv module.
# =============================================================================
def export_items_to_csv(user_id, filepath):
    import csv   # Python's built-in module for reading and writing CSV files

    rows = get_grocery_items(user_id)   # get all items for this user

    # Column headers for the CSV file
    headers = ["ID", "Name", "Quantity", "Unit", "Price/Unit (Rs)",
               "Estimated Cost (Rs)", "Category", "Purchased", "Created At"]

    # Open the file for writing. newline="" prevents extra blank lines on Windows.
    # encoding="utf-8" ensures special characters like Rs symbol work correctly.
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)   # write the header row first

        # Write one row per grocery item
        for row in rows:
            # Calculate estimated cost: quantity x price per unit
            estimated = round(row["quantity"] * row["price_per_unit"], 2)
            writer.writerow([
                row["id"], row["name"], row["quantity"], row["unit"],
                row["price_per_unit"], estimated, row["category"],
                "Yes" if row["purchased"] else "No",   # convert 1/0 to Yes/No
                row["created_at"]
            ])
