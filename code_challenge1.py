
from dbm.ndbm import library


class Librarian:
    def __init__(self, name, idno):
        self.name = name
        self.idno = idno

    def insert_books(self, book, box):
        box.append(book)
        print(f"The book {book.title} has been added")

    def remove_books(self, book, box):
        if book in box:
            box.remove(book)
            print(f"The book {book.title} has been removed")
        else:
            print(f"The book {book.title} is not in the box")

class Books:
    def __init__(self, title, author, publisher, no_of_copier, ):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.no_of_copier = no_of_copier
        self.is_available = True

    def check_out(self):
        if self.is_available:
            self.is_available = False
            print(f"The book {self.title} has been checked out")
        else:
            print(f"The book {self.title} is not available")

    def check_in(self):
        if not self.is_available:
            self.is_available = True
            print(f"The book {self.title} has been checked in") 
        else:
            print(f"The book {self.title} is already available") 

class Student:
    def __init__(self, name, idno, course):
        self.name = name
        self.idno = idno
        self.course = course

    def borrow_book(self, book):
        return book.check_out()
    def return_book(self, book):
        return book.check_in()

tuloy = True
library_box = []
while tuloy == True:
    print("1 - Add book")
    print("2 - remove book")
    print("3 - Borrow book")
    print("4 - Return book")
    print("5 - exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter the book title: ")
        author = input("Enter the author: ")
        publisher = input("Enter the publisher: ")
        no_of_copier = input("Enter the no_of_copier: ")
        new_book = Book(title, author, publisher)
        librarian = Librarian("L001", "Emma")
        print(librarian.add_book(new_book, library_catalog))