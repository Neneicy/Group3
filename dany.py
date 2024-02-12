from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author, isbn=None, quantity=1, available= 'yes'):
        self.title = title
        self.author = author
        self.available = available
        self.isbn = isbn if isbn is not None else self.generate_isbn()
        self.quantity = quantity
        self.borrow_history = []

    def generate_isbn(self):
        # This method generates a unique ISBN ID starting from 1000000
        Book.isbn_counter = getattr(Book, 'isbn_counter', 1000000) + 1
        return str(Book.isbn_counter)

    def borrow(self, user, borrow_date):
        if self.available and self.quantity > 0:
            self.available = False
            self.quantity -= 1
            self.borrow_history.append({'user': user.name, 'date': borrow_date})
            return True
        else:
            return False

    def return_book(self, return_date):
        if not self.available:
            self.available = True
            self.quantity += 1
            return_history = self.borrow_history.pop()
            return_history['return_date'] = return_date
            return return_history
        else:
            return None

    def __str__(self):
        return f"ISBN: {self.isbn} - {self.title} by {self.author} - Quantity: {self.quantity} - Available: {self.available}"

class User:
    def __init__(self, name):
        self.name = name

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        if self.books:
            book_number = 1000000  # Start book number from 1
            print("Available Books:")
            for book in self.books:
                if book.available:
                    print(f"{book_number}, {book}")
                    book_number += 1  # Increment book number for each available book
            else:
                print(f"'{book.title}' This book is not available in the library.")

    def borrow_book(self, isbn, user):
        book = self.search_book(isbn)
        if book:
            borrow_date = datetime.now().strftime("%Y-%m-%d")
            if book.borrow(user, borrow_date):
                print(f"-------------Thank you for borrowing------------ '{book.title}'.")
            else:
                print(f"'{book.title}' is not available.")
        else:
            print(f"Book with ISBN {isbn} not found.")

    def return_book(self, isbn):
        book = self.search_book(isbn)
        if book:
            return_date = datetime.now().strftime("%Y-%m-%d")
            return_history = book.return_book(return_date)
            if return_history:
                print("")
                print(f"-------------Thank you for returning------------ '{book.title}'.")
                print("")
                print(f"Borrowed by: {return_history['user']}")
                print(f"Borrowed on: {return_history['date']}")
                print(f"Returned on: {return_history['return_date']}")
            else:
                print(f"'{book.title}' is already available in the library.")
        else:
            print(f"Book with ISBN {isbn} not found.")

    def search_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

def main():
    system_library = Library()

    books = [
        Book("Computers under attack intruders worms and viruses 005.8 D411 1990", "DENNING", quantity=5),
        Book("Artificial Intelligence A modern approach 006.3 R967 2003", "RUSSELL NORVIG", quantity=3),
        Book("Programming Macromedia Flash 006.696 P413" , "Robert Penner's", quantity=2),
        Book("Electronic Communication 621.3 SH561 1991" , "SHRADER", quantity=3),
        Book("ELECTRONIC PRINCIPLE'S 621.3515 M262 1999" , "MALVINO", quantity=1),
        Book("Electronic Troubleshooting 621.381 M434 1992" , "matsuda", quantity=1),
        Book("Grob's Basic Electronics 621.381 SCH387 2007" , "aicy" , quantity=2),
        Book("Troubleshooting and repairing PCs 621.3916 H811 1997" , "hordesk!", quantity=2),
        Book("Upgrading and Repairing PCS sixth edition 621.3916 M946 1996" , "daniella" , quantity=1),
        Book("Digital Design 621.395 M285 1991" , "MANO", quantity=3),
        Book("Word2000 Microsoft Office Application 652.553 69 R896 1999" , "running Microsoft", quantity=2),
        Book("Understanding Psychology 150 F312 2005" , "Robert S.  Feldman", quantity=1),
        Book("Sociology 301 SCH294 2005 ", "Richard T. Schaefer", quantity=1),
        Book("Economics 330 SL631 1996" , "Slavin", quantity=1),
        Book("Microeconomics 338.5 P648 2001" , "PINDYCK RUBINFELD", quantity=3),
        Book("Price theory and applications 338.52 P281 1998 " , "pashigian", quantity=1),
        Book("Macroeconomics 339 D713 2001" , "Dornbusch Fisher startz",quantity=2),
        Book("Essential of Investment 332.6 B667 2001" , "Bodie Kane Marcus" ,quantity=3),
        Book("Macroeconomics 339 D713 2001" , "Dornbusch Fisher startz", quantity=1),
        # ... (add other books with quantity)
    ]

    for book in books:
        system_library.add_book(book)

    while True:
        print("""
█   █ ██▀ █   ▄▀▀ ▄▀▄ █▄ ▄█ ██▀   ▀█▀ ▄▀▄   ▄▀▄ ▄▀▀ █   ▄▀▀   █   █ ██▄ █▀▄ ▄▀▄ █▀▄ ▀▄▀   █▄ ▄█ ▄▀▄ █▄ █ ▄▀▄ ▄▀  ██▀ █▄ ▄█ ██▀ █▄ █ ▀█▀
▀▄▀▄▀ █▄▄ █▄▄ ▀▄▄ ▀▄▀ █ ▀ █ █▄▄    █  ▀▄▀   █▀█ ▀▄▄ █▄▄ ▀▄▄   █▄▄ █ █▄█ █▀▄ █▀█ █▀▄  █    █ ▀ █ █▀█ █ ▀█ █▀█ ▀▄█ █▄▄ █ ▀ █ █▄▄ █ ▀█  █

""")
        print("""
            _______
            /      //   READ CAREFULLY THE INSTRUCTIONS.
            /      //   THANK YOU!
            /______//   (1) Display Available Books, (2) Borrow a Book, (3) Return a Book, (4) Exit
            (______(/
            """)
        print("")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            system_library.display_books()
        elif choice == '2':
            isbn = input("Enter the ISBN of the book you want to borrow: ")
            user_name = input("Enter your name: ")
            user = User(user_name)
            system_library.borrow_book(isbn, user)
        elif choice == '3':
            isbn = input("Enter the ISBN of the book you want to return: ")
            system_library.return_book(isbn)
        elif choice == '4':
            print("Thank you for using our Library Management System. GOODBYE!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
