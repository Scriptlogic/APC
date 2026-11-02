# PROJECT CODE GUIDE
## Grocery List Manager — Complete Developer Reference

---

## 1. Project Overview

The Grocery List Manager is a desktop application built with **Python** and **Tkinter**.
It allows multiple users to manage their own personal grocery lists with full CRUD operations,
search, filtering, dark/light theme, and CSV export.

**Tech stack (standard library only — no pip installs needed):**

| Layer | Technology |
|---|---|
| GUI | `tkinter`, `tkinter.ttk` |
| Database | `sqlite3` |
| Password security | `hashlib`, `secrets` |
| Username validation | `re` (regular expressions) |
| CSV export | `csv` |
| File paths | `os` |
| Timestamps | `datetime` |

---

## 2. Project File Descriptions

| File | Role |
|---|---|
| `main.py` | Entry point. All Tkinter GUI: LoginScreen, RegisterScreen, Dashboard, App. |
| `auth.py` | Authentication: username validation, password hashing, register, login, live check. |
| `database.py` | All SQLite operations: connection, table creation, user CRUD, grocery CRUD, stats, CSV. |
| `_migrate.py` | One-time migration script. Upgrades old DB schema to support PBKDF2 passwords. |
| `_test_logic.py` | Headless test suite for database.py and auth.py. |
| `grocery_manager.db` | SQLite database file. Created automatically on first run. |
| `README.md` | Setup and usage guide for end users. |
| `PROJECT_CODE_GUIDE.md` | This file — developer reference and viva preparation. |

---

## 3. How the Three Main Files Communicate

```
main.py
   |
   |-- imports --> auth.py
   |                  |
   |                  |-- imports --> database.py
   |
   |-- imports --> database.py
```

- `main.py` calls `auth.login_user()` and `auth.register_user()` for authentication.
- `main.py` calls `database.*` directly for all grocery operations.
- `auth.py` calls `database.get_user_by_username()`, `database.username_exists()`, and `database.create_user()`.
- `database.py` imports nothing from the project — it only uses standard library modules.

---

## 4. Application Execution Flow

```
python main.py
      |
      v
if __name__ == "__main__": App()
      |
      v
App.__init__()
      |
      +-- database.initialise_database()   [database.py]
      |     Creates users and grocery_items tables if they don't exist.
      |
      +-- tk.Tk()                          [tkinter]
      |     Creates the main OS window (1150x720 px).
      |
      +-- self._show_login()
      |     Creates LoginScreen, which packs into the root window.
      |
      v
LoginScreen._build()
      Draws the login card: logo, title, username field, password field, buttons.

      User types username and password, clicks Login or presses Enter
      |
      v
LoginScreen._do_login()
      |
      +-- auth.login_user(username, password)     [auth.py]
      |     Looks up user in DB, hashes entered password, compares hashes.
      |     Returns (True, user_dict) or (False, "error message").
      |
      If login fails:  show red error message, stay on login screen.
      If login succeeds:
      |
      +-- self.destroy()     Remove login screen.
      +-- self.on_login_success(user_dict)  -->  App._show_dashboard(user_dict)
      |
      v
App._show_dashboard(user_row)
      Creates Dashboard(root, user_row, on_logout=_show_login)
      |
      v
Dashboard.__init__()
      |
      +-- self.theme = user_row["theme_preference"]   Loads saved theme.
      +-- self._build()
            |
            +-- _apply_ttk_style()     Style ttk widgets for current theme.
            +-- _build_header()        Top nav bar.
            +-- _build_stats()         Four summary cards.
            +-- _build_footer()        Bottom bar (packed FIRST to reserve space).
            +-- _build_main_area()
            |     +-- _build_form_panel()    Left: Add/Edit form.
            |     +-- _build_table_panel()   Right: table with filters.
            +-- refresh_table()        Load grocery items from DB into table.
            +-- refresh_stats()        Load totals from DB into stat cards.

      User performs operations...
      |
      +-- Clicks "Add"       --> _add_item()       --> database.add_grocery_item()
      +-- Clicks "Update"    --> _update_item()    --> database.update_grocery_item()
      +-- Clicks "Delete"    --> _delete_item()    --> database.delete_grocery_item()
      +-- Clicks "Purchased" --> _mark_purchased() --> database.mark_purchased(True)
      +-- Clicks "Pending"   --> _mark_pending()   --> database.mark_purchased(False)
      +-- Types in Search    --> refresh_table()   --> database.get_grocery_items()
      +-- Clicks Dark Mode   --> _toggle_theme()   --> database.update_theme_preference()
      +-- Clicks "Export CSV"--> _export_csv()     --> database.export_items_to_csv()
      |
      +-- Clicks "Logout"
            |
            v
      Dashboard._logout()
            +-- self.destroy()
            +-- self.on_logout()  -->  App._show_login()  -->  LoginScreen appears again
```

