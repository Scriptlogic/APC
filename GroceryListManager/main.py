# =============================================================================
# FILE: main.py
# PURPOSE:
#   This is the ENTRY POINT of the application.
#   It contains the entire Tkinter GUI:
#   - LoginScreen   : The first screen shown when the app starts.
#   - RegisterScreen: The account creation form.
#   - Dashboard     : The main grocery management screen after login.
#   - App           : The root controller that starts everything.
#
# HOW IT CONNECTS TO OTHER FILES:
#   - Imports database.py for all database operations.
#   - Imports auth.py for login and registration.
#
# APPLICATION EXECUTION FLOW:
#   python main.py
#       |
#       v
#   if __name__ == "__main__": App()   <-- Python runs this block first
#       |
#       v
#   App.__init__()
#       |
#       |--> database.initialise_database()  <-- creates DB tables if needed
#       |--> self.root = tk.Tk()             <-- creates the main window
#       |--> self._show_login()              <-- shows the login screen
#       v
#   LoginScreen appears (user types credentials)
#       |
#       v
#   LoginScreen._do_login()
#       |--> auth.login_user()               <-- verifies credentials
#       |--> self.destroy()                  <-- removes login screen
#       v
#   App._show_dashboard() --> Dashboard appears
#       |
#       v
#   User manages groceries --> Dashboard._logout() --> _show_login() again
#
# STANDARD LIBRARY MODULES USED:
#   - tkinter          : Python's built-in GUI library.
#   - tkinter.ttk      : Themed widgets (Treeview, Combobox, Scrollbar, Style).
#   - tkinter.messagebox : Popup dialog boxes.
#   - tkinter.filedialog : File save/open dialogs.
# =============================================================================

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import database   # our database.py - all SQLite operations
import auth       # our auth.py - login, register, password hashing


# =============================================================================
# CONSTANTS  (values that never change during the program)
# =============================================================================

APP_TITLE   = "Grocery List Manager"
APP_TAGLINE = "Your groceries, organised effortlessly."

UNITS = ["Kilogram (kg)", "Gram (gm)", "Liter", "Milliliter (ml)",
         "Dozen", "Piece", "Packet", "Bottle"]

CATEGORIES = ["Vegetables", "Fruits", "Dairy", "Grains", "Snacks",
              "Beverages", "Household", "Personal Care", "Other"]

# Common grocery items shown as suggestions in the Item Name dropdown.
# The user can pick one OR type their own custom name.
COMMON_ITEMS = [
    # Vegetables
    "Onion", "Tomato", "Potato", "Garlic", "Ginger", "Carrot", "Cabbage",
    "Cauliflower", "Brinjal", "Spinach", "Capsicum", "Green Chilli",
    "Cucumber", "Peas", "Beetroot", "Radish", "Drumstick", "Lady Finger",
    # Fruits
    "Banana", "Apple", "Mango", "Orange", "Grapes", "Papaya", "Watermelon",
    "Pomegranate", "Pineapple", "Guava", "Lemon",
    # Dairy
    "Milk", "Curd", "Butter", "Cheese", "Paneer", "Ghee", "Cream",
    # Grains & Pulses
    "Rice", "Wheat Flour", "Atta", "Maida", "Sooji", "Poha",
    "Toor Dal", "Moong Dal", "Chana Dal", "Urad Dal", "Rajma", "Chana",
    # Spices & Masala
    "Salt", "Sugar", "Turmeric", "Red Chilli Powder", "Coriander Powder",
    "Cumin Seeds", "Mustard Seeds", "Garam Masala", "Pepper", "Cardamom",
    # Oils & Condiments
    "Cooking Oil", "Mustard Oil", "Coconut Oil", "Olive Oil",
    "Tomato Ketchup", "Vinegar", "Soy Sauce",
    # Snacks & Bakery
    "Bread", "Biscuits", "Namkeen", "Chips", "Noodles", "Pasta",
    # Beverages
    "Tea", "Coffee", "Sugar", "Juice", "Soft Drink", "Coconut Water",
    # Household
    "Soap", "Shampoo", "Detergent", "Dishwash", "Floor Cleaner",
    "Toilet Cleaner", "Broom", "Toothpaste", "Toothbrush",
    # Personal Care
    "Face Wash", "Body Lotion", "Deodorant", "Sanitary Pads", "Razor",
]


# =============================================================================
# THEMES dictionary
# Stores two colour palettes: "light" and "dark".
# Every widget reads its colour from this dict.
# Switching themes = changing which palette is used.
# =============================================================================
THEMES = {
    "light": {
        "bg":          "#F0F2F5",   # main window background
        "card_bg":     "#FFFFFF",   # card/panel background
        "card_border": "#D8DEE9",   # card border colour
        "card_shadow": "#C8D0DC",   # card drop-shadow colour
        "entry_bg":    "#FAFBFC",   # text field background
        "entry_fg":    "#1A1A2E",   # text field text colour
        "entry_bd":    "#CBD5E1",   # text field border colour
        "entry_focus": "#3B82F6",   # text field border when focused
        "btn_primary": "#3B82F6",   # primary (blue) button
        "btn_pri_fg":  "#FFFFFF",
        "btn_success": "#10B981",   # success (green) button
        "btn_suc_fg":  "#FFFFFF",
        "btn_danger":  "#EF4444",   # danger (red) button
        "btn_dan_fg":  "#FFFFFF",
        "btn_accent":  "#8B5CF6",   # accent (purple) button
        "btn_acc_fg":  "#FFFFFF",
        "btn_warn":    "#F59E0B",   # warning (amber) button
        "btn_war_fg":  "#FFFFFF",
        "btn_neutral": "#E5E7EB",   # neutral (grey) button
        "btn_neu_fg":  "#374151",
        "heading_fg":  "#111827",   # heading text
        "label_fg":    "#374151",   # form label text
        "sublabel_fg": "#6B7280",
        "hint_fg":     "#9CA3AF",   # hint/placeholder text
        "header_bg":   "#1E3A5F",   # top navigation bar (navy)
        "header_fg":   "#FFFFFF",
        "card1":       "#3B82F6",   # Total Items card (blue)
        "card2":       "#10B981",   # Purchased card (green)
        "card3":       "#F59E0B",   # Pending card (amber)
        "card4":       "#8B5CF6",   # Est. Cost card (purple)
        "tree_bg":     "#FFFFFF",   # table background
        "tree_fg":     "#1A1A2E",   # table text
        "tree_alt":    "#F8FAFC",   # alternating row background
        "tree_sel":    "#3B82F6",   # selected row background
        "tree_sel_fg": "#FFFFFF",   # selected row text
        "tree_hdr_bg": "#1E3A5F",   # table header background
        "tree_hdr_fg": "#FFFFFF",
        "success_fg":  "#059669",   # success message text
        "error_fg":    "#DC2626",   # error message text
        "footer_bg":   "#E5E7EB",   # footer background
        "footer_fg":   "#6B7280",   # footer text
        "divider":     "#E5E7EB",   # horizontal divider line
    },
    "dark": {
        "bg":          "#0F172A",
        "card_bg":     "#1E293B",
        "card_border": "#334155",
        "card_shadow": "#0A0F1A",
        "entry_bg":    "#273549",
        "entry_fg":    "#E2E8F0",
        "entry_bd":    "#475569",
        "entry_focus": "#3B82F6",
        "btn_primary": "#3B82F6",
        "btn_pri_fg":  "#FFFFFF",
        "btn_success": "#10B981",
        "btn_suc_fg":  "#FFFFFF",
        "btn_danger":  "#EF4444",
        "btn_dan_fg":  "#FFFFFF",
        "btn_accent":  "#8B5CF6",
        "btn_acc_fg":  "#FFFFFF",
        "btn_warn":    "#F59E0B",
        "btn_war_fg":  "#1A1A2E",
        "btn_neutral": "#334155",
        "btn_neu_fg":  "#E2E8F0",
        "heading_fg":  "#F1F5F9",
        "label_fg":    "#CBD5E1",
        "sublabel_fg": "#94A3B8",
        "hint_fg":     "#64748B",
        "header_bg":   "#0F172A",
        "header_fg":   "#E2E8F0",
        "card1":       "#3B82F6",
        "card2":       "#10B981",
        "card3":       "#F59E0B",
        "card4":       "#8B5CF6",
        "tree_bg":     "#1E293B",
        "tree_fg":     "#E2E8F0",
        "tree_alt":    "#243447",
        "tree_sel":    "#3B82F6",
        "tree_sel_fg": "#FFFFFF",
        "tree_hdr_bg": "#0F172A",
        "tree_hdr_fg": "#94A3B8",
        "success_fg":  "#34D399",
        "error_fg":    "#F87171",
        "footer_bg":   "#1E293B",
        "footer_fg":   "#64748B",
        "divider":     "#334155",
    },
}


