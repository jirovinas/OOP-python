class Library:
    def __init__(self, title, author, publication, copies):
        self.book_title = title
        self.book_author = author
        self.book_publication = publication
        self.no_copies = copies
        self.available_books = copies  # Changed 'title_list' to 'copies'

class Students:
    def __init__(self, stud_name, stud_id, stud_course):
        self.name = stud_name
        self.id = stud_id
        self.course = stud_course

class Librarian:
    def __init__(self, name, id):
        self.name = name  # Changed 'name_' to 'name'
        self.id = id  # Changed 'id_' to 'id'
        self.book_list = []  # Added 'book_list' to keep track of available books

    def borrow(self, name, id, course):
        book = self.checkAvailable()
        if book:
            self.book_list.remove(book)
            print(f'{book.book_title} has been borrowed by {name}.')
        else:
            print("No available books to borrow.")

    def checkAvailable(self):
        if self.book_list:
            print("Available books:")
            for book in self.book_list:
                print(f"{book.book_title} by {book.book_author}")
            return self.book_list[0]  # Return the first available book for borrowing
        else:
            print("No available books.")
            return None

    def returnBook(self, stud_id):
        # You can add the book back to the book list when the student returns it
        pass

    def howManyAvailable(self):
        return len(self.book_list)

def run():
    print("Welcome to the Library Management System!")

    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    publication = input("Enter the publication information: ")
    copies = int(input("Enter the total number of copies: "))

    my_library = Library(title, author, publication, copies)

    librarian = Librarian("Librarian Name", "Librarian ID")  # Create a librarian instance

    while True:
        print("\nOptions:")
        print("1. Add a book")
        print("2. Borrow a book")
        print("3. Check available books")
        print("4. Return a book")
        print("5. Check how many copies are available")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            book_title = input("Enter the title of the book: ")
            book_author = input("Enter the author of the book: ")
            book_publication = input("Enter the publication information: ")
            no_copies = int(input("Enter the total number of copies: "))
            new_book = Library(book_title, book_author, book_publication, no_copies)
            librarian.book_list.append(new_book)  # Add the book to the librarian's book list
            print("\nBook added successfully!")

        elif choice == '2':
            student_name = input("Enter student name: ")
            student_ID = int(input("Enter student ID: "))
            student_course = input("Enter student course: ")
            librarian.borrow(student_name, student_ID, student_course)

        elif choice == '3':
            librarian.checkAvailable()

        elif choice == '4':
            student_ID = int(input("Enter student ID: "))
            librarian.returnBook(student_ID)

        elif choice == '5':
            available_copies = librarian.howManyAvailable()
            print(f"Available copies: {available_copies}")

        elif choice == '6':
            print("Exiting the Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

run()