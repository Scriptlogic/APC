# Program 12: Transactions Module

def issue_book(books, book_id):
    if book_id in books and books[book_id]["available"]:
        books[book_id]["available"] = False
        return "Book Issued"
    return "Book Not Available"

def return_book(books, book_id):
    if book_id in books:
        books[book_id]["available"] = True
        return "Book Returned"
    return "Book Not Found"