# =============================================================================
# SHARED WIDGET HELPERS
# Standalone functions that create reusable Tkinter widgets.
# =============================================================================

def flat_btn(parent, text, command, bg, fg,
             font=("Segoe UI", 10, "bold"), padx=14, pady=7, width=None):
    """
    FUNCTION: flat_btn()
    Creates a flat-styled tk.Button widget.
    We use tk.Button (not ttk.Button) because ttk buttons ignore bg/fg on Windows.
    PARAMETERS:
        parent  - parent container widget
        text    - button label text
        command - function to call when clicked
        bg      - background hex colour
        fg      - foreground (text) hex colour
        font    - font tuple
        padx    - horizontal padding inside button
        pady    - vertical padding inside button
        width   - optional fixed character width
    RETURNS: A tk.Button widget (caller must pack/grid it).
    CALLED FROM: LoginScreen._build(), RegisterScreen._build(),
                 Dashboard._build_header(), _build_form_panel(), _build_table_panel()
    """
    kw = dict(text=text, command=command, bg=bg, fg=fg,
              font=font, relief="flat", cursor="hand2",
              padx=padx, pady=pady, bd=0,
              activebackground=bg, activeforeground=fg)
    if width:
        kw["width"] = width
    return tk.Button(parent, **kw)


def styled_entry(parent, var, c, show=""):
    """
    FUNCTION: styled_entry()
    Creates a full-width text input with a custom border frame.
    Uses border_frame > inner_frame > Entry structure for consistent styling.
    PARAMETERS:
        parent - parent container
        var    - tk.StringVar() linked to this entry
        c      - colour palette dict from THEMES
        show   - character to show instead of typed text (e.g. "*" for passwords)
    RETURNS: (entry_widget, border_frame) tuple.
    CALLED FROM: LoginScreen._build(), RegisterScreen._build()
    """
    border = tk.Frame(parent, bg=c["entry_bd"])
    border.pack(fill="x", pady=(4, 0))
    inner = tk.Frame(border, bg=c["entry_bg"])
    inner.pack(fill="x", padx=1, pady=1)   # 1px padding creates the border effect
    e = tk.Entry(inner, textvariable=var, show=show,
                 font=("Segoe UI", 11),
                 bg=c["entry_bg"], fg=c["entry_fg"],
                 insertbackground=c["entry_fg"],
                 relief="flat", bd=0)
    e.pack(fill="x", ipady=8, padx=12)
    return e, border


def pw_field(parent, var, c, label="Password"):
    """
    FUNCTION: pw_field()
    Creates a complete password field: label + entry + Show/Hide toggle button.
    The toggle button sits INSIDE the right side of the entry box.
    Uses a mutable list [False] so the inner _toggle() closure can modify the state.
    PARAMETERS:
        parent - parent container
        var    - tk.StringVar() for the password
        c      - colour palette dict from THEMES
        label  - label text shown above the field
    RETURNS: The tk.Entry widget.
    CALLED FROM: LoginScreen._build(), RegisterScreen._build()
    """
    tk.Label(parent, text=label,
             font=("Segoe UI", 9, "bold"),
             bg=c["card_bg"], fg=c["label_fg"],
             anchor="w").pack(fill="x", pady=(12, 0))

    border = tk.Frame(parent, bg=c["entry_bd"])
    border.pack(fill="x", pady=(4, 0))
    inner = tk.Frame(border, bg=c["entry_bg"])
    inner.pack(fill="x", padx=1, pady=1)

    entry = tk.Entry(inner, textvariable=var, show="*",
                     font=("Segoe UI", 11),
                     bg=c["entry_bg"], fg=c["entry_fg"],
                     insertbackground=c["entry_fg"],
                     relief="flat", bd=0)
    entry.pack(side="left", fill="x", expand=True, ipady=8, padx=(12, 0))

    # showing[0] tracks whether password is visible.
    # We use a list because inner functions cannot reassign plain variables.
    showing = [False]

    def _toggle():
        # Flip the visibility state
        showing[0] = not showing[0]
        entry.config(show="" if showing[0] else "*")
        tog.config(text="Hide" if showing[0] else "Show")

    # Show/Hide button lives inside the entry box on the right
    tog = tk.Button(inner, text="Show",
                    command=_toggle,
                    font=("Segoe UI", 8, "bold"),
                    bg=c["entry_bg"], fg=c["btn_primary"],
                    relief="flat", bd=0, cursor="hand2",
                    activebackground=c["entry_bg"],
                    activeforeground=c["btn_primary"],
                    padx=10)
    tog.pack(side="right", padx=(0, 4))
    return entry


def divider(parent, c):
    """
    FUNCTION: divider()
    Creates a thin 1px horizontal line to visually separate form sections.
    CALLED FROM: LoginScreen._build(), RegisterScreen._build()
    """
    tk.Frame(parent, bg=c["divider"], height=1).pack(fill="x", pady=(16, 0))


# =============================================================================
# CLASS: LoginScreen
# PURPOSE: The first screen shown when the app starts.
# INHERITS: tk.Frame - so it is itself a Tkinter container widget.
# =============================================================================
class LoginScreen(tk.Frame):
    """Polished centred login card."""

    def __init__(self, master, on_login_success):
        """
        CONSTRUCTOR: LoginScreen.__init__()
        Stores parameters, builds the UI, and packs this frame.
        PARAMETERS:
            master           - root tk.Tk window
            on_login_success - function to call after login (App._show_dashboard)
        CALLED FROM: App._show_login()
        """
        super().__init__(master)    # initialise the parent tk.Frame
        self.master = master
        self.on_login_success = on_login_success
        self._build()               # build all widgets
        self.pack(fill="both", expand=True)   # fill the whole window

    def _build(self):
        """
        METHOD: LoginScreen._build()
        Creates all widgets: top stripe, centred card with shadow, logo, title,
        username field, password field, error label, and three buttons.
        CALLED FROM: __init__()
        CALLS: styled_entry(), pw_field(), flat_btn(), divider()
        """
        c = THEMES["light"]    # login screen always uses light theme
        self.configure(bg=c["bg"])

        # Thin navy decorative stripe at the top of the window
        tk.Frame(self, bg=c["header_bg"], height=4).pack(fill="x", side="top")

        # Centred wrapper - placed at 50% x, 50% y of the window
        wrap = tk.Frame(self, bg=c["bg"])
        wrap.place(relx=0.5, rely=0.5, anchor="center")

        # Drop-shadow effect: darker frame behind the card, offset by 3px
        shadow = tk.Frame(wrap, bg=c["card_shadow"])
        shadow.pack()
        card = tk.Frame(shadow, bg=c["card_bg"],
                        highlightbackground=c["card_border"],
                        highlightthickness=1)
        card.pack(padx=(0, 3), pady=(0, 3))

        # body adds internal padding around all card content
        body = tk.Frame(card, bg=c["card_bg"])
        body.pack(padx=48, pady=(30, 34))

        # Logo badge - fixed size 62x62, shows "GLM"
        badge = tk.Frame(body, bg=c["btn_primary"], width=62, height=62)
        badge.pack()
        badge.pack_propagate(False)   # prevent frame from shrinking to fit content
        tk.Label(badge, text="GLM",
                 font=("Segoe UI", 16, "bold"),
                 bg=c["btn_primary"], fg="#FFFFFF"
                 ).place(relx=0.5, rely=0.5, anchor="center")

        # App title and tagline
        tk.Label(body, text=APP_TITLE,
                 font=("Segoe UI", 22, "bold"),
                 bg=c["card_bg"], fg=c["heading_fg"]).pack(pady=(14, 0))
        tk.Label(body, text=APP_TAGLINE,
                 font=("Segoe UI", 9),
                 bg=c["card_bg"], fg=c["hint_fg"]).pack(pady=(4, 22))

        # Username label + entry
        # StringVar() links the Entry widget to a Python variable we can read
        tk.Label(body, text="Username",
                 font=("Segoe UI", 9, "bold"),
                 bg=c["card_bg"], fg=c["label_fg"],
                 anchor="w").pack(fill="x")
        self.user_var = tk.StringVar()
        self.user_entry, _ = styled_entry(body, self.user_var, c)

        # Password field with built-in Show/Hide toggle button
        self.pw_var = tk.StringVar()
        self.pw_entry = pw_field(body, self.pw_var, c, "Password")

        # Error label - shown in red when login fails
        # textvariable means the label text updates automatically when err_var changes
        self.err_var = tk.StringVar()
        tk.Label(body, textvariable=self.err_var,
                 fg=c["error_fg"], bg=c["card_bg"],
                 font=("Segoe UI", 9), wraplength=300,
                 anchor="w").pack(fill="x", pady=(10, 0))

        divider(body, c)   # horizontal separator line

        # Login button - full width, blue
        flat_btn(body, "Login", self._do_login,     # calls _do_login when clicked
                 c["btn_primary"], c["btn_pri_fg"],
                 font=("Segoe UI", 11, "bold"),
                 padx=0, pady=11, width=28
                 ).pack(fill="x", pady=(14, 6))

        # Create Account button - full width, green
        flat_btn(body, "Create Account", self._open_register,  # calls _open_register
                 c["btn_success"], c["btn_suc_fg"],
                 font=("Segoe UI", 10, "bold"),
                 padx=0, pady=10, width=28
                 ).pack(fill="x", pady=(0, 6))

        # Clear Fields button - full width, neutral grey
        flat_btn(body, "Clear Fields", self._clear,   # calls _clear
                 c["btn_neutral"], c["btn_neu_fg"],
                 font=("Segoe UI", 9),
                 padx=0, pady=8, width=28
                 ).pack(fill="x")

        tk.Label(body,
                 text="Don't have an account? Click Create Account.",
                 font=("Segoe UI", 8),
                 bg=c["card_bg"], fg=c["hint_fg"]
                 ).pack(pady=(16, 0))

        # Bind Enter key to login. Lambda ignores the event argument.
        self.master.bind("<Return>", lambda e: self._do_login())
        # After 80ms, focus the username field so user can type immediately
        self.after(80, lambda: self.user_entry.focus_set())

    def _do_login(self):
        """
        METHOD: LoginScreen._do_login()
        Called when Login button is clicked OR Enter key is pressed.
        Calls auth.login_user() to verify credentials.
        On success: destroys this screen and shows the Dashboard.
        On failure: shows red error message.
        CALLED BY: Login button click, <Return> key binding.
        CALLS: auth.login_user(), self.destroy(), self.on_login_success()
        """
        # auth.login_user() returns (True, user_dict) or (False, "error string")
        ok_flag, result = auth.login_user(
            self.user_var.get(),   # read username from StringVar
            self.pw_var.get()      # read password from StringVar
        )
        if ok_flag:
            self.err_var.set("")             # clear error label
            self.master.unbind("<Return>")   # remove Enter key binding
            self.destroy()                   # remove login screen from window
            self.on_login_success(result)    # calls App._show_dashboard(user_dict)
        else:
            self.err_var.set("  " + result)  # show error message in red

    def _open_register(self):
        """
        METHOD: LoginScreen._open_register()
        Called when Create Account button is clicked.
        Hides (NOT destroys) the login screen and shows RegisterScreen.
        CALLED BY: Create Account button click.
        CALLS: self.pack_forget(), RegisterScreen()
        """
        self.master.unbind("<Return>")    # remove login's Enter binding
        self.pack_forget()                # hide login (keep in memory for restore)
        RegisterScreen(self.master, on_back=self._restore)

    def _restore(self):
        """
        METHOD: LoginScreen._restore()
        Called when user clicks Back to Login on the RegisterScreen.
        Shows the login screen again and re-binds the Enter key.
        CALLED FROM: RegisterScreen._go_back() via self.on_back() callback.
        """
        self._clear()
        self.pack(fill="both", expand=True)   # show login screen again
        self.master.bind("<Return>", lambda e: self._do_login())
        self.user_entry.focus_set()

    def _clear(self):
        """
        METHOD: LoginScreen._clear()
        Resets all form fields and the error message to empty.
        CALLED BY: Clear Fields button click, self._restore()
        """
        self.user_var.set("")   # StringVar.set("") clears the Entry widget
        self.pw_var.set("")
        self.err_var.set("")


