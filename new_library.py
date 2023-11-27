from datetime import timedelta, datetime
import json
import string

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
        
    
        
        # def take_book(self, borrower_name):
        #     if self.available:
        #         self.available = False
        #         loan_date = datetime.now()
        #         due_date = loan_date + timedelta(days=self.max_loan_days)
        #         self.loan_history.append({'borrower': borrower_name, 'loan_date': loan_date, 'due_date': due_date})
        #         print(f"Book '{self.title}' taken by {borrower_name}. Due date: {due_date.strftime('%Y-%m-%d')}")
        #         return True
        #     else:
        #         print(f"The book '{self.title}' is not available for loan.")
        #         return False
        
        # def return_book(self, borrower_name):
            
        #     if not self.available:
        #         self.available = True
        #         return True
        #     else:
        #         print(f"The book '{self.title}' is not checked out.")
        #         return False

class Customers:
    def __init__(self, name, age, address, email):
        self.name = name
        self.age = age
        self.address = address
        self.email = email
        

class Library:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.books = {}
        self.customers = {}
        self.loan_history = {}
        self.orders = {}



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
        try:
            with open('Books.json', 'w') as books:
                json.dump(self.books, books, indent=2 )
        except FileNotFoundError:
            pass

    def save_customer(self):
        with open('customers.json', 'w') as customers:
            json.dump(self.customers, customers, indent=2)

    def add_book(self, series, title, author, year):
        self.books[series] = {'title': title, 'author': author, 'year': year, 'available': True}
        print(f"Book with from the {series} added successfully!")

    def add_customer(self, customer_id, name, age, address, email):
        self.customers[customer_id] = {'Name': name, 'Age': age, 'Address': address, "Email": email}
        print(f"Customer with ID {customer_id} added successfully!")

    def check_if_available(self, series):
        if series in self.books:
            return self.books[series]['available']
        else:
            print(f'the book from series {series} was not found')

    def show_all_books(self):
        for series, book_info in self.books.items():
            print(f"Series: {series}, Title: {book_info['title']}, Author: {book_info['author']}, Year: {book_info['year']}, Available: {book_info['available']}")

    def show_all_customers(self):
        for customer_id, customer_info in self.customers.items():
            print(f"ID: {customer_id}, Name: {customer_info['Name']}, Age: {customer_info['Age']}, Address: {customer_info['Address']}, Email: {customer_info['Email']}")

    

    def show_book_info(self, series):
        if series in self.books:
            print(f"Series: {series}, Title: {self.books[series]['title']}, Author: {self.books[series]['author']}, Year: {self.books[series]['year']}, Available: {self.books[series]['available']}")
        else:
            print(f"Book from series {series} was not found")

    def load_loan_history(self):
        try:
            with open('loan_history.json', 'r') as loan_history_file:
                self.loan_history = json.load(loan_history_file)
        except FileNotFoundError:
            pass

    def save_loan_history(self):
        with open('loan_history.json', 'w') as loan_history_file:
            json.dump(self.loan_history, loan_history_file, indent=4)

    def add_loan_history(self, customer_id, name, age, address, email, books):
        self.loan_history[customer_id] = {'Name': name, 'Age': age, 'Address': address, "Email": email, 'Books': books}
        print(f"Loan history for customer {customer_id} added successfully!")

   

    def borrow_book(self, customer_id, series):
        if customer_id not in self.loan_history:
            self.add_loan_history(customer_id, self.customers[customer_id]['Name'], self.customers[customer_id]['Age'], self.customers[customer_id]['Address'], self.customers[customer_id]['Email'], {})
            
        if len(self.loan_history[customer_id]['Books']) < 2:
            if series in self.books and self.books[series]['available']:
                self.books[series]['available'] = False
                print(f"Book from series {series} borrowed by customer {customer_id}")
                self.loan_history[customer_id]['Books'][series] = {'Borrowed At': str(datetime.now())}
            else:
                print(f"Book from series {series} is not available")
        else:
            print(f"Customer {customer_id} has already borrowed 2 books, You should return one of them first")

    def return_book(self, customer_id, series):
        if series in self.loan_history[customer_id]['Books']:
            self.books[series]['available'] = True
            self.loan_history[customer_id]['Books'][series]['Returned At'] = str(datetime.now())
            print(f"Book from series {series} returned by customer {customer_id}")
        else:
            print(f"Customer {customer_id} did not borrow book from series {series}, someone else have borrowed it")

    
    def load_orders(self):
        try:
            with open('orders.json', 'r') as orders:
                self.orders = json.load(orders)
        except FileNotFoundError:
            pass

    def save_orders(self):
        try:
            with open('orders.json', 'w') as orders:
                json.dump(self.orders, orders, indent=2)
        except FileNotFoundError:
            pass
    
    
    def order_book(self, customer_id, series, title, author, year):
        if series not in self.books or not self.books[series]['year'] == year:
            if customer_id not in self.orders:
                self.orders[customer_id] = []
            book_details = {
                'Series': series,
                'Title': title,
                'Author': author,
                'Year': year
            }
            self.orders[customer_id].append(book_details)
            self.save_orders()
            print(f"Customer {customer_id} ordered book from series {series}")
        else:
            print(f"Book from series {series} is already available")


        

    
