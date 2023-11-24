import json
from datetime import datetime, timedelta
from typing import Optional

class Book:
    def __init__(self, title, author, genre, language, year, max_loan_days=14):
        self.title = title
        self.author = author
        self.genre = genre
        self.language = language
        self.year = year
        self.max_loan_days = max_loan_days
        self.available = True
        self.loan_history = []

    def take(self):
        if self.available:
            self.available = False
            return True
        else:
            print(f"The book '{self.title}' is not available for loan.")
            return False

    def return_book(self):
        if not self.available:
            self.available = True
            return True
        else:
            print(f"The book '{self.title}' is not checked out.")
            return False

class Customer:
    class Customer:
        def __init__(self, full_name, age, town):
            self.full_name = full_name
            self.age = age
            self.town = town
            self.loaned_books = []
            self.ordered_books = []
            self.customer_history = []

        def show_info(self):
            print(f"Full Name: {self.full_name}, Age: {self.age}, Town: {self.town}")
            print(f"Loaned Books: {[book.title for book in self.loaned_books]}")
            print(f"Ordered Books: {[book.title for book in self.ordered_books]}")


class Library:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.books = []
        self.customers = []
        self.load_books_from_file("books.txt")
        self.create_default_customers_from_json("customers.json")

    def create_default_customers_from_json(self, file_path: Optional[str] = "default_customers.json"):
        try:
            with open(file_path, 'r') as file:
                default_customers_data = json.load(file)

                default_customers = [
                    Customer(
                        full_name=data["full_name"],
                        age=data["age"],
                        town=data["town"]
                    )
                    for data in default_customers_data
                ]

                self.customers.extend(default_customers)
                print(f"Default customers loaded successfully from {file_path}.")
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
        except Exception as e:
            print(f"Error loading default customers: {str(e)}")

    def add_book(self, title, author, genre, language, year):
        book = Book(title, author, genre, language, year)
        self.books.append(book)

    def load_books_from_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    title, author, year, genre, language = map(str.strip, line.split(','))
                    self.add_book(title, author, genre, language, int(year))
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")

    def display_books(self):
        for book in self.books:
            availability = "Available" if book.available else "Not Available"
            print(f"Title: {book.title}, Author: {book.author}, Year: {book.year}, Genre: {book.genre}, Language: {book.language}, Availability: {availability}")

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def loan_book(self, customer, title):
        book = self.find_book(title)
        if book:
            if len(customer.loaned_books) < 2:
                if book.take():
                    customer.loaned_books.append(book)
                    book.loan_history.append((datetime.now(), customer.full_name))
                    print(f"Book '{book.title}' has been successfully loaned to {customer.full_name}.")
                    self.save_state("library_state.json")  
                else:
                    print(f"Book '{book.title}' is not available for loan.")
            else:
                print(f"{customer.full_name} has already borrowed the maximum number of books (2).")
        else:
            print(f"Book '{title}' not found in the library.")

    def return_book(self, customer, title):
        book = self.find_book(title)
        if book in customer.loaned_books:
            if book.return_book():
                customer.loaned_books.remove(book)
                book.loan_history.append((datetime.now(), "Returned"))
                print(f"Book '{book.title}' has been successfully returned by {customer.full_name}.")
                self.save_state("library_state.json") 
            else:
                print(f"Book '{book.title}' is not checked out by {customer.full_name}.")
        else:
            print(f"{customer.full_name} does not have book '{title}' on loan.")

    def order_book(self, customer, title):
        if title not in [book.title for book in customer.ordered_books]:
            book = self.find_book(title)
            if book:
                customer.ordered_books.append(book)
                print(f"Book '{book.title}' has been ordered by {customer.full_name}.")
                self.save_state("library_state.json") 
            else:
                print(f"Book '{title}' not found in the library.")
        else:
            print(f"{customer.full_name} has already ordered book '{title}'.")

    def save_state(self, file_path: Optional[str] = "library_state.json"):
        library_state = {
            "name": self.name,
            "address": self.address,
            "books": [
                {
                    "title": book.title,
                    "author": book.author,
                    "year": book.year,
                    "genre": book.genre,
                    "language": book.language,
                    "available": book.available
                }
                for book in self.books
            ],
            "customers": [
                {
                    "full_name": customer.full_name,
                    "age": customer.age,
                    "town": customer.town,
                    "loaned_books": [book.title for book in customer.loaned_books],
                    "ordered_books": [book.title for book in customer.ordered_books]
                }
                for customer in self.customers
            ]
        }

        with open(file_path, 'w') as file:
            json.dump(library_state, file, indent=2)

    def load_state(self, library_file_path: Optional[str] = "library_state.json", customer_file_path: Optional[str] = "customers.json"):
        try:
            with open(customer_file_path, 'r') as file:
                customer_data = json.load(file)

                loaded_customers = [
                    Customer(
                        full_name=data["full_name"],
                        age=data["age"],
                        town=data["town"]
                    )
                    for data in customer_data
                ]

                self.customers.extend(loaded_customers)  # Add loaded customers to the library

                for customer_info in customer_data:
                    customer = self.find_customer(customer_info["full_name"])
                    if customer:
                        customer.loaned_books = [self.find_book(title) for title in customer_info["loaned_books"]]
                        customer.ordered_books = [self.find_book(title) for title in customer_info["ordered_books"]]

            with open(library_file_path, 'r') as file:
                library_state = json.load(file)

                # Load library state...
                for book_info in library_state["books"]:
                    book = self.find_book(book_info["title"])
                    if book:
                        book.available = book_info["available"]

            print("State loaded successfully.")
        except FileNotFoundError:
            print(f"Error: File not found. Creating a new library instance.")
            self.create_default_customers_from_json(customer_file_path)  # Provide the path to your default customers file
        except Exception as e:
            print(f"Error loading state: {str(e)}")