---

## 5. Complete Function and Class Reference

### database.py

| Function | Purpose | Called From | Calls |
|---|---|---|---|
| `get_connection()` | Opens and returns a SQLite connection | Every DB function | `sqlite3.connect()` |
| `_row_to_dict(row)` | Converts sqlite3.Row to plain dict | `get_user_by_username`, `get_grocery_items`, `get_item_by_id` | `dict()` |
| `initialise_database()` | Creates tables and indexes on first run | `App.__init__()` | `get_connection()` |
| `create_user(...)` | Inserts a new user row | `auth.register_user()` | `get_connection()` |
| `get_user_by_username(username)` | Finds a user by username (case-insensitive) | `auth.login_user()` | `get_connection()`, `_row_to_dict()` |
| `username_exists(username)` | Checks if a username is taken | `auth.register_user()`, `auth.check_username_live()` | `get_connection()` |
| `update_theme_preference(user_id, theme)` | Saves dark/light preference | `Dashboard._toggle_theme()` | `get_connection()` |
| `add_grocery_item(...)` | Inserts a new grocery item | `Dashboard._add_item()` | `get_connection()`, `datetime.now()` |
| `get_grocery_items(user_id, ...)` | Returns filtered item list | `Dashboard.refresh_table()`, `export_items_to_csv()` | `get_connection()`, `_row_to_dict()` |
| `get_item_by_id(item_id, user_id)` | Returns one item by ID | `Dashboard._on_row_select()` | `get_connection()`, `_row_to_dict()` |
| `update_grocery_item(...)` | Updates an existing item | `Dashboard._update_item()` | `get_connection()` |
| `delete_grocery_item(item_id, user_id)` | Deletes an item | `Dashboard._delete_item()` | `get_connection()` |
| `mark_purchased(item_id, user_id, purchased)` | Sets purchased flag | `Dashboard._mark_purchased()`, `Dashboard._mark_pending()` | `get_connection()` |
| `get_dashboard_stats(user_id)` | Returns (total, bought, pend, cost) | `Dashboard.refresh_stats()` | `get_connection()` |
| `export_items_to_csv(user_id, filepath)` | Writes CSV file | `Dashboard._export_csv()` | `get_grocery_items()`, `csv.writer()` |

---

### auth.py

| Function | Purpose | Called From | Calls |
|---|---|---|---|
| `validate_username(username)` | Checks username format rules | `register_user()`, `check_username_live()` | `re.fullmatch()` |
| `_generate_salt()` | Creates a random 32-char hex salt | `register_user()` | `secrets.token_hex()` |
| `_hash_password(password, salt)` | PBKDF2-SHA256 hash (new accounts) | `register_user()`, `login_user()` | `hashlib.pbkdf2_hmac()` |
| `_hash_password_legacy(password, salt)` | SHA-256 hash (old accounts) | `login_user()` | `hashlib.sha256()` |
| `register_user(username, password, confirm)` | Validates and creates account | `RegisterScreen._do_register()` | `validate_username()`, `database.username_exists()`, `_generate_salt()`, `_hash_password()`, `database.create_user()` |
| `login_user(username, password)` | Verifies credentials | `LoginScreen._do_login()` | `database.get_user_by_username()`, `_hash_password()` or `_hash_password_legacy()` |
| `check_username_live(username)` | Real-time availability check | `RegisterScreen._on_username_change()` | `validate_username()`, `database.username_exists()` |

---

### main.py — Classes and Methods

#### Helper functions (module level)

| Function | Purpose |
|---|---|
| `flat_btn(...)` | Creates a styled flat tk.Button |
| `styled_entry(...)` | Creates a full-width bordered Entry field |
| `pw_field(...)` | Creates a password Entry with Show/Hide button |
| `divider(parent, c)` | Creates a 1px horizontal divider line |

#### LoginScreen (inherits tk.Frame)

| Method | Purpose | Called By |
|---|---|---|
| `__init__(master, on_login_success)` | Constructor, builds UI | `App._show_login()` |
| `_build()` | Creates all login card widgets | `__init__()` |
| `_do_login()` | Verifies credentials and transitions to Dashboard | Login button, Enter key |
| `_open_register()` | Hides login, shows RegisterScreen | Create Account button |
| `_restore()` | Brings back the login screen | `RegisterScreen._go_back()` callback |
| `_clear()` | Resets all form fields | Clear Fields button, `_restore()` |

