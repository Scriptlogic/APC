# Program 12: Library Application Main Program

from Books.book import add_book, display_books, books
from Members.member import add_member, display_members
from Transactions.transaction import issue_book, return_book

add_book("B101", "Python Programming")
add_member("M101", "Amit")

print("Books =", display_books())
print("Members =", display_members())
print(issue_book(books, "B101"))
print(return_book(books, "B101"))