class LibraryTUI:
    def __init__(self, library):
        self.library = library

    def display_menu(self):
        print("\nLibrary Management System")
        print("1. Display Books")
        print("2. Loan Book")
        print("3. Return Book")
        print("4. Order Book")
        print("5. Display Customer Info")
        print("6. Save State")
        print("7. Quit")

    def run(self):
        file_path = "library_state.json"
        self.load_library_state(file_path)

        while True:
            self.display_menu()
            choice = input("Enter your choice (1-7): ")

            if choice == "1":
                self.library.display_books()
            elif choice == "2":
                customer_name = input("Enter your full name: ")
                title_to_loan = input("Enter the title of the book you want to loan: ")
                customer = self.find_customer(customer_name)
                if customer:
                    self.library.loan_book(customer, title_to_loan)
                else:
                    print(f"Customer '{customer_name}' not found.")
            elif choice == "3":
                customer_name = input("Enter your full name: ")
                title_to_return = input("Enter the title of the book you want to return: ")
                customer = self.find_customer(customer_name)
                if customer:
                    self.library.return_book(customer, title_to_return)
                else:
                    print(f"Customer '{customer_name}' not found.")
            elif choice == "4":
                customer_name = input("Enter your full name: ")
                title_to_order = input("Enter the title of the book you want to order: ")
                customer = self.find_customer(customer_name)
                if customer:
                    self.library.order_book(customer, title_to_order)
                else:
                    print(f"Customer '{customer_name}' not found.")
            elif choice == "5":
                customer_name = input("Enter the full name of the customer: ")
                customer = self.find_customer(customer_name)
                if customer:
                    customer.show_info()
                else:
                    print(f"Customer '{customer_name}' not found.")
            elif choice == "6":
                file_path = input("Enter the file path to save the state: ")
                self.library.save_state(file_path)
                print(f"State saved to {file_path}.")
            elif choice == "7":
                file_path = "library_state.json"
                self.library.save_state(file_path)
                print(f"State saved to {file_path}.")
                print("Exiting the Library Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def find_customer(self, name):
        for customer in self.library.customers:
            if customer.full_name == name:
                return customer
        return None

    def load_library_state(self, file_path):
        try:
            self.library.load_state(file_path)
            print("State loaded successfully.")
        except Exception as e:
            print(f"Error loading library state: {str(e)}")

if __name__ == "__main__":
    my_library = Library("City Library", "123 Main St")

    tui = LibraryTUI(my_library)
    tui.run()