#### RegisterScreen (inherits tk.Frame)

| Method | Purpose | Called By |
|---|---|---|
| `__init__(master, on_back)` | Constructor, builds UI | `LoginScreen._open_register()` |
| `_build()` | Creates all registration form widgets | `__init__()` |
| `_on_username_change(*_)` | Live username validation on every keystroke | `trace_add` on `user_var` |
| `_on_pw_change(*_)` | Shows password strength hint | `trace_add` on `pw_var` |
| `_do_register()` | Submits the registration form | Register button, Enter key |
| `_go_back()` | Destroys this screen, returns to login | Back to Login button, `after()` |

#### Dashboard (inherits tk.Frame)

| Method | Purpose | Called By |
|---|---|---|
| `__init__(master, user_row, on_logout)` | Constructor | `App._show_dashboard()` |
| `_build()` | Master builder, calls all section builders | `__init__()`, `_rebuild_dashboard()` |
| `_apply_ttk_style()` | Styles ttk widgets for current theme | `_build()` |
| `_build_header()` | Creates top nav bar | `_build()` |
| `_build_stats()` | Creates stat card row | `_build()` |
| `_populate_stat_cards()` | Creates the four coloured cards | `_build_stats()` |
| `_build_footer()` | Creates bottom footer bar | `_build()` |
| `_build_main_area()` | Creates two-column layout | `_build()` |
| `_build_form_panel(parent)` | Creates scrollable Add/Edit form | `_build_main_area()` |
| `_build_table_panel(parent)` | Creates filter bar + Treeview | `_build_main_area()` |
| `refresh_table()` | Reloads grocery items into Treeview | Many places after CRUD operations |
| `refresh_stats()` | Updates stat card numbers | `_build()`, `_refresh_all()` |
| `_refresh_all()` | Calls both refresh_table and refresh_stats | Refresh button, CRUD methods |
| `_on_row_select(_)` | Fills form when table row is clicked | `<<TreeviewSelect>>` event |
| `_validate_form()` | Validates form inputs before save | `_add_item()`, `_update_item()` |
| `_show_msg(text, error)` | Shows feedback message below buttons | All CRUD methods |
| `_add_item()` | Adds new grocery item to DB | Add button |
| `_update_item()` | Updates selected item in DB | Update button |
| `_delete_item()` | Deletes selected item from DB | Delete button |
| `_mark_purchased()` | Sets item purchased=True | Purchased button |
| `_mark_pending()` | Sets item purchased=False | Pending button |
| `_clear_form()` | Resets all form fields | Clear button, `_add_item()`, `_delete_item()` |
| `_export_csv()` | Exports all items to a CSV file | Export to CSV button |
| `_toggle_theme()` | Switches light/dark theme | Theme toggle button |
| `_rebuild_dashboard()` | Destroys and rebuilds all widgets with new theme | `_toggle_theme()` |
| `_logout()` | Confirms and returns to login screen | Logout button |

#### App

| Method | Purpose | Called By |
|---|---|---|
| `__init__()` | Creates window, initialises DB, shows login | `if __name__ == "__main__"` |
| `_show_login()` | Creates LoginScreen | `__init__()`, `Dashboard._logout()` |
| `_show_dashboard(user_row)` | Creates Dashboard | `LoginScreen._do_login()` via callback |

---

## 6. Important SQL Queries

### Table Creation

```sql
-- Users table (initialise_database)
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password_hash TEXT NOT NULL,
    password_salt TEXT NOT NULL,
    hash_algo TEXT NOT NULL DEFAULT 'pbkdf2',
    theme_preference TEXT NOT NULL DEFAULT 'light'
)

-- Case-insensitive unique index (prevents Siddhi and siddhi as separate accounts)
CREATE UNIQUE INDEX IF NOT EXISTS uix_users_username_lower ON users (LOWER(username))

-- Grocery items table
CREATE TABLE IF NOT EXISTS grocery_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    ...
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
)
```

### User Operations

```sql
-- Login lookup (case-insensitive)
SELECT * FROM users WHERE LOWER(username) = LOWER(?)

-- Check if username is taken (registration)
SELECT id FROM users WHERE LOWER(username) = LOWER(?)

-- Save theme preference
UPDATE users SET theme_preference = ? WHERE id = ?

-- Insert new user
INSERT INTO users (username, password_hash, password_salt, hash_algo) VALUES (?, ?, ?, ?)
```

