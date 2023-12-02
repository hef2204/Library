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
        with open('loan_history.json', 'r') as loan_history_file:
            self.loan_history = json.load(loan_history_file)
        try:
            with open('Books.json', 'r') as Books_file:
                self.books = json.load(Books_file)
        except FileNotFoundError:
            pass  

       
        try:
            with open('customers.json', 'r') as f:
                self.customers = json.load(f)
        except FileNotFoundError:
            pass  

        
        try:
            with open('loan_history.json', 'r') as f:
                self.loan_history = json.load(f)
        except FileNotFoundError:
            pass

       
        try:
            with open('order_history.json', 'r') as f:
                self.order_history = json.load(f)
        except FileNotFoundError:
            pass  

        self.load_books()
        self.load_customers()
        self.load_loan_history()
        self.load_order_history()

    def load_loan_history(self):
        try:
            with open('loan_history.json', 'r') as loan_history_file:
                self.loan_history = json.load(loan_history_file)
        except FileNotFoundError:
            pass



    def load_books(self):
        try:
            with open('Books.json', 'r') as books:
                self.books = json.load(books)
        except FileNotFoundError:
            self.books = {}

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
        self.save_book()
        print(f"Book with from the {series} added successfully!")

    def display_books(self):
        for series, book_info in self.books.items():
            if book_info['available']:
                print(f"Series: {series}, Title: {book_info['title']}, Author: {book_info['author']}, Year: {book_info['year']}, Available: {book_info['available']}")

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

    def show_customer_history(self, customer_id):
        customer_id = str(customer_id)  
        if customer_id in self.loan_history:
            print(f"ID: {customer_id}, Name: {self.loan_history[customer_id]['Name']}, Age: {self.loan_history[customer_id]['Age']}, Address: {self.loan_history[customer_id]['Address']}, Email: {self.loan_history[customer_id]['Email']}, Books: {self.loan_history[customer_id]['Books']}")
            if customer_id in self.orders:
                print(f"Orders: {self.orders[customer_id]}")
            else:
                print("No orders found for this customer.")
        else:
            print(f"Customer with ID {customer_id} was not found")
        
    

    def show_book_info(self, series):
        if series in self.books:
            print(f"Series: {series}, Title: {self.books[series]['title']}, Author: {self.books[series]['author']}, Year: {self.books[series]['year']}, Available: {self.books[series]['available']}")
        else:
            print(f"Book from series {series} was not found")



    def add_loan_history(self, customer_id, series, status):
        if customer_id not in self.loan_history:
            self.loan_history[customer_id] = {
                'Name': self.customers[customer_id]['Name'],
                'Age': self.customers[customer_id]['Age'],
                'Address': self.customers[customer_id]['Address'],
                'Email': self.customers[customer_id]['Email'],
                'Books': {}
            }

        self.loan_history[customer_id]['Books'][series] = {
            'Borrowed At': str(datetime.now()) if status == 'Borrowed' else None,
            'Returned At': str(datetime.now()) if status == 'Returned' else None,
            'Status': status
        }

        self.save_loan_history()

    def save_loan_history(self):
        with open('loan_history.json', 'w') as loan_history_file:
            json.dump(self.loan_history, loan_history_file, indent=4)

    def add_loan_history(self, customer_id):
        if customer_id not in self.loan_history:
            self.loan_history[customer_id] = {
            'Name': self.customers[customer_id]['Name'],
            'Age': self.customers[customer_id]['Age'],
            'Address': self.customers[customer_id]['Address'],
            'Email': self.customers[customer_id]['Email'],
            'Books': {}
        }
        else:
            print(f"No customer with ID {customer_id} exists")

   

    def borrow_book(self, customer_id, series):
        if customer_id in self.customers:
            if customer_id not in self.loan_history:
                self.add_loan_history(customer_id)
                
            if len(self.loan_history[customer_id]['Books']) < 2:
                if series in self.books and self.books[series]['available']:
                    if series in self.books and self.books[series]['available']:
                        if series not in self.loan_history[customer_id]['Books']: 
                            self.books[series]['available'] = False
                            print(f"Book from series {series} borrowed by customer {customer_id}")
                            self.loan_history[customer_id]['Books'][series] = {'Borrowed At': str(datetime.now()), 'Status': 'Borrowed'}
                            self.save_book()
                            self.save_loan_history()
                            self.add_loan_history(customer_id, series, 'Borrowed')  # Add this line

                    else:
                        print(f"Book from series {series} is already borrowed by customer {customer_id}")
                else:
                    print(f"Book from series {series} is not available")
            else:
                print(f"Customer {customer_id} has already borrowed 2 books, You should return one of them first")
        else:
            print(f"No customer with ID {customer_id} exists")

    def return_book(self, customer_id, series):
        if series in self.loan_history[customer_id]['Books']:
            self.books[series]['available'] = True
            self.loan_history[customer_id]['Books'][series]['Returned At'] = str(datetime.now())
            self.loan_history[customer_id]['Books'][series]['Status'] = 'Returned'
            self.save_book()  # Save books after a book is returned
            self.save_loan_history()
            self.add_loan_history(customer_id, series, 'Returned')
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
        if customer_id not in self.orders:
            self.orders[customer_id] = {'Books': []}
        if len(self.orders[customer_id]['Books']) < 2:
            if series not in self.books or not self.books[series]['available'] or not self.books[series]['year'] == year:
                book_details = {
                    'Series': series,
                    'Title': title,
                    'Author': author,
                    'Year': year
                }
                self.orders[customer_id]['Books'].append(book_details.copy())
                self.save_orders()
                print(f"Customer {customer_id} ordered book from series {series}")
            else:
                print(f"Book from series {series} is already available")
        else:
            print(f"Customer {customer_id} has already ordered 2 books")

    def show_all_orders(self):
        for customer_id, order_info in self.orders.items():
            print(f"ID: {customer_id}, Books: {order_info['Books']}")

    def show_order_info(self, customer_id):
        if customer_id in self.orders:
            print(f"ID: {customer_id}, Books: {self.orders[customer_id]['Books']}")
        else:
            print(f"Customer {customer_id} did not order any books")

    def cancel_order(self, customer_id, series):
        if customer_id in self.orders:
            for book in self.orders[customer_id]['Books']:
                if book['Series'] == series:
                    self.orders[customer_id]['Books'].remove(book)
                    self.save_orders()
                    print(f"Customer {customer_id} canceled order for book from series {series}")
                    return
            print(f"Customer {customer_id} did not order book from series {series}")
        else:
            print(f"Customer {customer_id} did not order any books")

    def load_order_history(self):
        try:
            with open('order_history.json', 'r') as order_history_file:
                self.order_history = json.load(order_history_file)
        except FileNotFoundError:
            pass


    def start_program(self):
        while True:
            print("                         ")
            print("Welcome to the library!")
            print("1. Loan a book")
            print("2. Return a book")
            print("3. Order a book")
            print("4. Cancel order")
            print("5. Show all available books")
            print("6. Exit")
            print("7. Show customers history")
            
            
            choice = input("Enter your choice: ")

            if choice == '1':
                customer_id = int(input("Enter your customer ID: "))
                series = input("Enter series: ")
                my_library.borrow_book(customer_id, series)

            elif choice == '2':
                customer_id = int(input("Enter your customer ID: "))
                series = input("Enter series: ")
                my_library.return_book(customer_id, series)

            elif choice == '3':
                customer_id = int(input("Enter your customer ID: "))
                series = input("Enter series: ")
                my_library.order_book(customer_id, series)

            elif choice == '4':
                customer_id = int(input("Enter your customer ID: "))
                series = input("Enter series: ")
                my_library.cancel_order(customer_id, series)

            elif choice == '5':
                my_library.display_books()

            elif choice == '6':
                print("Exiting the program")
                break

            elif choice == '7':
                customer_id = input("Enter your customer ID: ")
                my_library.show_customer_history(customer_id)

            else:
                print("Invalid choice. Please enter a number between 1 and 6.")





    


