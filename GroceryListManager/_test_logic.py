# coding: utf-8
"""
_test_logic.py  -  Headless test suite for database.py and auth.py.
Run:  python _test_logic.py
"""
import os
import sys
import tempfile

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

import database as db
import auth

# ── helpers ───────────────────────────────────────────────────────────────────

def ok(msg):
    print("[PASS]", msg)

def fail(msg):
    raise AssertionError("[FAIL] " + msg)

# ── setup: wipe test accounts ─────────────────────────────────────────────────

db.initialise_database()

def _cleanup():
    c = db.get_connection()
    c.execute("DELETE FROM users WHERE LOWER(username) IN ('testuser','other_user','testuser99')")
    c.commit()
    c.close()

_cleanup()
ok("DB initialised and test data cleaned")

# ── username validation ────────────────────────────────────────────────────────

cases_valid = ["arjun123", "Arjun_K", "user2026", "TestUser"]
cases_invalid = [
    ("abc",           "too short"),
    ("123arjun",      "starts with digit"),
    ("arjun k",       "contains space"),
    ("arjun@123",     "contains @"),
    ("a" * 21,        "too long"),
    ("",              "empty"),
]

for uname in cases_valid:
    v, msg = auth.validate_username(uname)
    assert v, f"Expected valid for '{uname}', got: {msg}"
ok("validate_username: valid examples pass")

for uname, reason in cases_invalid:
    v, msg = auth.validate_username(uname)
    assert not v, f"Expected invalid ({reason}) for '{uname}'"
ok("validate_username: invalid examples rejected")

# ── registration ──────────────────────────────────────────────────────────────

r_ok, r_msg = auth.register_user("testuser", "pass123", "pass123")
assert r_ok, "Expected register success: " + r_msg
ok("Register new user: " + r_msg)

r2_ok, r2_msg = auth.register_user("testuser", "pass123", "pass123")
assert not r2_ok, "Expected duplicate rejection"
ok("Duplicate username rejected: " + r2_msg)

# Case-insensitive duplicate
r3_ok, r3_msg = auth.register_user("TESTUSER", "pass123", "pass123")
assert not r3_ok, "Expected case-insensitive duplicate rejection"
ok("Case-insensitive duplicate rejected: " + r3_msg)

r4_ok, r4_msg = auth.register_user("alice", "abc", "abc")
assert not r4_ok, "Expected short-password rejection"
ok("Short password rejected: " + r4_msg)

r5_ok, r5_msg = auth.register_user("", "pass123", "pass123")
assert not r5_ok, "Expected empty-username rejection"
ok("Empty username rejected: " + r5_msg)

r6_ok, r6_msg = auth.register_user("user1", "pass123", "different")
assert not r6_ok, "Expected mismatched-password rejection"
ok("Mismatched passwords rejected: " + r6_msg)

# ── login ──────────────────────────────────────────────────────────────────────

l_ok, user = auth.login_user("testuser", "pass123")
assert l_ok, "Expected login success: " + str(user)
assert isinstance(user, dict), "user must be a dict"
ok("Login success, user=" + user["username"])

# Case-insensitive login
l2_ok, user2 = auth.login_user("TESTUSER", "pass123")
assert l2_ok, "Expected case-insensitive login success"
assert user2["id"] == user["id"], "Must return same user record"
ok("Case-insensitive login OK")

l3_ok, l3_msg = auth.login_user("testuser", "wrongpw")
assert not l3_ok
ok("Wrong password rejected: " + l3_msg)

l4_ok, l4_msg = auth.login_user("nobody", "pass123")
assert not l4_ok
ok("Unknown user rejected: " + l4_msg)

l5_ok, l5_msg = auth.login_user("", "")
assert not l5_ok
ok("Empty login rejected: " + l5_msg)

# ── grocery items ──────────────────────────────────────────────────────────────

uid = user["id"]

id1 = db.add_grocery_item(uid, "Rice",  5, "Kilogram (kg)", 60, "Grains",     False)
id2 = db.add_grocery_item(uid, "Milk",  2, "Liter",         60, "Dairy",      False)
id3 = db.add_grocery_item(uid, "Onion", 1, "Kilogram (kg)", 30, "Vegetables", False)
ok("Added 3 items: ids %d %d %d" % (id1, id2, id3))

# ── stats ─────────────────────────────────────────────────────────────────────