### Grocery Operations

```sql
-- Get items (base query — filters added dynamically)
SELECT * FROM grocery_items WHERE user_id = ?
  AND LOWER(name) LIKE ?        -- if search text provided
  AND category = ?              -- if category filter selected
  AND purchased = 1             -- if "Purchased" status selected
ORDER BY created_at DESC

-- Insert new item
INSERT INTO grocery_items (user_id, name, quantity, unit, price_per_unit,
  category, purchased, created_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?)

-- Update item
UPDATE grocery_items
  SET name=?, quantity=?, unit=?, price_per_unit=?, category=?, purchased=?
  WHERE id=? AND user_id=?

-- Delete item
DELETE FROM grocery_items WHERE id = ? AND user_id = ?

-- Toggle purchased flag
UPDATE grocery_items SET purchased = ? WHERE id = ? AND user_id = ?

-- Dashboard statistics
SELECT COUNT(*) FROM grocery_items WHERE user_id = ?
SELECT COUNT(*) FROM grocery_items WHERE user_id = ? AND purchased = 1
SELECT SUM(quantity * price_per_unit) FROM grocery_items WHERE user_id = ?
```

---

## 7. Key Flows

### Login Flow
```
LoginScreen._do_login()
  --> auth.login_user(username, password)
        --> database.get_user_by_username(username)   [find user by name]
        --> _hash_password(entered_password, stored_salt)  [hash what was typed]
        --> compare hashes: if equal -> login OK
  --> if OK: self.destroy() + App._show_dashboard(user_dict)
  --> if fail: show red error message
```

### Registration Flow
```
RegisterScreen._do_register()
  --> auth.register_user(username, password, confirm)
        --> validate_username(username)            [check format rules]
        --> database.username_exists(username)     [check if taken]
        --> _generate_salt()                       [random 32-char string]
        --> _hash_password(password, salt)         [PBKDF2 hash]
        --> database.create_user(username, hash, salt)  [INSERT into DB]
  --> if OK: show success + after(1500, _go_back)
  --> if fail: show red error message
```

### Add Grocery Item Flow
```
Dashboard._add_item()
  --> _validate_form()                        [check name, qty > 0, price >= 0]
  --> database.add_grocery_item(user_id, ...) [INSERT into grocery_items]
  --> _show_msg("'name' added.")
  --> _clear_form()
  --> _refresh_all()
        --> refresh_table()  --> database.get_grocery_items(user_id)
        --> refresh_stats()  --> database.get_dashboard_stats(user_id)
```

### Update Grocery Item Flow
```
1. User clicks table row  --> _on_row_select()
      --> database.get_item_by_id(item_id, user_id)
      --> populates form fields + stores self.selected_id

2. User edits fields, clicks Update  --> _update_item()
      --> _validate_form()
      --> database.update_grocery_item(selected_id, user_id, ...)
      --> _show_msg + _refresh_all()
```

### Delete Grocery Item Flow
```
Dashboard._delete_item()
  --> messagebox.askyesno("Confirm Delete?")   [user must confirm]
  --> if Yes: database.delete_grocery_item(selected_id, user_id)
  --> _show_msg + _clear_form + _refresh_all()
```

### Expense Calculation Flow
```
-- In database.get_dashboard_stats():
   SELECT SUM(quantity * price_per_unit) FROM grocery_items WHERE user_id = ?
   Example: Rice 5 x 60 = 300, Milk 2 x 60 = 120 -> SUM = 420

-- In Dashboard.refresh_table() (per-row cost display):
   est = round(row["quantity"] * row["price_per_unit"], 2)
   displayed as "Rs420.00" in the Est. Cost column

-- In Dashboard.refresh_stats():
   database.get_dashboard_stats() returns estimated_cost
   self.stat_cost.config(text=f"Rs{cost:,.2f}")
```

### CSV Export Flow
```
Dashboard._export_csv()
  --> filedialog.asksaveasfilename()        [shows save dialog to user]
  --> database.export_items_to_csv(user_id, filepath)
        --> get_grocery_items(user_id)      [fetch all items]
        --> csv.writer(file)               [open file for writing]
        --> writer.writerow(headers)       [write column names]
        --> for each item: calculate cost, writer.writerow([...])
  --> messagebox.showinfo("Export Successful")
```

