books = ["Python Basics", "Data Structures", "Web Development"]
books.append("Machine Learning")
search_title = "Python Basics"
if search_title in books:
    print(f"'{search_title}' is available in the library.")
books.remove("Web Development")
print("All Books in Library:", books)
print("Total Books:", len(books))