# =============================================================================
# CLASS: RegisterScreen
# PURPOSE: Registration form with live username validation.
# INHERITS: tk.Frame
# =============================================================================
class RegisterScreen(tk.Frame):
    """Registration form with live username validation."""

    _RULES = ("4-20 chars  |  Start with a letter  |"
              "  Letters, digits, underscore only  |  No spaces")

    def __init__(self, master, on_back):
        """
        CONSTRUCTOR: RegisterScreen.__init__()
        PARAMETERS:
            master  - root tk.Tk window
            on_back - callback to return to login (LoginScreen._restore)
        CALLED FROM: LoginScreen._open_register()
        """
        super().__init__(master)
        self.master  = master
        self.on_back = on_back
        self._build()
        self.pack(fill="both", expand=True)

    def _build(self):
        """
        METHOD: RegisterScreen._build()
        Creates all registration form widgets.
        KEY FEATURE: trace_add("write", _on_username_change) triggers live
        validation every time a character is typed in the username field.
        CALLED FROM: __init__()
        """
        c = THEMES["light"]
        self.configure(bg=c["bg"])

        tk.Frame(self, bg=c["header_bg"], height=4).pack(fill="x", side="top")

        wrap = tk.Frame(self, bg=c["bg"])
        wrap.place(relx=0.5, rely=0.5, anchor="center")

        shadow = tk.Frame(wrap, bg=c["card_shadow"])
        shadow.pack()
        card = tk.Frame(shadow, bg=c["card_bg"],
                        highlightbackground=c["card_border"],
                        highlightthickness=1)
        card.pack(padx=(0, 3), pady=(0, 3))

        body = tk.Frame(card, bg=c["card_bg"])
        body.pack(padx=48, pady=(28, 32))

        # Green badge (different from login's blue badge)
        badge = tk.Frame(body, bg=c["btn_success"], width=62, height=62)
        badge.pack()
        badge.pack_propagate(False)
        tk.Label(badge, text="NEW",
                 font=("Segoe UI", 14, "bold"),
                 bg=c["btn_success"], fg="#FFFFFF"
                 ).place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(body, text="Create Account",
                 font=("Segoe UI", 21, "bold"),
                 bg=c["card_bg"], fg=c["heading_fg"]).pack(pady=(14, 0))
        tk.Label(body, text="Join to start managing your groceries",
                 font=("Segoe UI", 9),
                 bg=c["card_bg"], fg=c["hint_fg"]).pack(pady=(4, 20))

        # Username field
        tk.Label(body, text="Username",
                 font=("Segoe UI", 9, "bold"),
                 bg=c["card_bg"], fg=c["label_fg"],
                 anchor="w").pack(fill="x")
        self.user_var = tk.StringVar()
        self.user_entry, _ = styled_entry(body, self.user_var, c)

        # Live hint label below username
        self.user_hint_var = tk.StringVar(value=self._RULES)
        self.user_hint_lbl = tk.Label(body, textvariable=self.user_hint_var,
                                      font=("Segoe UI", 8),
                                      bg=c["card_bg"], fg=c["hint_fg"],
                                      anchor="w", wraplength=300,
                                      justify="left")
        self.user_hint_lbl.pack(fill="x", pady=(4, 0))

        # trace_add: call _on_username_change() every time user_var changes
        # "write" means trigger on any write to the variable (i.e., every keystroke)
        self.user_var.trace_add("write", self._on_username_change)

        # Password field
        self.pw_var = tk.StringVar()
        pw_field(body, self.pw_var, c, "Password  (min 6 characters)")

        # Password strength hint (updates as user types)
        self.pw_strength_var = tk.StringVar()
        tk.Label(body, textvariable=self.pw_strength_var,
                 font=("Segoe UI", 8), bg=c["card_bg"],
                 fg=c["hint_fg"], anchor="w").pack(fill="x", pady=(4, 0))
        self.pw_var.trace_add("write", self._on_pw_change)

        # Confirm Password field
        self.cpw_var = tk.StringVar()
        pw_field(body, self.cpw_var, c, "Confirm Password")

        # Error and success message labels
        self.err_var = tk.StringVar()
        tk.Label(body, textvariable=self.err_var,
                 fg=c["error_fg"], bg=c["card_bg"],
                 font=("Segoe UI", 9), wraplength=300,
                 anchor="w").pack(fill="x", pady=(10, 0))

        self.ok_var = tk.StringVar()
        tk.Label(body, textvariable=self.ok_var,
                 fg=c["success_fg"], bg=c["card_bg"],
                 font=("Segoe UI", 9), wraplength=300,
                 anchor="w").pack(fill="x")

        divider(body, c)

        # Register button - green
        flat_btn(body, "Register", self._do_register,
                 c["btn_success"], c["btn_suc_fg"],
                 font=("Segoe UI", 11, "bold"),
                 padx=0, pady=11, width=28
                 ).pack(fill="x", pady=(14, 6))

        # Back to Login button - blue
        flat_btn(body, "Back to Login", self._go_back,
                 c["btn_primary"], c["btn_pri_fg"],
                 font=("Segoe UI", 10, "bold"),
                 padx=0, pady=10, width=28
                 ).pack(fill="x")

        self.master.bind("<Return>", lambda e: self._do_register())
        self.user_entry.focus_set()

    def _on_username_change(self, *_):
        """
        METHOD: RegisterScreen._on_username_change()
        Called automatically every keystroke in the username field (via trace_add).
        Updates the hint label: grey rules -> green "available" -> red "error/taken".
        CALLED BY: trace_add("write", self._on_username_change) in _build()
        CALLS: auth.check_username_live()
        """
        raw = self.user_var.get()
        c = THEMES["light"]

        if not raw.strip():
            # Field is empty - show the rules in grey
            self.user_hint_var.set(self._RULES)
            self.user_hint_lbl.config(fg=c["hint_fg"])
            return

        # Check format validity and database availability
        status, msg = auth.check_username_live(raw)
        if status == "ok":
            self.user_hint_var.set("OK  " + msg)
            self.user_hint_lbl.config(fg=c["success_fg"])   # green
        else:
            self.user_hint_var.set("X  " + msg)
            self.user_hint_lbl.config(fg=c["error_fg"])     # red

    def _on_pw_change(self, *_):
        """
        METHOD: RegisterScreen._on_pw_change()
        Called automatically every keystroke in the password field.
        Shows password strength based on length.
        CALLED BY: trace_add("write", self._on_pw_change) in _build()
        """
        n = len(self.pw_var.get())
        if   n == 0:  self.pw_strength_var.set("")
        elif n <  6:  self.pw_strength_var.set("Strength: Too short (need 6+)")
        elif n <  8:  self.pw_strength_var.set("Strength: Weak")
        elif n < 12:  self.pw_strength_var.set("Strength: Moderate")
        else:         self.pw_strength_var.set("Strength: Strong")

    def _do_register(self):
        """
        METHOD: RegisterScreen._do_register()
        Called when Register button is clicked or Enter is pressed.
        Calls auth.register_user() to validate and create the account.
        On success: shows message and redirects to login after 1.5 seconds.
        CALLED BY: Register button click, <Return> key.
        CALLS: auth.register_user(), self.master.after()
        """
        ok_flag, msg = auth.register_user(
            self.user_var.get(),    # username
            self.pw_var.get(),      # password
            self.cpw_var.get()      # confirm password
        )
        if ok_flag:
            self.err_var.set("")
            self.ok_var.set("Success! " + msg + "  Redirecting...")
            # after(1500, func) = call func after 1500 milliseconds (1.5 seconds)
            self.master.after(1500, self._go_back)
        else:
            self.ok_var.set("")
            self.err_var.set("Error: " + msg)

    def _go_back(self):
        """
        METHOD: RegisterScreen._go_back()
        Destroys the registration screen and calls on_back() to return to login.
        CALLED BY: Back to Login button, master.after() after successful register.
        """
        self.master.unbind("<Return>")
        self.destroy()        # permanently remove this screen
        self.on_back()        # calls LoginScreen._restore()