### Theme Switch Flow
```
Dashboard._toggle_theme()
  --> self.theme = "dark" if "light" else "light"
  --> self.c = THEMES[self.theme]
  --> database.update_theme_preference(user_id, theme)   [save to DB]
  --> _rebuild_dashboard()
        --> snap = save current form values and selected row ID
        --> destroy all child widgets
        --> _build()   [recreate everything with new colours]
        --> restore form values from snap
        --> refresh_table() + refresh_stats()
        --> re-select previously selected row in table
```

---

## 8. Important Variables

| Variable | Where | What It Stores |
|---|---|---|
| `DB_PATH` | `database.py` module level | Full file path to grocery_manager.db |
| `THEMES` | `main.py` module level | Dict of two colour palettes ("light", "dark") |
| `UNITS` | `main.py` module level | List of measurement unit strings |
| `CATEGORIES` | `main.py` module level | List of grocery category strings |
| `MIN_PASSWORD_LENGTH` | `auth.py` module level | Minimum password length (6) |
| `self.user_id` | `Dashboard` instance | Integer ID of logged-in user — used in EVERY DB call |
| `self.theme` | `Dashboard` instance | Current theme string: "light" or "dark" |
| `self.c` | `Dashboard` instance | Active colour dict = `THEMES[self.theme]` |
| `self.selected_id` | `Dashboard` instance | DB ID of selected table row (None if nothing selected) |
| `self.tree` | `Dashboard` instance | The ttk.Treeview table widget |
| `self.v_name` | `Dashboard` instance | StringVar linked to Item Name entry |
| `self.v_qty` | `Dashboard` instance | StringVar linked to Quantity entry |
| `self.v_unit` | `Dashboard` instance | StringVar linked to Unit dropdown |
| `self.v_price` | `Dashboard` instance | StringVar linked to Price entry |
| `self.v_cat` | `Dashboard` instance | StringVar linked to Category dropdown |
| `self.v_bought` | `Dashboard` instance | BooleanVar linked to Purchased checkbox |
| `self.search_var` | `Dashboard` instance | StringVar for search box |
| `self.filter_cat` | `Dashboard` instance | StringVar for category filter dropdown |
| `self.filter_status` | `Dashboard` instance | StringVar for status filter dropdown |
| `self.msg_var` | `Dashboard` instance | StringVar for feedback message label |

---

## 9. Database Design

### users table

| Column | Type | Description |
|---|---|---|
| `id` | INTEGER PRIMARY KEY | Auto-incrementing unique ID |
| `username` | TEXT NOT NULL | Username as typed (original case preserved) |
| `password_hash` | TEXT NOT NULL | Hashed password (PBKDF2 or SHA-256) — NEVER plain text |
| `password_salt` | TEXT NOT NULL | Random 32-char string mixed into password before hashing |
| `hash_algo` | TEXT DEFAULT 'pbkdf2' | Which algorithm: 'pbkdf2' (new) or 'sha256' (legacy) |
| `theme_preference` | TEXT DEFAULT 'light' | Saved theme: 'light' or 'dark' |

**Unique index:** `uix_users_username_lower` on `LOWER(username)` — enforces case-insensitive uniqueness.

### grocery_items table

| Column | Type | Description |
|---|---|---|
| `id` | INTEGER PRIMARY KEY | Auto-incrementing unique ID |
| `user_id` | INTEGER NOT NULL | Foreign key → users.id (links item to its owner) |
| `name` | TEXT NOT NULL | Item name (e.g. "Rice") |
| `quantity` | REAL NOT NULL | Amount (e.g. 5.0) |
| `unit` | TEXT NOT NULL | Unit string (e.g. "Kilogram (kg)") |
| `price_per_unit` | REAL NOT NULL | Price in rupees (e.g. 60.0) |
| `category` | TEXT NOT NULL | Category string (e.g. "Grains") |
| `purchased` | INTEGER DEFAULT 0 | 0 = Pending, 1 = Purchased |
| `created_at` | TEXT NOT NULL | Timestamp: "2026-10-26 14:30:00" |

**Foreign key:** `user_id REFERENCES users(id) ON DELETE CASCADE`
Means: if a user is deleted, all their grocery items are automatically deleted too.

---

## 10. Security Notes

### Password Hashing
- Passwords are **never** stored as plain text.
- New accounts: `hashlib.pbkdf2_hmac("sha256", password, salt, iterations=260_000)`
- 260,000 iterations makes brute-force attacks very slow (NIST 2023 recommendation).
- Each user gets a unique random salt from `secrets.token_hex(16)`.
- Even if two users have the same password, their hashes are completely different.