my_library = Library('my library', 'peer 78,haifa')
# my_library.load_books()
# my_library.add_book("Harry potter", "The chamber", 'J.k rolling', 2001)
# my_library.add_book('ABC123', 'Python Programming','John Doe',2022)
# my_library.add_book('bye', 'Python Programming','John Doe',2022)
# my_library.add_book('C#', 'Python Programming','John Doe',2022)
# my_library.save_book()
my_library.add_customer(1, 'boris', 28, 'peer 78, Haifa', 'bbb@com')
my_library.add_customer(2,'Seva', 28, 'peer 78, Haifa', 'bbb@com')
my_library.add_customer(3, 'Slava', 28, 'peer 78, Petah Tikva', 'bbb@com')
my_library.add_customer(4, 'Ofer', 38, 'bbb 78, K.Motskin', 'bbb@com')
my_library.add_customer(5, 'Shay', 28, 'peer 78, K.Motskin', 'bbb@com')
my_library.add_customer(6, 'Saar', 28, 'peer 78, Haifa', 'bbb@com')
my_library.add_customer(7, 'Yahav', 28, 'peer 78, T.A', 'bbb@com')
my_library.add_customer(8, 'Alisa', 28, 'peer 78, Jerusalem', 'bbb@com')
my_library.add_customer(9, 'Yana', 28, 'peer 78, Haifa', 'bbb@com')
# my_library.add_book('ABCdef123', 'Python Programming','John Doe',2022)

my_library.load_books() 



my_library.start_program()