# =============================================================================
# CLASS: Dashboard
# PURPOSE:
#   The main application screen shown after successful login.
#   Contains everything needed to manage the grocery list:
#     - Header bar: app name, username, theme toggle, logout
#     - Stat cards: Total, Purchased, Pending, Estimated Cost
#     - Left panel: Add/Edit form with all CRUD buttons
#     - Right panel: Grocery table with search and filter bar
#     - Footer bar
#
# KEY ATTRIBUTES:
#   self.user_id     - integer ID of logged-in user (used in ALL DB calls)
#   self.username    - display name shown in the header
#   self.theme       - current theme string: "light" or "dark"
#   self.c           - current colour dict: THEMES[self.theme]
#   self.selected_id - DB ID of the row currently selected in the table
#                      (None = nothing selected)
#   self.tree        - the ttk.Treeview table widget
#   self.v_name, self.v_qty, self.v_unit, self.v_price,
#   self.v_cat, self.v_bought  - StringVar / BooleanVar linked to form fields
#   self.search_var  - StringVar for the search box
#   self.filter_cat  - StringVar for the category filter dropdown
#   self.filter_status - StringVar for the status filter dropdown
#   self.msg_var     - StringVar for the feedback message below the buttons
#   self.msg_label   - the Label widget for that feedback message
# =============================================================================
class Dashboard(tk.Frame):
    """Full grocery-management dashboard shown after login."""

    def __init__(self, master, user_row, on_logout):
        """
        CONSTRUCTOR: Dashboard.__init__()
        Stores user data, picks the saved theme, and builds the entire UI.

        PARAMETERS:
            master   - root tk.Tk window
            user_row - dict with logged-in user's DB row:
                       {"id", "username", "theme_preference", ...}
            on_logout - callback called after logout -> App._show_login()

        CALLED FROM: App._show_dashboard()
        """
        super().__init__(master)
        self.master    = master
        self.user      = user_row
        self.user_id   = user_row["id"]          # used in every DB query
        self.username  = user_row["username"]    # displayed in header
        self.on_logout = on_logout               # called when user logs out
        self.theme     = user_row["theme_preference"]  # "light" or "dark"
        self.c         = THEMES[self.theme]      # active colour palette
        self.selected_id = None                  # no row selected yet
        self._build()
        self.pack(fill="both", expand=True)

    # -------------------------------------------------------------------------
    def _build(self):
        """
        METHOD: Dashboard._build()
        Master builder - calls every section builder in the correct order.

        BUILD ORDER (order matters for Tkinter's pack layout):
          1. _apply_ttk_style() - styles ttk widgets
          2. configure bg
          3. _build_header()  - packed to top
          4. _build_stats()   - packed to top (below header)
          5. _build_footer()  - packed to BOTTOM first (reserves space)
          6. _build_main_area() - fills remaining space between top and bottom
          7. refresh_table()  - loads data into the grocery table
          8. refresh_stats()  - loads numbers into the stat cards

        WHY FOOTER BEFORE MAIN AREA?
          If we packed the main area first with expand=True it would take all
          remaining space and push the footer off screen. Packing footer with
          side="bottom" first reserves its height before the main area expands.

        CALLED FROM: __init__(), _rebuild_dashboard()
        """
        self._apply_ttk_style()
        self.configure(bg=self.c["bg"])
        self._build_header()
        self._build_stats()
        self._build_footer()       # anchor to bottom FIRST
        self._build_main_area()    # fills everything between header+stats and footer
        self.refresh_table()
        self.refresh_stats()

    # -------------------------------------------------------------------------
    def _apply_ttk_style(self):
        """
        METHOD: Dashboard._apply_ttk_style()
        Configures colours for ttk widgets (Treeview, Combobox, Scrollbar).
        ttk widgets have their own separate styling system (ttk.Style),
        which is why we cannot just pass bg= to them like normal tk widgets.

        CALLED FROM: _build()
        """
        c = self.c
        s = ttk.Style()
        s.theme_use("clam")   # "clam" allows the most colour customisation on Windows

        # Style the Treeview (the grocery table)
        s.configure("Treeview",
                    background=c["tree_bg"], foreground=c["tree_fg"],
                    fieldbackground=c["tree_bg"], rowheight=28,
                    font=("Segoe UI", 10))
        s.configure("Treeview.Heading",      # column header row
                    background=c["tree_hdr_bg"], foreground=c["tree_hdr_fg"],
                    font=("Segoe UI", 10, "bold"), relief="flat")
        s.map("Treeview",
              background=[("selected", c["tree_sel"])],
              foreground=[("selected", c["tree_sel_fg"])])

        # Style Combobox dropdowns
        s.configure("TCombobox",
                    fieldbackground=c["entry_bg"], background=c["entry_bg"],
                    foreground=c["entry_fg"],
                    selectbackground=c["tree_sel"],
                    selectforeground=c["tree_sel_fg"])
        s.map("TCombobox",
              fieldbackground=[("readonly", c["entry_bg"])],
              foreground=[("readonly", c["entry_fg"])])

        # Style scrollbars
        s.configure("Vertical.TScrollbar",
                    troughcolor=c["bg"], background=c["card_border"])
        s.configure("Horizontal.TScrollbar",
                    troughcolor=c["bg"], background=c["card_border"])

    # -------------------------------------------------------------------------
    def _build_header(self):
        """
        METHOD: Dashboard._build_header()
        Creates the top navy navigation bar.
        Left side : [GLM] logo | App title | divider | username
        Right side: theme toggle button | logout button

        CALLED FROM: _build()
        CALLS: flat_btn(), self._toggle_theme(), self._logout()
        """
        c = self.c
        hdr = tk.Frame(self, bg=c["header_bg"])
        hdr.pack(fill="x", side="top")

        # Left side of the header
        left = tk.Frame(hdr, bg=c["header_bg"])
        left.pack(side="left", padx=16, pady=10)
        tk.Label(left, text="[GLM]",
                 font=("Segoe UI", 13, "bold"),
                 bg=c["header_bg"], fg="#93C5FD").pack(side="left")
        tk.Label(left, text="  " + APP_TITLE,
                 font=("Segoe UI", 14, "bold"),
                 bg=c["header_bg"], fg="#FFFFFF").pack(side="left")
        tk.Frame(left, bg="#334155", width=1, height=20   # vertical divider
                 ).pack(side="left", padx=14)
        tk.Label(left, text=self.username,
                 font=("Segoe UI", 10),
                 bg=c["header_bg"], fg="#94A3B8").pack(side="left")

        # Right side of the header
        right = tk.Frame(hdr, bg=c["header_bg"])
        right.pack(side="right", padx=16, pady=10)

        # Theme toggle button - label and colour change based on current theme
        theme_lbl = "Light Mode" if self.theme == "dark" else "Dark Mode"
        theme_bg  = "#1E40AF" if self.theme == "dark" else "#334155"
        flat_btn(right, " " + theme_lbl, self._toggle_theme,   # calls _toggle_theme
                 theme_bg, "#FFFFFF",
                 font=("Segoe UI", 9, "bold"),
                 padx=12, pady=6).pack(side="right", padx=(8, 0))

        flat_btn(right, "  Logout  ", self._logout,   # calls _logout
                 c["btn_danger"], c["btn_dan_fg"],
                 font=("Segoe UI", 9, "bold"),
                 padx=12, pady=6).pack(side="right")

    # -------------------------------------------------------------------------
    def _build_stats(self):
        """
        METHOD: Dashboard._build_stats()
        Creates the row frame for the four stat cards and calls
        _populate_stat_cards() to create the cards inside it.

        CALLED FROM: _build()
        CALLS: _populate_stat_cards()
        """
        c = self.c
        self.stats_row = tk.Frame(self, bg=c["bg"])
        self.stats_row.pack(fill="x", padx=16, pady=(12, 6), side="top")
        self._populate_stat_cards()

    # -------------------------------------------------------------------------
    def _populate_stat_cards(self):
        """
        METHOD: Dashboard._populate_stat_cards()
        Creates the four coloured summary cards inside stats_row.

        Each card shows:  large number on top, small label below.
        The value labels are stored as self.stat_total, self.stat_bought,
        self.stat_pend, self.stat_cost so refresh_stats() can update them.

        HOW setattr() WORKS:
          setattr(self, "stat_total", val_label)  is the same as:
          self.stat_total = val_label
          We use setattr() because the attribute name is built dynamically
          from the variable 'key' in the loop.

        CALLED FROM: _build_stats()
        """
        c = self.c
        for w in self.stats_row.winfo_children():
            w.destroy()   # clear any existing cards before re-building

        specs = [
            ("Total Items",   "total",  c["card1"]),   # blue
            ("Purchased",     "bought", c["card2"]),   # green
            ("Pending",       "pend",   c["card3"]),   # amber
            ("Categories",    "cats",   c["card4"]),   # purple
        ]
        for label, key, colour in specs:
            # Fixed-size coloured card
            card = tk.Frame(self.stats_row, bg=colour, width=190, height=78)
            card.pack(side="left", padx=5)
            card.pack_propagate(False)   # keep fixed size regardless of content

            # Centre the content inside the card using .place()
            inner = tk.Frame(card, bg=colour)
            inner.place(relx=0.5, rely=0.5, anchor="center")

            # Large number (updated by refresh_stats)
            val = tk.Label(inner, text="--",
                           font=("Segoe UI", 20, "bold"),
                           bg=colour, fg="#FFFFFF")
            val.pack()
            tk.Label(inner, text=label, font=("Segoe UI", 9),
                     bg=colour, fg="#DBEAFE").pack()

            # Dynamically store reference: self.stat_total, self.stat_bought, etc.
            setattr(self, f"stat_{key}", val)

    # -------------------------------------------------------------------------
    def _build_footer(self):
        """
        METHOD: Dashboard._build_footer()
        Creates the thin footer bar at the very bottom of the window.
        MUST be packed with side="bottom" BEFORE _build_main_area() is called.

        CALLED FROM: _build()
        """
        c = self.c
        foot = tk.Frame(self, bg=c["footer_bg"])
        foot.pack(fill="x", side="bottom")   # reserve space at the bottom
        tk.Label(foot,
                 text="  " + APP_TAGLINE + "   |   Data stored locally in SQLite",
                 font=("Segoe UI", 8), bg=c["footer_bg"],
                 fg=c["footer_fg"]).pack(side="left", pady=4, padx=6)
        tk.Label(foot, text="Grocery List Manager  2026  ",
                 font=("Segoe UI", 8), bg=c["footer_bg"],
                 fg=c["footer_fg"]).pack(side="right", pady=4, padx=6)

    # -------------------------------------------------------------------------
    def _build_main_area(self):
        """
        METHOD: Dashboard._build_main_area()
        Creates the two-column content area between the stats and footer.

        Column 0 (left, fixed min 270px) : form panel
        Column 1 (right, expandable)     : table panel

        GRID LAYOUT:
          columnconfigure(0, weight=0) = left column does NOT stretch
          columnconfigure(1, weight=1) = right column stretches to fill space

        CALLED FROM: _build()
        CALLS: _build_form_panel(), _build_table_panel()
        """
        c = self.c
        area = tk.Frame(self, bg=c["bg"])
        area.pack(fill="both", expand=True, padx=16, pady=(0, 6))
        area.columnconfigure(0, weight=0, minsize=270)
        area.columnconfigure(1, weight=1)
        area.rowconfigure(0, weight=1)
        self._build_form_panel(area)    # left column
        self._build_table_panel(area)   # right column

    # -------------------------------------------------------------------------
    def _build_form_panel(self, parent):
        """
        METHOD: Dashboard._build_form_panel()
        Creates the left panel: a scrollable form for adding/editing items.

        SCROLLABLE CANVAS PATTERN:
          Canvas (viewport) -> inner Frame (all content) -> scrollbar
          When inner frame grows beyond canvas height, scrollbar lets user scroll.
          _resize_inner() updates scrollregion when content changes.
          _resize_canvas() keeps inner frame width = canvas width.
          MouseWheel event enables mouse-wheel scrolling.

        FORM FIELDS (all linked to StringVar/BooleanVar):
          Item Name, Quantity, Unit (dropdown), Price per Unit, Category (dropdown),
          Mark as Purchased (checkbox)

        ACTION BUTTONS (3 columns x 2 rows grid):
          Row 0: Add | Update | Delete
          Row 1: Purchased | Pending | Clear

        CALLED FROM: _build_main_area()
        """
        c = self.c
        outer = tk.Frame(parent, bg=c["card_bg"],
                         highlightbackground=c["card_border"],
                         highlightthickness=1)
        outer.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        self.form_frame = outer   # stored for reference in _show_msg()

        # Canvas acts as the scrollable viewport
        canvas = tk.Canvas(outer, bg=c["card_bg"],
                           highlightthickness=0, width=256)
        vsb = ttk.Scrollbar(outer, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=vsb.set)
        vsb.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        # inner holds all the actual form widgets
        inner = tk.Frame(canvas, bg=c["card_bg"])
        win = canvas.create_window((0, 0), window=inner, anchor="nw")

        # Update scrollregion when inner frame content changes
        def _resize_inner(e):
            canvas.configure(scrollregion=canvas.bbox("all"))

        # Keep inner frame width synced to canvas width
        def _resize_canvas(e):
            canvas.itemconfig(win, width=e.width)

        inner.bind("<Configure>", _resize_inner)
        canvas.bind("<Configure>", _resize_canvas)

        # Mouse wheel scrolling: delta/120 = +/-1 on Windows
        def _wheel(e):
            canvas.yview_scroll(int(-1 * (e.delta / 120)), "units")
        canvas.bind_all("<MouseWheel>", _wheel)

        P = 14   # standard horizontal padding for all form content

        # Section heading
        tk.Label(inner, text="Add / Edit Item",
                 font=("Segoe UI", 12, "bold"),
                 bg=c["card_bg"], fg=c["heading_fg"]
                 ).pack(anchor="w", padx=P, pady=(14, 8))
        tk.Frame(inner, bg=c["divider"], height=1).pack(fill="x", padx=P)

        # Helper: creates a bold field label inside the form
        def lbl(text):
            tk.Label(inner, text=text,
                     font=("Segoe UI", 9, "bold"),
                     bg=c["card_bg"], fg=c["label_fg"],
                     anchor="w").pack(anchor="w", padx=P, pady=(9, 0))

        # Helper: creates a bordered text entry field linked to a StringVar
        def field(var):
            border = tk.Frame(inner, bg=c["entry_bd"])
            border.pack(fill="x", padx=P, pady=(3, 0))
            fi = tk.Frame(border, bg=c["entry_bg"])
            fi.pack(fill="x", padx=1, pady=1)
            e = tk.Entry(fi, textvariable=var,   # textvariable links widget to var
                         font=("Segoe UI", 10),
                         bg=c["entry_bg"], fg=c["entry_fg"],
                         insertbackground=c["entry_fg"],
                         relief="flat", bd=0)
            e.pack(fill="x", ipady=5, padx=8)
            return e

        # Helper: creates a read-only dropdown (Combobox) linked to a StringVar
        def combo(var, values):
            cb = ttk.Combobox(inner, textvariable=var,
                              values=values, state="readonly",
                              font=("Segoe UI", 10))
            cb.pack(fill="x", padx=P, ipady=3, pady=(3, 0))
            return cb

        # Form StringVars and BooleanVar - linked to the Entry/Combobox widgets
        # Reading values: self.v_name.get(), self.v_qty.get(), etc.
        self.v_name   = tk.StringVar()
        self.v_qty    = tk.StringVar()
        self.v_unit   = tk.StringVar(value=UNITS[0])       # default: first unit
        self.v_cat    = tk.StringVar(value=CATEGORIES[0])  # default: first category
        self.v_bought = tk.BooleanVar(value=False)         # default: not purchased

        # Item Name - editable Combobox so user can pick a suggestion OR type freely
        lbl("Item Name *")
        name_border = tk.Frame(inner, bg=c["entry_bd"])
        name_border.pack(fill="x", padx=P, pady=(3, 0))
        name_inner = tk.Frame(name_border, bg=c["entry_bg"])
        name_inner.pack(fill="x", padx=1, pady=1)
        self.name_combo = ttk.Combobox(name_inner, textvariable=self.v_name,
                                       values=COMMON_ITEMS,
                                       font=("Segoe UI", 10))
        # state="" means editable — user can type any custom name
        self.name_combo.config(state="normal")
        self.name_combo.pack(fill="x", ipady=4, padx=4)

        # Hint below the name field
        tk.Label(inner, text="Pick from list or type your own item name",
                 font=("Segoe UI", 7, "italic"),
                 bg=c["card_bg"], fg=c["hint_fg"],
                 anchor="w").pack(anchor="w", padx=P)

        lbl("Quantity *");  field(self.v_qty)
        lbl("Unit");        combo(self.v_unit, UNITS)
        lbl("Category");    combo(self.v_cat, CATEGORIES)

        # Mark as Purchased checkbox - linked to BooleanVar
        ck = tk.Frame(inner, bg=c["card_bg"])
        ck.pack(fill="x", padx=P, pady=(10, 0))
        tk.Checkbutton(ck, text=" Mark as Purchased",
                       variable=self.v_bought,   # BooleanVar: True/False
                       font=("Segoe UI", 9),
                       bg=c["card_bg"], fg=c["label_fg"],
                       activebackground=c["card_bg"],
                       selectcolor=c["entry_bg"],
                       cursor="hand2", relief="flat").pack(side="left")

        # Feedback message label (green=success, red=error)
        tk.Frame(inner, bg=c["divider"], height=1).pack(fill="x", padx=P, pady=(12, 0))
        self.msg_var   = tk.StringVar()
        self.msg_label = tk.Label(inner, textvariable=self.msg_var,
                                  font=("Segoe UI", 9),
                                  bg=c["card_bg"], fg=c["success_fg"],
                                  wraplength=235, justify="left")
        self.msg_label.pack(anchor="w", padx=P, pady=(4, 4))

        # Action buttons - 3 columns x 2 rows grid
        # Row 0: Add | Update | Delete
        # Row 1: Purchased | Pending | Clear
        bg_grid = tk.Frame(inner, bg=c["card_bg"])
        bg_grid.pack(fill="x", padx=P, pady=(2, 6))
        btn_specs = [
            # (label,       method to call,        bg colour,        fg colour)
            ("Add",       self._add_item,       c["btn_primary"], c["btn_pri_fg"]),
            ("Update",    self._update_item,    c["btn_accent"],  c["btn_acc_fg"]),
            ("Delete",    self._delete_item,    c["btn_danger"],  c["btn_dan_fg"]),
            ("Purchased", self._mark_purchased, c["btn_success"], c["btn_suc_fg"]),
            ("Pending",   self._mark_pending,   c["btn_warn"],    c["btn_war_fg"]),
            ("Clear",     self._clear_form,     c["btn_neutral"], c["btn_neu_fg"]),
        ]
        for i, (lbl_text, cmd, bg, fg) in enumerate(btn_specs):
            # i // 3 gives the row (0 for first 3 buttons, 1 for last 3)
            # i % 3  gives the column (0, 1, or 2)
            flat_btn(bg_grid, lbl_text, cmd, bg, fg,
                     font=("Segoe UI", 9, "bold"),
                     padx=6, pady=6).grid(
                         row=i // 3, column=i % 3,
                         padx=2, pady=3, sticky="ew")
        bg_grid.columnconfigure(0, weight=1)
        bg_grid.columnconfigure(1, weight=1)
        bg_grid.columnconfigure(2, weight=1)

        # Export to CSV button at the bottom of the form
        tk.Frame(inner, bg=c["divider"], height=1).pack(fill="x", padx=P, pady=(4, 0))
        flat_btn(inner, "Export to CSV", self._export_csv,   # calls _export_csv
                 c["card4"], "#FFFFFF",
                 font=("Segoe UI", 9, "bold"),
                 padx=10, pady=7
                 ).pack(fill="x", padx=P, pady=(8, 14))

    # -------------------------------------------------------------------------
    def _build_table_panel(self, parent):
        """
        METHOD: Dashboard._build_table_panel()
        Creates the right panel: filter bar + Treeview table + scrollbars.

        FILTER BAR contains:
          - Search box: trace_add fires refresh_table() on every keystroke
          - Category dropdown: fires refresh_table() on <<ComboboxSelected>>
          - Status dropdown: fires refresh_table() on <<ComboboxSelected>>
          - Refresh button: manually calls _refresh_all()

        TREEVIEW TABLE:
          ttk.Treeview displays grocery items in rows and columns.
          show="headings" means no tree hierarchy, just a plain table.
          Each row's iid (identifier) is set to str(item["id"]) from the DB,
          so selecting a row gives us the exact database primary key.

        CALLED FROM: _build_main_area()
        CALLS: self.refresh_table() (indirectly via trace/events)
        """
        c = self.c
        panel = tk.Frame(parent, bg=c["bg"])
        panel.grid(row=0, column=1, sticky="nsew")

        # --- Filter bar ---
        fbar = tk.Frame(panel, bg=c["card_bg"],
                        highlightbackground=c["card_border"],
                        highlightthickness=1)
        fbar.pack(fill="x", pady=(0, 8))
        fi = tk.Frame(fbar, bg=c["card_bg"])
        fi.pack(fill="x", padx=10, pady=8)

        def flbl(text):   # small helper for filter bar labels
            tk.Label(fi, text=text, font=("Segoe UI", 9, "bold"),
                     bg=c["card_bg"], fg=c["label_fg"]
                     ).pack(side="left", padx=(8, 3))

        # Search entry - every keystroke triggers refresh_table() via trace_add
        flbl("Search:")
        self.search_var = tk.StringVar()
        self.search_var.trace_add("write", lambda *_: self.refresh_table())
        tk.Entry(fi, textvariable=self.search_var,
                 font=("Segoe UI", 10),
                 bg=c["entry_bg"], fg=c["entry_fg"],
                 insertbackground=c["entry_fg"],
                 highlightbackground=c["entry_bd"],
                 highlightthickness=1, relief="flat",
                 width=20).pack(side="left", ipady=4)

        # Category filter dropdown
        flbl("Category:")
        self.filter_cat = tk.StringVar(value="All")
        cat_cb = ttk.Combobox(fi, textvariable=self.filter_cat,
                              values=["All"] + CATEGORIES,
                              state="readonly", width=13, font=("Segoe UI", 10))
        cat_cb.pack(side="left")
        # <<ComboboxSelected>> fires when user picks an option
        cat_cb.bind("<<ComboboxSelected>>", lambda e: self.refresh_table())

        # Status filter dropdown (All / Purchased / Pending)
        flbl("Status:")
        self.filter_status = tk.StringVar(value="All")
        stat_cb = ttk.Combobox(fi, textvariable=self.filter_status,
                               values=["All", "Purchased", "Pending"],
                               state="readonly", width=10, font=("Segoe UI", 10))
        stat_cb.pack(side="left")
        stat_cb.bind("<<ComboboxSelected>>", lambda e: self.refresh_table())

        # Refresh button - calls _refresh_all() (table + stats)
        flat_btn(fi, "Refresh", self._refresh_all,
                 c["btn_primary"], c["btn_pri_fg"],
                 font=("Segoe UI", 9, "bold"),
                 padx=10, pady=4).pack(side="right", padx=(0, 4))

        # --- Treeview table ---
        tf = tk.Frame(panel, bg=c["bg"])
        tf.pack(fill="both", expand=True)

        cols = ("id", "name", "qty", "unit", "cat", "status", "added")
        self.tree = ttk.Treeview(tf, columns=cols,
                                 show="headings", selectmode="browse")

        col_defs = [
            ("id",     "#",         45,  "center"),
            ("name",   "Item Name", 200, "w"),
            ("qty",    "Qty",       60,  "center"),
            ("unit",   "Unit",      115, "w"),
            ("cat",    "Category",  120, "w"),
            ("status", "Status",    100, "center"),
            ("added",  "Added",     95,  "center"),
        ]
        for cid, heading, width, anchor in col_defs:
            self.tree.heading(cid, text=heading)
            self.tree.column(cid, width=width, minwidth=36, anchor=anchor)

        # Attach vertical and horizontal scrollbars
        vsb = ttk.Scrollbar(tf, orient="vertical",   command=self.tree.yview)
        hsb = ttk.Scrollbar(tf, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.tree.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")
        hsb.grid(row=1, column=0, sticky="ew")
        tf.rowconfigure(0, weight=1)
        tf.columnconfigure(0, weight=1)

        # Bind row click: when user selects a row, populate the form
        # <<TreeviewSelect>> is a virtual event fired when selection changes
        self.tree.bind("<<TreeviewSelect>>", self._on_row_select)

    # -------------------------------------------------------------------------
    def refresh_table(self):
        """
        METHOD: Dashboard.refresh_table()
        Clears the Treeview and repopulates it from the database,
        applying the current search text, category filter, and status filter.

        HOW ALTERNATING ROW COLOURS WORK:
          Each inserted row gets a tag: "bought", "even", or "odd".
          tag_configure() sets the colour for each tag.
          "bought" rows get green foreground text.
          "even"/"odd" rows alternate between two slightly different backgrounds.

        HOW iid WORKS:
          Each row is inserted with iid=str(r["id"]).
          When the user clicks a row, self.tree.selection() returns that iid.
          int(sel[0]) then gives us back the database primary key.
          This is the safe way to know which DB row is selected.

        CALLED FROM:
          _build(), _refresh_all(),
          search_var trace (every search keystroke),
          cat_cb and stat_cb <<ComboboxSelected>> events,
          _add_item(), _update_item(), _delete_item(),
          _mark_purchased(), _mark_pending()

        CALLS: database.get_grocery_items()
        """
        # Clear all existing rows
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Fetch from database with current filter values
        rows = database.get_grocery_items(
            self.user_id,
            search=getattr(self, "search_var", tk.StringVar()).get(),
            category=getattr(self, "filter_cat", tk.StringVar(value="All")).get(),
            status=getattr(self, "filter_status", tk.StringVar(value="All")).get(),
        )
        c = self.c
        for i, r in enumerate(rows):
            stxt = "Purchased" if r["purchased"] else "Pending"
            tag  = "bought" if r["purchased"] else ("even" if i % 2 == 0 else "odd")
            self.tree.insert("", "end", iid=str(r["id"]),
                             values=(r["id"], r["name"],
                                     r["quantity"], r["unit"],
                                     r["category"], stxt,
                                     r["created_at"][:10]),
                             tags=(tag,))

        # Apply tag colours
        self.tree.tag_configure("bought", foreground=c["success_fg"])  # green text
        self.tree.tag_configure("even",   background=c["tree_bg"])
        self.tree.tag_configure("odd",    background=c["tree_alt"])    # alternate row

    # -------------------------------------------------------------------------
    def refresh_stats(self):
        """
        METHOD: Dashboard.refresh_stats()
        Updates the four stat card numbers with fresh data from the database.

        CALLED FROM: _build(), _refresh_all()
        CALLS: database.get_dashboard_stats()
        """
        total, bought, pend, cost = database.get_dashboard_stats(self.user_id)
        self.stat_total.config(text=str(total))
        self.stat_bought.config(text=str(bought))
        self.stat_pend.config(text=str(pend))
        # Count distinct categories currently in use
        rows = database.get_grocery_items(self.user_id)
        cats = len(set(r["category"] for r in rows)) if rows else 0
        self.stat_cats.config(text=str(cats))

    # -------------------------------------------------------------------------
    def _refresh_all(self):
        """
        METHOD: Dashboard._refresh_all()
        Convenience method - refreshes both the table AND the stat cards.

        CALLED BY: Refresh button click, _add_item(), _update_item(),
                   _delete_item(), _mark_purchased(), _mark_pending()
        """
        self.refresh_table()
        self.refresh_stats()

    # -------------------------------------------------------------------------
    def _on_row_select(self, _=None):
        """
        METHOD: Dashboard._on_row_select()
        Called automatically when the user clicks a row in the Treeview.
        Reads the item from the database and fills all form fields with its data.
        Also stores the item ID in self.selected_id for Update/Delete to use.

        HOW IT WORKS:
          self.tree.selection() returns the iid of the selected row.
          The iid is the string database ID set during refresh_table().
          int(sel[0]) converts it back to an integer for the DB query.

        CALLED BY: <<TreeviewSelect>> event on self.tree (set in _build_table_panel)
        CALLS: database.get_item_by_id()
        """
        sel = self.tree.selection()   # tuple of selected row iids
        if not sel:
            return

        item_id = int(sel[0])   # convert string iid back to integer DB ID
        row = database.get_item_by_id(item_id, self.user_id)   # verify ownership
        if not row:
            return

        self.selected_id = item_id
        self.v_name.set(row["name"])
        self.v_qty.set(str(row["quantity"]))
        self.v_unit.set(row["unit"])
        self.v_cat.set(row["category"])
        self.v_bought.set(bool(row["purchased"]))
        self.msg_var.set("")

    # -------------------------------------------------------------------------
    def _validate_form(self):
        """Validates form fields. Returns (name, qty, None) on success or (None, None, "error") on failure."""
        name = self.v_name.get().strip()
        if not name:
            return None, None, "Item name is required."
        try:
            qty = float(self.v_qty.get().strip())
            if qty <= 0: raise ValueError
        except ValueError:
            return None, None, "Quantity must be a positive number."
        return name, qty, None

    # -------------------------------------------------------------------------
    def _show_msg(self, text, error=False):
        """
        METHOD: Dashboard._show_msg()
        Shows a feedback message below the form buttons.
        Green text for success, red text for errors.

        PARAMETERS:
            text  - message string to display
            error - True = show in red, False = show in green (default)

        CALLED FROM: _add_item(), _update_item(), _delete_item(),
                     _mark_purchased(), _mark_pending(), _validate_form() callers
        """
        self.msg_var.set(text)
        self.msg_label.config(
            fg=self.c["error_fg"] if error else self.c["success_fg"])

    # -------------------------------------------------------------------------
    def _add_item(self):
        """Called when the Add button is clicked. Validates, saves to DB, refreshes."""
        name, qty, err = self._validate_form()
        if err:
            self._show_msg(err, error=True); return
        database.add_grocery_item(
            self.user_id, name, qty,
            self.v_unit.get(), 0.0,        # price removed; stored as 0
            self.v_cat.get(), self.v_bought.get()
        )
        self._show_msg(f"'{name}' added.")
        self._clear_form()
        self._refresh_all()

    # -------------------------------------------------------------------------
    def _update_item(self):
        """Called when the Update button is clicked. Requires a row to be selected."""
        if not self.selected_id:
            self._show_msg("Select a row first.", error=True); return
        name, qty, err = self._validate_form()
        if err:
            self._show_msg(err, error=True); return
        database.update_grocery_item(
            self.selected_id, self.user_id,
            name, qty, self.v_unit.get(), 0.0,   # price removed; stored as 0
            self.v_cat.get(), self.v_bought.get()
        )
        self._show_msg(f"'{name}' updated.")
        self._refresh_all()

    # -------------------------------------------------------------------------
    def _delete_item(self):
        """
        METHOD: Dashboard._delete_item()
        Called when the Delete button is clicked.
        Shows a confirmation dialog before deleting.
        Requires a row to be selected.

        CALLED BY: "Delete" button
        CALLS: messagebox.askyesno(), database.delete_grocery_item(),
               _show_msg(), _clear_form(), _refresh_all()
        """
        if not self.selected_id:
            self._show_msg("Select a row first.", error=True); return
        name = self.v_name.get().strip() or f"item #{self.selected_id}"

        # Show a Yes/No confirmation dialog before deleting
        # messagebox.askyesno() returns True if user clicks Yes
        if messagebox.askyesno("Confirm Delete",
                               f"Delete '{name}'?", icon="warning"):
            database.delete_grocery_item(self.selected_id, self.user_id)
            self._show_msg(f"'{name}' deleted.")
            self._clear_form()
            self._refresh_all()

    # -------------------------------------------------------------------------
    def _mark_purchased(self):
        """
        METHOD: Dashboard._mark_purchased()
        Called when the Purchased button is clicked.
        Sets the item's purchased flag to True (1) in the database.

        CALLED BY: "Purchased" button
        CALLS: database.mark_purchased(True), _show_msg(), _refresh_all()
        """
        if not self.selected_id:
            self._show_msg("Select a row first.", error=True); return
        database.mark_purchased(self.selected_id, self.user_id, True)
        self.v_bought.set(True)   # update checkbox in the form
        self._show_msg("Marked as purchased.")
        self._refresh_all()

    # -------------------------------------------------------------------------
    def _mark_pending(self):
        """
        METHOD: Dashboard._mark_pending()
        Called when the Pending button is clicked.
        Sets the item's purchased flag to False (0) in the database.

        CALLED BY: "Pending" button
        CALLS: database.mark_purchased(False), _show_msg(), _refresh_all()
        """
        if not self.selected_id:
            self._show_msg("Select a row first.", error=True); return
        database.mark_purchased(self.selected_id, self.user_id, False)
        self.v_bought.set(False)   # update checkbox in the form
        self._show_msg("Marked as pending.")
        self._refresh_all()

    # -------------------------------------------------------------------------
    def _clear_form(self):
        """
        METHOD: Dashboard._clear_form()
        Resets all form fields to their default empty/initial values.
        Also clears self.selected_id so no item is selected.

        CALLED BY: "Clear" button, _add_item(), _delete_item()
        """
        self.v_name.set("")
        self.v_qty.set("")
        self.v_unit.set(UNITS[0])
        self.v_cat.set(CATEGORIES[0])
        self.v_bought.set(False)
        self.selected_id = None
        self.msg_var.set("")

    # -------------------------------------------------------------------------
    def _export_csv(self):
        """
        METHOD: Dashboard._export_csv()
        Called when the Export to CSV button is clicked.
        Opens a file save dialog, then writes all grocery items to a CSV file.

        CALLED BY: "Export to CSV" button
        CALLS: filedialog.asksaveasfilename(), database.export_items_to_csv(),
               messagebox.showinfo() or messagebox.showerror()
        """
        # Ask the user where to save the file
        fp = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv")],
            title="Export Grocery List",
            initialfile=f"{self.username}_groceries.csv")
        if not fp:
            return   # user cancelled the dialog

        try:
            database.export_items_to_csv(self.user_id, fp)   # write the file
            messagebox.showinfo("Export Successful", f"Saved to:\n{fp}")
        except Exception as exc:
            messagebox.showerror("Export Failed", str(exc))

    # -------------------------------------------------------------------------
    def _toggle_theme(self):
        """
        METHOD: Dashboard._toggle_theme()
        Called when the Dark Mode / Light Mode button is clicked.
        Switches theme, saves preference to database, rebuilds the dashboard.

        CALLED BY: theme toggle button in _build_header()
        CALLS: database.update_theme_preference(), _rebuild_dashboard()
        """
        # Switch between "light" and "dark"
        self.theme = "dark" if self.theme == "light" else "light"
        self.c = THEMES[self.theme]   # update active colour palette
        database.update_theme_preference(self.user_id, self.theme)  # save to DB
        self._rebuild_dashboard()

    # -------------------------------------------------------------------------
    def _rebuild_dashboard(self):
        """
        METHOD: Dashboard._rebuild_dashboard()
        Destroys all widgets and rebuilds the entire dashboard with the new theme.
        Preserves all form data and the selected row before rebuilding,
        then restores them after.

        WHY REBUILD INSTEAD OF JUST CHANGING COLOURS?
          Tkinter widgets don't automatically re-read colour variables.
          The only clean way to apply a new theme to all widgets is to
          destroy them all and create them fresh.

        CALLED FROM: _toggle_theme()
        """
        # Save current state before destroying widgets
        snap = {
            "name":   self.v_name.get(),
            "qty":    self.v_qty.get(),
            "unit":   self.v_unit.get(),
            "cat":    self.v_cat.get(),
            "bought": self.v_bought.get(),
            "search": self.search_var.get() if hasattr(self, "search_var") else "",
            "fcat":   self.filter_cat.get() if hasattr(self, "filter_cat") else "All",
            "fstat":  self.filter_status.get() if hasattr(self, "filter_status") else "All",
            "selid":  self.selected_id,
        }

        # Destroy all child widgets
        for w in self.winfo_children():
            w.destroy()

        # Rebuild everything with the new theme colours
        self._build()

        # Restore saved state
        self.v_name.set(snap["name"])
        self.v_qty.set(snap["qty"])
        self.v_unit.set(snap["unit"])
        self.v_cat.set(snap["cat"])
        self.v_bought.set(snap["bought"])
        self.search_var.set(snap["search"])
        self.filter_cat.set(snap["fcat"])
        self.filter_status.set(snap["fstat"])
        self.selected_id = snap["selid"]
        self.refresh_table()
        self.refresh_stats()

        # Re-select the previously selected row in the table
        if snap["selid"] and str(snap["selid"]) in self.tree.get_children():
            self.tree.selection_set(str(snap["selid"]))
            self.tree.see(str(snap["selid"]))   # scroll to make it visible

    # -------------------------------------------------------------------------
    def _logout(self):
        """
        METHOD: Dashboard._logout()
        Called when the Logout button is clicked.
        Shows a confirmation dialog, then destroys the dashboard
        and calls on_logout() to return to the login screen.

        CALLED BY: Logout button in _build_header()
        CALLS: messagebox.askyesno(), self.destroy(), self.on_logout()
        """
        if messagebox.askyesno("Logout", "Are you sure you want to log out?"):
            for w in self.winfo_children():
                w.destroy()
            self.destroy()        # remove dashboard from window
            self.on_logout()      # calls App._show_login() -> LoginScreen appears