### SQL Injection Prevention
- All SQL uses parameterized queries with `?` placeholders.
- Example: `conn.execute("SELECT * FROM users WHERE id = ?", (user_id,))`
- User input is **never** directly concatenated into SQL strings.

### User Isolation
- Every grocery query includes `WHERE user_id = ?` with the logged-in user's ID.
- This makes it impossible for User A to see, edit, or delete User B's items.

---

## 11. VIVA Questions and Answers

---

**Q1. Where does the application start? What is the entry point?**

At the bottom of `main.py`:
```python
if __name__ == "__main__":
    App()
```
Python runs this block when `python main.py` is executed. It creates an `App` object which calls `App.__init__()`.

---

**Q2. Where is the database connection established?**

In `database.py`, inside the function `get_connection()`:
```python
conn = sqlite3.connect(DB_PATH, timeout=10)
```
Every database function calls `get_connection()` to open a fresh connection, then closes it after the operation.

---

**Q3. Where are the database tables created?**

In `database.py`, inside `initialise_database()`. This function is called once from `App.__init__()` before the window opens. It uses `CREATE TABLE IF NOT EXISTS` so it is safe to call every time.

---

**Q4. Where is `initialise_database()` called?**

In `App.__init__()` in `main.py`:
```python
database.initialise_database()
```
This is the very first thing `App.__init__()` does, before creating the window.

---

**Q5. Where is `login_user()` defined and where is it called?**

**Defined:** `auth.py`, function `login_user(username, password)`.
**Called from:** `LoginScreen._do_login()` in `main.py`:
```python
ok_flag, result = auth.login_user(self.user_var.get(), self.pw_var.get())
```

---

**Q6. How does `login_user()` work?**

1. Strips whitespace from username and password.
2. Calls `database.get_user_by_username(username)` to find the user.
3. Reads the `hash_algo` field to know which hashing method was used.
4. Hashes the **entered** password using the **stored salt**.
5. Compares the result with the stored hash.
6. If hashes match → returns `(True, user_dict)`.
7. If no match or user not found → returns `(False, "Invalid username or password.")`.

---

**Q7. Where is `register_user()` defined and called?**

**Defined:** `auth.py`, function `register_user(username, password, confirm_password)`.
**Called from:** `RegisterScreen._do_register()` in `main.py`.

---

**Q8. How does `register_user()` work step by step?**

1. Strip whitespace from all inputs.
2. Call `validate_username()` — checks length, format, and character rules.
3. Check password is not empty and is at least 6 characters.
4. Check password and confirm password match.
5. Call `database.username_exists()` — reject if username is already taken.
6. Call `_generate_salt()` — create a random 32-character salt.
7. Call `_hash_password(password, salt)` — PBKDF2 hash.
8. Call `database.create_user(username, hash, salt)` — INSERT into DB.
9. Return `(True, "Account created!")`.

---

**Q9. Where is password hashing implemented?**

In `auth.py`:
- `_hash_password(password, salt)` — uses `hashlib.pbkdf2_hmac` with 260,000 iterations. Used for new accounts.
- `_hash_password_legacy(password, salt)` — uses `hashlib.sha256`. Used for accounts created before the migration.

---

**Q10. What is a salt and why is it used?**

A salt is a random string added to a password before hashing. It is generated by `_generate_salt()` using `secrets.token_hex(16)`.

Without a salt, two users with the same password would produce the same hash, allowing "rainbow table" attacks. With a unique salt per user, every hash is different even for identical passwords.

---

**Q11. How does the application know which user is logged in?**

`LoginScreen._do_login()` calls `auth.login_user()` which returns the user's full database row as a dictionary. This is passed to `App._show_dashboard(user_row)`, which passes it to `Dashboard.__init__(master, user_row, on_logout)`. The Dashboard stores `self.user_id = user_row["id"]` and uses it in every database call.

---

**Q12. Where is a grocery item inserted into the database?**

In `database.py`, function `add_grocery_item()`:
```sql
INSERT INTO grocery_items (user_id, name, quantity, unit, price_per_unit, category, purchased, created_at)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
```
This is called from `Dashboard._add_item()` in `main.py` when the Add button is clicked.

---

**Q13. Where is the UPDATE SQL query for grocery items?**

In `database.py`, function `update_grocery_item()`:
```sql
UPDATE grocery_items
SET name=?, quantity=?, unit=?, price_per_unit=?, category=?, purchased=?
WHERE id=? AND user_id=?
```
Called from `Dashboard._update_item()` in `main.py`.

---

**Q14. Where is the DELETE SQL query?**