# self.books[series]['available'] == False:


    


my_library = Library('my library', 'peer 78,haifa')
my_library.add_book("Harry potter", "The chamber", 'J.k rolling', 2001)
my_library.add_book('ABC123', 'Python Programming','John Doe',2022)
my_library.add_book('bye', 'Python Programming','John Doe',2022)
my_library.add_book('C#', 'Python Programming','John Doe',2022)
my_library.save_book()
my_library.add_customer(1, 'boris', 28, 'peer 78, Haifa', 'bbb@com')
my_library.add_customer(2, 'Seva', 28, 'peer 78, Haifa', 'bbb@com')
my_library.add_customer(3, 'Slava', 28, 'peer 78, Petah Tikva', 'bbb@com')
my_library.add_customer(4, 'Ofer', 38, 'bbb 78, K.Motskin', 'bbb@com')
my_library.add_customer(5, 'Shay', 28, 'peer 78, K.Motskin', 'bbb@com')
my_library.add_customer(6, 'Saar', 28, 'peer 78, Haifa', 'bbb@com')
my_library.add_customer(7, 'Yahav', 28, 'peer 78, T.A', 'bbb@com')
my_library.add_customer(8, 'Alisa', 28, 'peer 78, Jerusalem', 'bbb@com')
my_library.save_customer()

my_library.borrow_book(1, 'ABC123')
my_library.borrow_book(1, 'Harry potter')
# my_library.return_book(1, 'Harry potter')

# my_library.borrow_book(2, 'Harry potter')
# my_library.save_loan_history()
# my_library.return_book(2, 'Harry potter')
# my_library.borrow_book(1, 'bye')
# my_library.borrow_book(2, 'Harry potter')
# # my_library.return_book(2, 'bye')
# my_library.save_loan_history()
# my_library.borrow_book(6, 'ABC123')
# my_library.return_book(1, 'bye')
# my_library.return_book(2, 'Harry potter')
my_library.borrow_book(1, 'C#')
# my_library.return_book(1, 'C#')

# my_library.save_loan_history()
# my_library.load_loan_history()
# my_library.order_book('gggg', 1)
# my_library.order_book('ABC12675456')
# my_library.order_book(1, 'XYZ456', 'Test Title', 'Test Author', 2022)
# my_library.order_book(1, 'C#', 'Python Programming','John Doe',2022)
# my_library.order_book(1, 'C#', 'Python Programming','John Doe',2025)
# my_library.order_book(1, "Harry potter", "The chamber", 'J.k rolling', 2005)
# my_library.order_book(1, "Harry potter", "The chamber", 'J.k rolling', 2001)
# my_library.order_book(1, "Harry potterhhhhhh", "The kaka", 'J.kaka rolling', 2001)
# my_library.load_orders()
# my_library.order_books('ABC1234567')

# my_library.show_all_books()