# =============================================================================
# CLASS: App
# PURPOSE:
#   The root application controller.
#   Creates the main Tk window, initialises the database, and manages
#   transitions between LoginScreen and Dashboard.
#
# THIS IS WHERE THE PROGRAM STARTS.
# The block at the bottom: if __name__ == "__main__": App()
# tells Python to create an App object when this file is run directly.
# =============================================================================
class App:
    """Root controller - manages screen transitions."""

    def __init__(self):
        """
        CONSTRUCTOR: App.__init__()
        The very first thing that runs when the application starts.

        STEP BY STEP:
          1. database.initialise_database() - creates DB tables if not present
          2. tk.Tk() - creates the main OS window
          3. window title, size, minimum size, background colour
          4. _show_login() - displays the LoginScreen
          5. root.mainloop() - starts the Tkinter event loop
                               (keeps the window open and responds to clicks)

        CALLED FROM: if __name__ == "__main__": App()  (at the bottom of this file)
        CALLS: database.initialise_database(), tk.Tk(), self._show_login()
        """
        # Create tables in the database (safe to call every time - uses IF NOT EXISTS)
        database.initialise_database()

        # Create the main application window
        self.root = tk.Tk()
        self.root.title(APP_TITLE)          # title bar text
        self.root.geometry("1150x720")      # initial window size: 1150px wide, 720px tall
        self.root.minsize(960, 600)         # minimum window size (can't shrink smaller)
        self.root.configure(bg="#F0F2F5")   # window background colour

        # Show the login screen
        self._show_login()

        # Start the Tkinter event loop
        # mainloop() keeps the window open and waits for user actions.
        # It only returns when the window is closed.
        self.root.mainloop()

    def _show_login(self):
        """
        METHOD: App._show_login()
        Creates and shows the LoginScreen.
        Passes App._show_dashboard as the callback for when login succeeds.

        CALLED FROM: __init__() at startup, Dashboard._logout() after logout.
        CALLS: LoginScreen()
        """
        # Create LoginScreen - it packs itself into self.root automatically
        LoginScreen(self.root, on_login_success=self._show_dashboard)

    def _show_dashboard(self, user_row):
        """
        METHOD: App._show_dashboard()
        Called when LoginScreen._do_login() succeeds.
        Creates the Dashboard with the logged-in user's data.

        PARAMETERS:
            user_row - dict with logged-in user's database row
                       {"id", "username", "theme_preference", ...}

        CALLED FROM: LoginScreen._do_login() via self.on_login_success(result)
        CALLS: Dashboard()
        """
        # Create Dashboard - it packs itself into self.root automatically
        Dashboard(self.root, user_row, on_logout=self._show_login)


# =============================================================================
# ENTRY POINT
# This block only runs when you execute: python main.py
# It does NOT run when another file imports main.py.
# __name__ is "__main__" only for the file being run directly.
# =============================================================================
if __name__ == "__main__":
    App()   # create App object, which starts the whole application