In `database.py`, function `delete_grocery_item()`:
```sql
DELETE FROM grocery_items WHERE id = ? AND user_id = ?
```
Called from `Dashboard._delete_item()` in `main.py` after the user confirms the dialog.

---

**Q15. How is the total estimated cost calculated?**

In two places:

**Per-item cost** — in `Dashboard.refresh_table()` in `main.py`:
```python
est = round(r["quantity"] * r["price_per_unit"], 2)
```

**Dashboard total** — in `database.get_dashboard_stats()` using SQL:
```sql
SELECT SUM(quantity * price_per_unit) FROM grocery_items WHERE user_id = ?
```
This is shown on the Est. Cost stat card.

---

**Q16. How does the search functionality work?**

1. The search box is linked to `self.search_var` (a `StringVar`).
2. `trace_add("write", ...)` calls `refresh_table()` on every keystroke.
3. `refresh_table()` calls `database.get_grocery_items(user_id, search=search_var.get())`.
4. In `database.get_grocery_items()`, if search text is provided:
   ```sql
   AND LOWER(name) LIKE ?    -- with value "%rice%"
   ```
5. LIKE with `%` wildcards matches any name containing the search text.

---

**Q17. How is the purchased status updated?**

In `database.py`, function `mark_purchased(item_id, user_id, purchased: bool)`:
```sql
UPDATE grocery_items SET purchased = ? WHERE id = ? AND user_id = ?
```
`int(purchased)` converts `True` → 1 and `False` → 0.

Called from:
- `Dashboard._mark_purchased()` with `purchased=True`
- `Dashboard._mark_pending()` with `purchased=False`

---

**Q18. How does CSV export work?**

1. User clicks "Export to CSV" → `Dashboard._export_csv()`.
2. `filedialog.asksaveasfilename()` shows a save dialog.
3. `database.export_items_to_csv(user_id, filepath)` is called.
4. Inside that function: `get_grocery_items(user_id)` fetches all items.
5. Python's `csv.writer` opens the file and writes the header row and data rows.
6. Each row includes the calculated `estimated = quantity * price_per_unit`.

---

**Q19. How does theme switching work?**

1. User clicks the theme button → `Dashboard._toggle_theme()`.
2. `self.theme` is flipped: "light" ↔ "dark".
3. `self.c = THEMES[self.theme]` — updates the active colour palette.
4. `database.update_theme_preference(user_id, theme)` — saves to DB.
5. `_rebuild_dashboard()` is called:
   - Saves current form values and selected row ID in `snap` dict.
   - Destroys all child widgets.
   - Calls `_build()` which recreates everything with new colours.
   - Restores saved values from `snap`.

---

**Q20. How is the user's theme preference remembered between sessions?**

- Saved: `database.update_theme_preference(user_id, theme)` — UPDATE query.
- Loaded: `auth.login_user()` returns the full user dict including `theme_preference`.
- Applied: `Dashboard.__init__()` reads `user_row["theme_preference"]` and sets `self.theme`.

---

**Q21. What is a Foreign Key and where is it used?**

A Foreign Key links rows in one table to rows in another table.
In this project:
```sql
FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
```
This means `grocery_items.user_id` must match an existing `users.id`.
`ON DELETE CASCADE` means if a user is deleted, all their grocery items are automatically deleted too.

---

**Q22. What is a Primary Key and which columns are Primary Keys?**

A Primary Key uniquely identifies each row in a table. It cannot be NULL or duplicate.
- `users.id` is the Primary Key for the users table.
- `grocery_items.id` is the Primary Key for the grocery_items table.
Both use `INTEGER PRIMARY KEY AUTOINCREMENT`, meaning SQLite assigns the next available number automatically.

---

**Q23. What is `AUTOINCREMENT` in SQL?**

`AUTOINCREMENT` means SQLite automatically assigns a unique increasing number to the `id` column when a new row is inserted. We never need to specify an ID value ourselves.

---

**Q24. What does `row_factory = sqlite3.Row` do?**

By default, SQLite returns rows as plain tuples, accessed by position: `row[0]`, `row[1]`.
Setting `conn.row_factory = sqlite3.Row` makes rows behave like dictionaries, so we can access columns by name: `row["username"]`, `row["id"]`. This makes the code much more readable.

---

**Q25. Why do we use `_row_to_dict(row)` before closing the connection?**

`sqlite3.Row` objects keep an internal reference to the database connection. If we close the connection and then try to use the Row object, it can fail or return corrupt data.

Converting the Row to a plain Python dictionary with `dict(row)` before `conn.close()` ensures the data is safe to use after the connection is closed.

