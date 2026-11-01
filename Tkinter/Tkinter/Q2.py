import tkinter as tk
from tkinter import filedialog, messagebox

root = tk.Tk()
root.title("My Notepad")
root.geometry("800x550")

current_file = None

# Text area
text_area = tk.Text(
    root, font=("Consolas", 12),
    undo=True, wrap="word"
)
text_area.pack(fill="both", expand=True)

# Scrollbar
scrollbar = tk.Scrollbar(text_area, command=text_area.yview)
scrollbar.pack(side="right", fill="y")
text_area.config(yscrollcommand=scrollbar.set)

def new_file():
    global current_file
    if text_area.get("1.0", "end-1c"):
        answer = messagebox.askyesnocancel(
            "My Notepad", "Save current file?"
        )
        if answer is None:
            return
        if answer and not save_file():
            return

    text_area.delete("1.0", "end")
    current_file = None
    root.title("Untitled - My Notepad")

def open_file():
    global current_file
    file = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"),
                   ("All Files", "*.*")]
    )
    if file:
        try:
            with open(file, "r", encoding="utf-8") as f:
                content = f.read()
            text_area.delete("1.0", "end")
            text_area.insert("1.0", content)
            current_file = file
            root.title(file + " - My Notepad")
        except Exception as e:
            messagebox.showerror("Error", str(e))

def save_file():
    global current_file
    if current_file is None:
        return save_as()
    try:
        with open(current_file, "w", encoding="utf-8") as f:
            f.write(text_area.get("1.0", "end-1c"))
        return True
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return False

def save_as():
    global current_file
    file = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"),
                   ("All Files", "*.*")]
    )
    if not file:
        return False
    current_file = file
    if save_file():
        root.title(file + " - My Notepad")
        return True
    current_file = None
    return False

def select_all(event=None):
    text_area.tag_add("sel", "1.0", "end-1c")
    return "break"

def show_about():
    messagebox.showinfo(
        "About My Notepad",
        "My Notepad\nCreated using Python and Tkinter"
    )

# Menu bar
menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file, accelerator="Ctrl+N")
file_menu.add_command(label="Open", command=open_file, accelerator="Ctrl+O")
file_menu.add_command(label="Save", command=save_file, accelerator="Ctrl+S")
file_menu.add_command(label="Save As", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)
menu_bar.add_cascade(label="File", menu=file_menu)

edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Undo", command=lambda: text_area.edit_undo())
edit_menu.add_command(label="Redo", command=lambda: text_area.edit_redo())
edit_menu.add_separator()
edit_menu.add_command(label="Cut", command=lambda: text_area.event_generate("<<Cut>>"))
edit_menu.add_command(label="Copy", command=lambda: text_area.event_generate("<<Copy>>"))
edit_menu.add_command(label="Paste", command=lambda: text_area.event_generate("<<Paste>>"))
edit_menu.add_command(label="Select All", command=select_all)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=show_about)
menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)

# Keyboard shortcuts
root.bind("<Control-n>", lambda event: new_file())
root.bind("<Control-o>", lambda event: open_file())
root.bind("<Control-s>", lambda event: save_file())
root.bind("<Control-a>", select_all)

# Status bar
status = tk.Label(
    root, text="Ready", anchor="w",
    relief="sunken"
)
status.pack(side="bottom", fill="x")

root.mainloop()