total, bought, pend, cost = db.get_dashboard_stats(uid)
assert total == 3,            "total=" + str(total)
assert bought == 0,           "bought=" + str(bought)
assert pend   == 3,           "pend=" + str(pend)
assert abs(cost - 450.0) < 0.01, "cost=" + str(cost)
ok("Stats: total=%d bought=%d pend=%d cost=%.2f" % (total, bought, pend, cost))

# ── purchased toggle ──────────────────────────────────────────────────────────

db.mark_purchased(id1, uid, True)
_, b2, p2, _ = db.get_dashboard_stats(uid)
assert b2 == 1 and p2 == 2
ok("mark_purchased OK")

db.mark_purchased(id1, uid, False)
_, b3, p3, _ = db.get_dashboard_stats(uid)
assert b3 == 0 and p3 == 3
ok("mark_pending OK")

# ── search & filter ───────────────────────────────────────────────────────────

rows = db.get_grocery_items(uid, search="rice")
assert len(rows) == 1 and rows[0]["name"] == "Rice"
ok("Search 'rice' -> " + rows[0]["name"])

rows2 = db.get_grocery_items(uid, category="Dairy")
assert len(rows2) == 1 and rows2[0]["name"] == "Milk"
ok("Category filter 'Dairy' -> " + rows2[0]["name"])

db.mark_purchased(id2, uid, True)
rows3 = db.get_grocery_items(uid, status="Purchased")
assert len(rows3) == 1 and rows3[0]["name"] == "Milk"
rows4 = db.get_grocery_items(uid, status="Pending")
assert len(rows4) == 2
ok("Status filter OK: 1 purchased, 2 pending")

# ── update ────────────────────────────────────────────────────────────────────

db.update_grocery_item(id2, uid, "Full Cream Milk", 3, "Liter", 70, "Dairy", True)
row = db.get_item_by_id(id2, uid)
assert row["name"] == "Full Cream Milk"
assert row["quantity"] == 3
assert row["price_per_unit"] == 70
ok("Update -> " + row["name"])

# ── delete ────────────────────────────────────────────────────────────────────

db.delete_grocery_item(id3, uid)
rows5 = db.get_grocery_items(uid)
assert len(rows5) == 2, "expected 2 remaining, got " + str(len(rows5))
ok("Delete -> %d remaining" % len(rows5))

# ── cost calculation ──────────────────────────────────────────────────────────

# Rice 5x60=300, Full Cream Milk 3x70=210 -> 510
_, _, _, final_cost = db.get_dashboard_stats(uid)
assert abs(final_cost - 510.0) < 0.01, "cost=" + str(final_cost)
ok("Cost calc -> Rs %.2f" % final_cost)

# ── theme preference ──────────────────────────────────────────────────────────

db.update_theme_preference(uid, "dark")
u_check = db.get_user_by_username("testuser")
assert u_check["theme_preference"] == "dark"
ok("Theme saved: " + u_check["theme_preference"])

# ── CSV export ────────────────────────────────────────────────────────────────

fpath = os.path.join(tempfile.gettempdir(), "_grocery_test_export.csv")
db.export_items_to_csv(uid, fpath)
with open(fpath, encoding="utf-8") as f:
    lines = f.read().strip().splitlines()
assert len(lines) == 3, "expected 3 CSV lines, got " + str(len(lines))
ok("CSV export: %d lines (header + 2 items)" % len(lines))
os.remove(fpath)

# ── cross-user isolation ──────────────────────────────────────────────────────

auth.register_user("other_user", "other123", "other123")
other = db.get_user_by_username("other_user")
assert other is not None
other_rows = db.get_grocery_items(other["id"])
assert len(other_rows) == 0, "other user must have 0 items, got " + str(len(other_rows))
ok("Cross-user isolation: other_user sees 0 items")

cross = db.get_item_by_id(id1, other["id"])
assert cross is None, "Cross-user item access must be blocked"
ok("get_item_by_id cross-user blocked")

# ── check_username_live ───────────────────────────────────────────────────────

status, msg = auth.check_username_live("testuser")
assert status == "taken", "expected taken, got " + status
ok("check_username_live: taken -> " + msg)

status2, msg2 = auth.check_username_live("brandnewuser99")
assert status2 == "ok", "expected ok, got " + status2
ok("check_username_live: available -> " + msg2)

status3, msg3 = auth.check_username_live("ab")
assert status3 == "error", "expected error, got " + status3
ok("check_username_live: too short -> " + msg3)

# ── cleanup ───────────────────────────────────────────────────────────────────

_cleanup()
ok("Cleanup done")

print("")
print("=" * 40)
print("ALL TESTS PASSED")
print("=" * 40)
