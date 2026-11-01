import tkinter as tk
from tkinter import messagebox
import re

root = tk.Tk()
root.title("Registration Form")
root.geometry("750x700")
root.configure(bg="lightblue")

tk.Label(
    root, text="REGISTRATION FORM",
    font=("Arial", 18, "bold"),
    bg="lightblue"
).pack(pady=10)

form = tk.Frame(root, bg="lightblue")
form.pack()

def add_label(text, row):
    tk.Label(
        form, text=text, font=("Arial", 11),
        bg="lightblue"
    ).grid(row=row, column=0, sticky="w", padx=10, pady=5)

# Name fields
add_label("First Name:", 0)
first_name = tk.Entry(form, width=30)
first_name.grid(row=0, column=1, pady=5)

add_label("Middle Name:", 1)
middle_name = tk.Entry(form, width=30)
middle_name.grid(row=1, column=1, pady=5)

add_label("Last Name:", 2)
last_name = tk.Entry(form, width=30)
last_name.grid(row=2, column=1, pady=5)

# Mobile number with India code
add_label("Mobile Number:", 3)
phone_frame = tk.Frame(form, bg="lightblue")
phone_frame.grid(row=3, column=1, sticky="w")

tk.Label(
    phone_frame, text="+91",
    font=("Arial", 11, "bold"), bg="lightblue"
).pack(side="left")

phone = tk.Entry(phone_frame, width=23)
phone.pack(side="left", padx=5)

# State listbox
add_label("State:", 4)
state_list = tk.Listbox(form, height=3, exportselection=False)
state_list.grid(row=4, column=1, sticky="w", pady=5)

states = ["Maharashtra", "Karnataka", "Goa"]
for state in states:
    state_list.insert(tk.END, state)

# District data
district_data = {
    "Maharashtra": ["Kolhapur", "Pune", "Mumbai"],
    "Karnataka": ["Belagavi", "Bengaluru", "Dharwad"],
    "Goa": ["North Goa", "South Goa"]
}

# District listbox
add_label("District:", 5)
district_list = tk.Listbox(form, height=3, exportselection=False)
district_list.grid(row=5, column=1, sticky="w", pady=5)

# Taluka data
taluka_data = {
    "Kolhapur": ["Karveer", "Panhala", "Kagal"],
    "Pune": ["Haveli", "Mulshi", "Junnar"],
    "Mumbai": ["Andheri", "Borivali", "Kurla"],
    "Belagavi": ["Belagavi", "Khanapur", "Gokak"],
    "Bengaluru": ["Anekal", "Bengaluru North"],
    "Dharwad": ["Dharwad", "Hubballi"],
    "North Goa": ["Bardez", "Bicholim"],
    "South Goa": ["Salcete", "Mormugao"]
}

# Taluka listbox
add_label("Taluka:", 6)
taluka_list = tk.Listbox(form, height=3, exportselection=False)
taluka_list.grid(row=6, column=1, sticky="w", pady=5)

def update_districts(event=None):
    district_list.delete(0, tk.END)
    taluka_list.delete(0, tk.END)

    selected = state_list.curselection()
    if selected:
        state = state_list.get(selected[0])
        for district in district_data[state]:
            district_list.insert(tk.END, district)

def update_talukas(event=None):
    taluka_list.delete(0, tk.END)

    selected = district_list.curselection()
    if selected:
        district = district_list.get(selected[0])
        for taluka in taluka_data.get(district, []):
            taluka_list.insert(tk.END, taluka)

state_list.bind("<<ListboxSelect>>", update_districts)
district_list.bind("<<ListboxSelect>>", update_talukas)

# Address field
add_label("Address:", 7)
address = tk.Text(form, width=30, height=3)
address.grid(row=7, column=1, pady=5)

# Submit and validate
def submit_form():
    first = first_name.get().strip()
    middle = middle_name.get().strip()
    last = last_name.get().strip()
    mobile = phone.get().strip()
    addr = address.get("1.0", tk.END).strip()

    # Validate names
    if not re.fullmatch(r"[A-Za-z]+", first):
        messagebox.showerror(
            "Error", "First name must contain letters A-Z only."
        )
        first_name.focus_set()
        return

    if not re.fullmatch(r"[A-Za-z]+", middle):
        messagebox.showerror(
            "Error", "Middle name must contain letters A-Z only."
        )
        middle_name.focus_set()
        return

    if not re.fullmatch(r"[A-Za-z]+", last):
        messagebox.showerror(
            "Error", "Last name must contain letters A-Z only."
        )
        last_name.focus_set()
        return

    # Validate Indian mobile number
    if not re.fullmatch(r"[6-9][0-9]{9}", mobile):
        messagebox.showerror(
            "Error",
            "Enter a valid 10-digit Indian mobile number."
        )
        phone.focus_set()
        return

    # Validate state, district and taluka selection
    if not state_list.curselection():
        messagebox.showerror("Error", "Please select a state.")
        return

    if not district_list.curselection():
        messagebox.showerror("Error", "Please select a district.")
        return

    if not taluka_list.curselection():
        messagebox.showerror("Error", "Please select a taluka.")
        return

    # Validate address and six-digit Indian PIN code
    if not addr:
        messagebox.showerror("Error", "Please enter your address.")
        address.focus_set()
        return

    pin_codes = re.findall(r"(?<!\d)[1-9][0-9]{5}(?!\d)", addr)

    if not pin_codes:
        messagebox.showerror(
            "Error",
            "Address must contain a valid 6-digit Indian PIN code."
        )
        address.focus_set()
        return

    state = state_list.get(state_list.curselection()[0])
    district = district_list.get(district_list.curselection()[0])
    taluka = taluka_list.get(taluka_list.curselection()[0])

    messagebox.showinfo(
        "Success",
        f"Registration Successful!\n\n"
        f"Name: {first} {middle} {last}\n"
        f"Mobile: +91 {mobile}\n"
        f"State: {state}\n"
        f"District: {district}\n"
        f"Taluka: {taluka}\n"
        f"Address: {addr}"
    )

    # Clear the form after successful submission
    first_name.delete(0, tk.END)
    middle_name.delete(0, tk.END)
    last_name.delete(0, tk.END)
    phone.delete(0, tk.END)
    address.delete("1.0", tk.END)

    state_list.selection_clear(0, tk.END)
    district_list.delete(0, tk.END)
    taluka_list.delete(0, tk.END)

tk.Button(
    root, text="Submit", command=submit_form,
    font=("Arial", 12, "bold"),
    bg="green", fg="white", width=15
).pack(pady=15)

root.mainloop()