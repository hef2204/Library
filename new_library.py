from datetime import timedelta, datetime
import json
from os import name

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
    pass

class Library:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.books = {}
        self.customers = {}
        self.loan_history = {}



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

    

    def return_book(self, series, customer_id):
        if series in self.books:
            if not self.books[series]['available']:
                self.books[series]['available'] = True
                print(f"Book from series {series} returned by customer {customer_id}")
            else:
                print(f"Book from series {series} is not taken")
        else:
            print(f"Book from series {series} was not found")

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
            json.dump(self.loan_history, loan_history_file, indent=2)

    def add_loan_history(self, customer_id, name, age, address, email, books):
        self.loan_history[customer_id] = {'Name': name, 'Age': age, 'Address': address, "Email": email, 'Books': books}
        print(f"Loan history for customer {customer_id} added successfully!")

   

    def borrow_book(self, customer_id, series):
        if series in self.books and self.books[series]['available']:
            self.books[series]['available'] = False
            print(f"Book from series {series} borrowed by customer {customer_id}")
            if customer_id in self.loan_history:
                self.loan_history[customer_id]['Books'].append(series)
            else:
                self.add_loan_history(customer_id, 'Name', 'Age', 'Address', 'Email', [series])
        else:
            print(f"Book from series {series} is not available")


        

    



    


my_library = Library('my library', 'peer 78,haifa')
my_library.add_book("Harry potter", "The chamber", 'J.k rolling', 2001)
my_library.add_book(series='ABC123', title='Python Programming', author='John Doe', year=2022)
my_library.add_customer(1, 'boris', 28, 'peer 78, haifa', 'bbb@com')
my_library.add_customer(2, 'Seva', 28, 'peer 78, haifa', 'bbb@com')
my_library.save_customer()
# print(my_library.books)

my_library.borrow_book(1 , 'ABC123')
my_library.borrow_book(2 , 'Harry potter')
# my_library.show_all_books()

# my_library.borrow_book('Harry potter', 1)
my_library.save_loan_history()

# my_library.show_all_books()
# my_library.return_book('ABC123', 1)
# my_library.show_all_books()
# my_library.show_book_info('harry potter')









# class libraryUI:
#     def __init__(self):
#         pass

#     def main_menu(self):
#         print("Welcome to the Library!")

#         while True:
#             print("Please select an option:")
#             print("1. Show all books")
#             print("2. Show all customers")
#             print("3. Add a book")
#             print("4. Add a customer")
#             print("5. Take a book")
#             print("6. Return a book")
#             print("7. Show book info")
#             print("8. Exit")
#             option = input("Enter your choice: ")

#             if option == '1':
#                 self.show_all_books()
#             elif option == '2':
#                 self.show_all_customers()
#             elif option == '3':
#                 self.add_book()
#             elif option == '4':
#                 self.add_customer()
#             elif option == '5':
#                 self.take_book()
#             elif option == '6':
#                 self.return_book()
#             elif option == '7':
#                 self.show_book_info()
#             elif option == '8':
#                 print("Goodbye!")
#                 break
#             else:
#                 print("Invalid option, please try again")


# if __name__ == '__main__':
#     library = Library('My Library', '123 Main St')
#     library.load_books()
#     library.load_customers()
#     libraryUI = libraryUI()
#     libraryUI.main_menu()
#     library.save_book()
#     library.save_customer()
















































# book_series_to_check = 'boris'

# if my_library.check_if_avilable(book_series_to_check):
#     print('available')
# else:
#     print('not')

# my_library.save_book()

# my_library.show_all_books()





# my_library.save_book()
# my_library.load_books()


# my_library.save_customer()
# my_library.load_customers()



    



