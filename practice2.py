class Book:
    def __init__(self, title, author)  -> None:
        self.title = title 
        self.author = author
        self.available = True

    def check_out(self):
        self.available = False
    def check_in(self):
        self.available = True

class Member:
    def __init__(self, member_id, name) -> None:
        self.member_id = member_id
        self.name = name
        self.books_borrowed =[]

    def borrow_book(self, book):
        if book.available == True:
            self.books_borrowed.append(book)
            book.check_out()
            print(f"The book {book.title} has been borrowed")
        else:
            print("The book is not available")

    def return_book(self, book):
        if book.available == False:
            self.books_borrowed.remove(book)
            book.check_in()
            print(f"The book {book.title} has been returned")
        else:
            print("The book has been didn't return")

class Library:
    def __init__(self) -> None:
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

# Create instances of books, members, and a library
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

member1 = Member("M001", "Alice")
member2 = Member("M002", "Bob")

library = Library()

# Add books to the library
library.add_book(book1)
library.add_book(book2)

# Add members to the library
library.add_member(member1)
library.add_member(member2)

# Allow members to borrow and return books
member1.borrow_book(book1)
member2.borrow_book(book2)
member2.return_book(book2)

