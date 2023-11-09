class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def check_available(self):
        return self.copies
    
    def borrow(self):
        if self.copies > 0:
            self.copies -=1
            return f"Successfully borrowed {self.title} by author {self.author}"
        else:
            return f"Sorry, {self.title} is current unavailable"
        
    def return_book(self):
        self.copies += 1
        return f"Returned {self.title} by {self.author}"
        
class Librarian:
    def __init__(self):
        self.books = []
        
    def add_book(self, title, author, copies=1):
        for book in self.books:
            if book.title == title and book.author == author:
                book.copies += copies
                return f"Added {copies} copies of {title} by {author}"
            new_book = Book(title, author, copies)
            self.books.append(new_book)
            return f"Added {title}by {author} with {copies} copies"
        
    def remove_book(self, title, author):
        for book in self.books:
            if book.title == title and book.author == author:
                self.remove_book(book)
                return f"The book {title} by {author} has been remove"
            return f"{title} by {author} not found"
    def list_books(self):
        for book in self.books:
            print(book)
class Student:
    def __init__(self,name):
        self.name = name

    def borrow_book(self, book):
        return book.borrow()
    
    def return_book(self, book):
        return book.return_book()
    
if __name__ == "__main__":
    librarian = Librarian()

    librarian.add_book("Python Book", "Jiro", 10)
    librarian.add_book("Math Book", "Miko", 10)
    librarian.add_book("PE Book", "Vinas", 10)
    

    student1 = Student("Jiro")
    student2 = Student("Miko")

    print("Books available in he library:")
    librarian.list_books()

    book = Book("", "", 4)

    print("\nJiro borrows a book:")
    print(len(librarian.books))
    print(student1.borrow_book(book))

    print("\nBooks available in the library:")
    librarian.list_books()

    print("\nJiro returns the book:")
    print(student1.return_book(book))

    print("\nBooks available in the library:")
    librarian.list_books()

    print("\nMiko borrows book:")
    print(student2.borrow_book(book))

    print("\nBooks available in the library:")
    librarian.list_books()

    print("\nLibrarian removes a book:")
    print(librarian.remove_book("Python Book", "Jiro"))

    print("\nBooks available in the library:")
    librarian.list_books()