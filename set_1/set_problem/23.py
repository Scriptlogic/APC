# 23. Check requested books availability

available_books = {
    "Python",
    "Java",
    "C Programming",
    "DBMS",
    "Operating System"
}

requested_books = {
    "Python",
    "DBMS",
    "HTML",
    "Java"
}

available_requested = available_books & requested_books

print("Requested books that are available:")
print(available_requested)