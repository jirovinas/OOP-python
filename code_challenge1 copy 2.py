class Student:
    def __init__(self, name, idno, course):
        self.name = name
        self.idno = idno
        self.course = course

    def borrow_book(self, book):
        pass

    def return_book(self, book):
        pass

class Librarian:
    def __init__(self, name, idno):
        self.name = name
        self.idno = idno

    def insert_book(self, title, author, publisher, no_of_copies):
        return Book(title, author, publisher, no_of_copies)

    def remove_book(self, book_name):
        for book in library:
            if book.title == book_name:
                library.remove(book)
                print(f"\nThe book {book.title} has been removed")
        else:
            print(f"\nThe book {book.title} is not in the box")

class Book:
    def __init__(self, title, author, publisher, no_of_copies):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.no_of_copies = no_of_copies

    def check_availability(self):
        if self.no_of_copies > 0:
            return f"\nThe book '{self.title}' is available."
        else:
            return f"\nThe book '{self.title}' is not available."
def back_to_menu():
    print("Going back to the main menu...")
    return False

book_1 = Book('jiro', 'j', 'j', 3)

library = [book_1]

goku_the_librarian = Librarian("Goku",123)
jiro_the_student = Student("jiro",123,"BSIT")
login = False
user_type = ''


while True:
    if login == True and user_type == 'Librarian':
        

        print("""
            [1] - Add Book
            [2] - Remove Book
            [3] - Check Available Books
            [4] - Back
            [5] - Exit
            """)

        choice = eval(input("Enter your choice: "))

        if choice == 1:
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            publisher = input("Enter the publisher of the book: ")
            no_of_copies = eval(input("Enter the number of copies: "))

            book = Book(title, author, publisher, no_of_copies)
            library.append(book)
            print(book.title, "Has been added")

        elif choice == 2:
            title = input("Enter the title of the book to remove: ")
            for book in library:
                if book.title == title:
                    goku_the_librarian.remove_book(book.title)
                    print("Remove Successfully")
                    

        elif choice == 3:
            title = input("Enter the title of the book to check availability: ")
            for book in library:
                if book.title == title:
                    print(book.check_availability())
                    break
            else:
                print(f"\nThe book '{title}' is not available.")

        elif choice == 4:
            login = back_to_menu()
        elif choice == 5:
            print("Exit")
            break
        
    
    elif login == True and user_type == 'Student':
        print('Login as Student')
        print("""
            [1] - Borrow Book
            [2] - Return Book
            [3] - Check Available Books
            [4] - Back
            [5] - Exit
            """)

        choice = eval(input("Enter your choice: "))
        if choice == 1:
            title = input("Enter the title of the book to borrow: ")
            book_to_borrow = next((book for book in library if book.title == title), None)
            if book_to_borrow:
                jiro_the_student.borrow_book(book_to_borrow)
                library.remove(book_to_borrow)
            else:
                print(f"The book '{title}' is not available.")

        elif choice == 2:
            title = input("Enter the title of the book to return: ")
            book_to_return = next((book for book in library if book.title == title), None)
            if book_to_return:
                jiro_the_student.return_book(book_to_return)
            else:
                print(f"The book '{title}' is not available for returning.")
                    
        elif choice == 3:
            title = input("Enter the title of the book to check availability: ")
            for book in library:
                if book.title == title:
                    print(book.check_availability())
                    break
            else:
                print(f"The book '{title}' is not available.")
        elif choice == 4:
            login = back_to_menu()

        elif choice == 5:
            print("Exit")
            break
    

    elif login == False:
        print('Welcome to the Library')
        print("""
            [1] - Student
            [2] - Librarian
            [3] - Logout
            """)

        choice  = eval(input("Enter your choice: "))

        if choice == 1:
            print('\nLogin as Student')
            print('Please Enter Student name, id number and course\n')
            name = str(input('Enter name > '))
            id_no = int(input('Enter id number > '))
            course = str(input('Enter course > '))

            if jiro_the_student.name == name and jiro_the_student.idno == id_no and jiro_the_student.course == course:
                user_type = 'Student'
                login = True
                print("Login Successfully", jiro_the_student.name)
                continue

        elif choice == 2:
            print('\nLogin as Librarian')
            print('Please Enter librarian name and id number\n')
            name = str(input('Enter name > '))
            id_no = int(input('Enter id number > '))
            
            if goku_the_librarian.name == name and goku_the_librarian.idno == id_no:
                user_type = 'Librarian'
                login = True
                print('Login Successfully ', goku_the_librarian.name)
                continue

        elif choice == 3:
            print("Exit")
            break
