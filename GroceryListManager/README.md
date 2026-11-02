# 🛒 Grocery List Manager

A complete desktop Grocery List Manager built with **Python + Tkinter + SQLite**.  
No third-party packages are required — everything runs with a standard Python 3 installation.

---

## Project Files

| File | Purpose |
|------|---------|
| `main.py` | Entry point. Contains the full Tkinter GUI — login screen, registration screen, and the main dashboard with all grocery-management features. |
| `database.py` | All SQLite logic — creates the database tables, and provides functions to create/read/update/delete users and grocery items. |
| `auth.py` | Registration and login helpers. Handles input validation, password hashing (SHA-256 + random salt), and credential verification. |
| `grocery_manager.db` | SQLite database file. Created automatically the first time you run the app. |
| `README.md` | This file. |

---

## Requirements

- **Python 3.8 or later** (download from https://www.python.org)
- No pip installs needed — only standard-library modules are used:
  `tkinter`, `sqlite3`, `hashlib`, `secrets`, `csv`, `os`, `datetime`

---

## How to Run (Windows)

Open **PowerShell** in the `GroceryListManager` folder and run:

```powershell
python main.py
```

Or navigate to the folder first:

```powershell
cd "e:\3rd year\APC\APC project\GroceryListManager"
python main.py
```

---

## How to Register and Log In

1. The **Login** screen appears when you start the app.
2. Click **Create Account** to open the registration form.
3. Enter a username (≥ 3 characters), a password (≥ 6 characters), and confirm the password.
4. Click **Register** — you will be redirected back to the login screen automatically.
5. Enter your credentials and click **Login** (or press **Enter**).

Each user's grocery list is completely private — one user can never see another's items.

---

## Dashboard Features

### Adding an item
1. Fill in **Item Name**, **Quantity**, **Unit**, **Price per Unit**, and **Category**.
2. Optionally tick **Mark as Purchased**.
3. Click **➕ Add**.

### Editing an item
1. Click any row in the table — the form fills automatically.
2. Change any field.
3. Click **✏️ Update**.

### Deleting an item
1. Select a row.
2. Click **🗑 Delete** and confirm the dialog.

### Purchasing / Pending
- Select a row and click **✅ Purchased** or **🔄 Pending**.

### Searching and filtering
- Type in the **Search** box to filter by name in real time.
- Use the **Category** and **Status** dropdowns to narrow results.

### Exporting to CSV
- Click **📥 Export to CSV** and choose a save location.

### Logout
- Click **🚪 Logout** in the top-right corner.

---

## Switching Themes

- Click **🌙 Dark Mode** (or **☀️ Light Mode**) in the header bar.
- The interface switches immediately, preserving all form data and the selected row.
- Your preference is saved to the database and restored the next time you log in.

---

## Database Location

The database file is created at:

```
GroceryListManager\grocery_manager.db
```

It stores all user accounts and grocery items.  
Delete this file to reset the app completely.

---

## Sample Calculation

| Item  | Qty | Unit | Price/Unit | Est. Cost |
|-------|-----|------|-----------|-----------|
| Rice  | 5   | kg   | ₹60       | ₹300      |
| Milk  | 2   | L    | ₹60       | ₹120      |
| **Total** | | | | **₹420** |

---

## Testing Checklist

- [ ] App starts and shows the login screen
- [ ] New user can register; duplicate username is rejected
- [ ] Wrong password is rejected with a friendly message
- [ ] Registered user can log in and log out
- [ ] Each user sees only their own grocery items
- [ ] Add, Update, Delete, Search, Filter all work correctly
- [ ] Purchased / Pending toggle works
- [ ] Dashboard stats refresh after changes
- [ ] Dark ↔ Light mode switches immediately without losing data
- [ ] Theme is remembered after logout and re-login
- [ ] Data persists after closing and reopening the app
- [ ] CSV export produces a correct file
- [ ] Invalid input (empty name, text in quantity) shows an error — no crash
