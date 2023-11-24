from datetime import timedelta, datetime
import json

class Book:
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

        def __str__(self):
            return f"Book: {self.title} by {self.author} ({self.year})"

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
        
        def take_book(self, borrower_name):
            if self.available:
                self.available = False
                loan_date = datetime.now()
                due_date = loan_date + timedelta(days=self.max_loan_days)
                self.loan_history.append({'borrower': borrower_name, 'loan_date': loan_date, 'due_date': due_date})
                print(f"Book '{self.title}' taken by {borrower_name}. Due date: {due_date.strftime('%Y-%m-%d')}")
                return True
            else:
                print(f"The book '{self.title}' is not available for loan.")
                return False

class Customers:
    pass

class Library:
    def __init__(self, name, adress):
        self.name = name
        self.adress = adress
        self.books = {}
        self.customers = {}



    def load_books(self):
        try:
            with open('Books.json', 'r') as books:
                self.books = json.load(books)
        except FileNotFoundError:
            pass

    def load_customers(self):
        try:
            with open('customers.json', 'r') as customers:
                self.customers = json.load(customers)
        except FileNotFoundError:
            pass

    def save_book(self):
        with open('Books.json', 'w') as books:
            json.dump(self.books, books, indent=2 )

    def save_customer(self):
        with open('customers.json', 'w') as customers:
            json.dump(self.customers, customers, indent=2)

    def add_book(self, series, title, author, year):
        self.books[series] = {'title': title, 'author': author, 'year': year, 'available': True}
        print(f"Book with from the {series} added successfully!")

    def add_customer(self, customer_id, name, age, adress, email):
        self.customers[customer_id] = {'Name': name, 'Age': age, 'Adress': adress, "Email": email}
        print(f"Customer with ID {customer_id} added successfully!")

    def check_if_avilable(self, series):
        if series in self.books:
            return self.books[series]['available']
        else:
            print(f'the book from series {series} was not found')

    def show_all_books(self):
        for series, book_info in self.books.items():
            print(f"Series: {series}, Title: {book_info['title']}, Author: {book_info['author']}, Year: {book_info['year']}, Available: {book_info['available']}")











class libraryUI:
    pass










































my_library = Library('my library', 'peer 78,haifa')
my_library.add_book("Harry potter", "The chamber", 'J.k rolling', 2001)
my_library.add_book(series='ABC123', title='Python Programming', author='John Doe', year=2022)


# book_series_to_check = 'boris'

# if my_library.check_if_avilable(book_series_to_check):
#     print('available')
# else:
#     print('not')

# my_library.save_book()

# my_library.show_all_books()





# my_library.save_book()
# my_library.load_books()

# my_library.add_customer(1, 'boris', 28, 'peer 78, haifa', 'bbb@com')
# my_library.save_customer()
# my_library.load_customers()



    



