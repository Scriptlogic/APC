"""
_migrate.py
One-time database migration:
  - Rebuilds the users table to remove the column-level UNIQUE constraint
    on username and replaces it with a UNIQUE INDEX on LOWER(username).
  - Adds a hash_algo column so legacy SHA-256 passwords continue to work
    while new registrations use PBKDF2-HMAC-SHA256.
  - Preserves all users and all grocery_items rows.

Run once: python _migrate.py
"""
import sqlite3
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)
import database

DB_PATH = database.DB_PATH

print(f"Migrating: {DB_PATH}")

conn = sqlite3.connect(DB_PATH, timeout=10)
conn.execute("PRAGMA foreign_keys = OFF")   # disable FK checks during migration
conn.execute("PRAGMA journal_mode = WAL")

cur = conn.cursor()

# Check if migration already done
cur.execute("PRAGMA table_info(users)")
cols = [r[1] for r in cur.fetchall()]
already_migrated = "hash_algo" in cols

if already_migrated:
    print("Migration already applied. Nothing to do.")
    conn.close()
    sys.exit(0)

print("Backing up users data...")
cur.execute("SELECT id, username, password_hash, password_salt, theme_preference FROM users")
users = cur.fetchall()
print(f"  Found {len(users)} user(s).")

cur.execute("SELECT id, user_id, name, quantity, unit, price_per_unit, category, purchased, created_at FROM grocery_items")
items = cur.fetchall()
print(f"  Found {len(items)} grocery item(s).")

print("Dropping old tables...")
cur.execute("DROP TABLE IF EXISTS grocery_items")
cur.execute("DROP TABLE IF EXISTS users")

print("Creating new users table with hash_algo column...")
cur.execute("""
    CREATE TABLE users (
        id               INTEGER PRIMARY KEY AUTOINCREMENT,
        username         TEXT    NOT NULL,
        password_hash    TEXT    NOT NULL,
        password_salt    TEXT    NOT NULL,
        hash_algo        TEXT    NOT NULL DEFAULT 'sha256',
        theme_preference TEXT    NOT NULL DEFAULT 'light'
    )
""")

cur.execute("""
    CREATE UNIQUE INDEX uix_users_username_lower
    ON users (LOWER(username))
""")

print("Re-inserting users (marked as sha256)...")
for row in users:
    uid, username, pw_hash, pw_salt, theme = row
    cur.execute(
        "INSERT INTO users (id, username, password_hash, password_salt, hash_algo, theme_preference) "
        "VALUES (?, ?, ?, ?, 'sha256', ?)",
        (uid, username, pw_hash, pw_salt, theme)
    )

print("Re-creating grocery_items table...")
cur.execute("""
    CREATE TABLE grocery_items (
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

print("Re-inserting grocery items...")
for item in items:
    cur.execute(
        "INSERT INTO grocery_items "
        "(id, user_id, name, quantity, unit, price_per_unit, category, purchased, created_at) "
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
        item
    )

conn.execute("PRAGMA foreign_keys = ON")
conn.commit()
conn.close()

print(f"\nMigration complete.")
print(f"  Users migrated : {len(users)}")
print(f"  Items migrated : {len(items)}")
print("\nNote: Existing accounts use legacy SHA-256 passwords and will continue to work.")
print("New registrations will automatically use PBKDF2-HMAC-SHA256.")