---

**Q26. What is `PRAGMA foreign_keys = ON`?**

SQLite does not enforce foreign key constraints by default. This PRAGMA command enables them for the current connection. Without it, you could insert a grocery item with a `user_id` that doesn't exist in the users table.

---

**Q27. What is `PRAGMA journal_mode = WAL`?**

WAL stands for Write-Ahead Logging. It changes how SQLite writes changes to disk. WAL mode allows multiple reads to happen at the same time as a write, which prevents "database is locked" errors that were occurring when multiple connections were opened quickly in succession.

---

**Q28. What is a lambda function and where is it used?**

A lambda function is a small anonymous (unnamed) function defined in one line.
Used in `main.py` to bind keyboard and event handlers:
```python
self.master.bind("<Return>", lambda e: self._do_login())
```
Here `lambda e: self._do_login()` creates a function that ignores the event argument `e` and just calls `_do_login()`. This is needed because `.bind()` always passes an event object to the callback.

---

**Q29. What is `trace_add("write", callback)` and where is it used?**

`StringVar.trace_add("write", callback)` tells Tkinter to call `callback` automatically whenever the StringVar's value changes (i.e., every time the user types a character).

Used in `RegisterScreen._build()`:
```python
self.user_var.trace_add("write", self._on_username_change)
self.pw_var.trace_add("write", self._on_pw_change)
```
Also in `Dashboard._build_table_panel()`:
```python
self.search_var.trace_add("write", lambda *_: self.refresh_table())
```

---

**Q30. What is `super().__init__(master)` and why is it needed?**

Every class in this project inherits from `tk.Frame`. When we write:
```python
class LoginScreen(tk.Frame):
    def __init__(self, master, on_login_success):
        super().__init__(master)
```
`super().__init__(master)` calls the `__init__` method of the parent class `tk.Frame`. This is required to properly initialise the Frame widget — without it, the Frame would not be created and all subsequent widget operations would fail.

---

**Q31. What is `pack_forget()` and how is it different from `destroy()`?**

- `pack_forget()` — hides the widget from the screen but keeps it in memory. It can be shown again with `.pack()`. Used in `LoginScreen._open_register()` to hide the login screen while showing the registration screen.
- `destroy()` — permanently removes the widget and all its children from memory. Cannot be undone. Used in `LoginScreen._do_login()` to permanently remove the login screen before showing the Dashboard.

---

**Q32. What is `self.master.after(1500, self._go_back)` and what does it do?**

`after(delay_milliseconds, function)` schedules a function to be called after a delay, without blocking the GUI.

Used in `RegisterScreen._do_register()` after successful registration:
```python
self.master.after(1500, self._go_back)
```
This shows the success message for 1.5 seconds, then automatically goes back to the login screen. Without `after()`, we would have to use `time.sleep()` which would freeze the entire GUI.

---

**Q33. Why are buttons created with `tk.Button` instead of `ttk.Button`?**

`ttk.Button` on Windows uses the native Windows styling, which ignores the `bg` (background colour) and `fg` (foreground colour) settings we provide. `tk.Button` with `relief="flat"` gives us full colour control, which is required for the coloured button design in this project.

---

**Q34. What does `iid=str(r["id"])` do in the Treeview, and why is it important?**

When inserting a row into the Treeview:
```python
self.tree.insert("", "end", iid=str(r["id"]), values=(...))
```
`iid` is the unique identifier for that Treeview row. We set it to the string version of the database primary key.

When the user clicks a row, `self.tree.selection()` returns a tuple containing this `iid`. We convert it back with `int(sel[0])` to get the exact database ID of the selected item. This ensures we always update/delete the correct item, even after searching or filtering changes the display order.

---

**Q35. How does the application prevent one user from seeing another user's items?**

Every SQL query for grocery items includes `WHERE user_id = ?` with `self.user_id` (the logged-in user's integer ID). This is enforced in:
- `get_grocery_items(user_id, ...)` — SELECT
- `get_item_by_id(item_id, user_id)` — SELECT with both item ID and user ID
- `update_grocery_item(..., user_id, ...)` — UPDATE WHERE id=? AND user_id=?
- `delete_grocery_item(item_id, user_id)` — DELETE WHERE id=? AND user_id=?
- `mark_purchased(item_id, user_id, ...)` — UPDATE WHERE id=? AND user_id=?

Even if an attacker knew another user's item ID, the `AND user_id=?` clause would prevent any access.

---

*End of PROJECT_CODE_GUIDE.md*
