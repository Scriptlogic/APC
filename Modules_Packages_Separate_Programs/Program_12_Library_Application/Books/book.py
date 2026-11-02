# Program 12: Books Module

books = {}

def add_book(book_id, title):
    books[book_id] = {"title": title, "available": True}

def display_books():
    return books
