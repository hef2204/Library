from datetime import timedelta, datetime
import json
import string
import Book
import Customer
import sqlite3


class Library:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.books = {}
        self.customers = {}
        self.loan_history = {}
        self.orders = {}
        self.book_id_counter = 1
        try:
            with open('book_id_counter.json', 'r') as f:
                self.book_id_counter = json.load(f)
        except FileNotFoundError:
            self.book_id_counter = 1

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

    def add_book(self, book_type, series, title, author, year):
        book_id = self.book_id_counter  
        if book_type == 'Fiction':
            max_loan_time = 10
        elif book_type == "Drama":
            max_loan_time = 5
        elif book_type == 'Fantasy':
            max_loan_time = 2
        else:
            print("Invalid book type. Please enter a type between Fiction , Drama or Fantasy.")
            return
        self.books[book_id] = {'type': book_type, 'series': series, 'title': title, 'author': author, 'year': year, 'available': True, 'max_loan_time': max_loan_time}
        self.save_book()
        print(f"Book with ID {book_id} from the {series} added successfully!")
        self.book_id_counter += 1
        with open('book_id_counter.json', 'w') as f:
            json.dump(self.book_id_counter, f)
        

    def remove_book(self, book_id):
        if book_id in self.books:
            self.books.pop(book_id)
            self.save_book()
            print(f"Book with ID {book_id} removed successfully!")
        else:
            print(f"Book with ID {book_id} was not found")


    def display_all_books(self):
        for series, book_info, book_id in self.books.items():
            print(f"Id: {book_id}, Series: {series}, Title: {book_info['title']}, Author: {book_info['author']}, Year: {book_info['year']}, Available: {book_info['available']}")


    def display_late_borrowed_books(self):
        for book_id, book_info in self.books.items():
            if not book_info['available']:
                due_date = datetime.strptime(book_info['due_date'], "%Y-%m-%d")
                if datetime.now() > due_date:
                    print(f"Book ID: {book_id}, Series: {book_info['series']}, Title: {book_info['title']}, Author: {book_info['author']}, Year: {book_info['year']}, was borrowed on: {book_info['due_date']}")
                else:
                    print("No late loans found.")


    def display_all_borrowed_books(self):
        for book_id, book_info in self.books.items():
            for customer_id, customer_info in self.loan_history.items():
                if not book_info['available']:
                    print(f"Book ID: {book_id}, Series: {book_info['series']}, Title: {book_info['title']}, Author: {book_info['author']}, Year: {book_info['year']}, was borrowed by: {customer_info['Name']} id: {customer_id}")
        else:
            print("No loans found.")

    def display_all_customers(self):
        for customer_id, customer_info in self.customers.items():
            print(f"ID: {customer_id}, Name: {customer_info['Name']}, Age: {customer_info['Age']}, Address: {customer_info['Address']}, Email: {customer_info['Email']}")

    def display_all_books(self):
        for book_id, book_info in self.books.items():
            print(f"Book ID: {book_id}")
            for key, value in book_info.items():
                print(f"{key}: {value}")
            print()

    def add_customer(self, customer_id, name, age, address, email):
        self.customers[customer_id] = {'Name': name, 'Age': age, 'Address': address, "Email": email}
        print(f"Customer with ID {customer_id} added successfully!")

    def add_new_customer(self, name, age, address, email):
        customer_id = len(self.customers) + 2
        self.customers[customer_id] = {'Name': name, 'Age': age, 'Address': address, "Email": email}
        self.save_customer()
        print(f"Customer with ID {customer_id} added successfully!")


    def remove_customer(self, customer_id):
        if customer_id in self.customers:
            self.customers.pop(customer_id)
            print(f"Customer with ID {customer_id} removed successfully!")
            self.save_customer()
        else:
            print(f"Customer with ID {customer_id} was not found")
        



    def check_if_available(self, series):
        if series in self.books:
            return self.books[series]['available']
        else:
            print(f'the book from series {series} was not found')


    def find_book_by_id(self, book_id):
        if book_id in self.books:
            return self.books[book_id]
        else:
            print(f"Book with ID {book_id} was not found")

    def find_book_by_name(self, book_name):
        for book_id, book_info in self.books.items():
            if book_info['title'] == book_name:
                return book_info
        print(f"Book '{book_name}' was not found")


    def find_customer_by_id(self, customer_id):
        if customer_id in self.customers:
            return self.customers[customer_id]
        else:
            print(f"Customer with ID {customer_id} was not found")

    def find_customer_by_name(self, customer_name):
        customer_name = customer_name.lower()
        for customer_id, customer_info in self.customers.items():
            if customer_info['Name'].lower() == customer_name:
                return customer_info
        return None



    def show_all_books(self):
        for series, book_info in self.books.items():
            print(f"Series: {series}, Title: {book_info['title']}, Author: {book_info['author']}, Year: {book_info['year']}, Available: {book_info['available']}")


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

  
    def add_loan_history(self, customer_id, book_id, state):
        if customer_id not in self.loan_history:
            self.loan_history[customer_id] = {
                'Name': self.customers[customer_id]['Name'],
                'Age': self.customers[customer_id]['Age'],
                'Address': self.customers[customer_id]['Address'],
                'Email': self.customers[customer_id]['Email'],
                'Books': {}
            }
        elif 'Books' not in self.loan_history[customer_id]:
            self.loan_history[customer_id]['Books'] = {}

        if book_id not in self.loan_history[customer_id]['Books']:
            self.loan_history[customer_id]['Books'][book_id] = {
                'title': self.books[book_id]['title'],
                'borrowed_at': '',
                'returned_at': '',
                'state': ''
            }

        if state == 'Borrowed':
            self.loan_history[customer_id]['Books'][book_id]['borrowed_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        elif state == 'Returned':
            self.loan_history[customer_id]['Books'][book_id]['returned_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.loan_history[customer_id]['Books'][book_id]['state'] = state




    def borrow_book(self, customer_id, book_id):
        book = self.books.get(book_id)
        if customer_id not in self.customers:
            print(f"Customer with ID {customer_id} does not exist.")
            return
        if customer_id in self.loan_history:
            borrowed_books = [book for book in self.loan_history[customer_id]['Books'].values() if book['state'] == 'Borrowed']
            if len(borrowed_books) >= 2:
                print(f"Customer with ID {customer_id} has already borrowed 2 books. you should return one of them first.")
                return
        if not book:
            print(f"Book with ID {book_id} does not exist.")
            return
        if not book['available']:
            print(f"Book with ID {book_id} is not available.")
            return
        book['available'] = False
        due_date = datetime.now() + timedelta(days=book['max_loan_time'])
        book['due_date'] = due_date.strftime("%Y-%m-%d")
        self.books[book_id] = book
        self.add_loan_history(customer_id, book_id, 'Borrowed') 
        print(f"Book with ID {book_id} has been borrowed. It is due on {book['due_date']}. You have {book['max_loan_time']} days to return it.")

    def return_book(self, customer_id, book_identifier, by_id=True):
        if by_id:
            book_id = book_identifier
            if book_id in self.books and not self.books[book_id]['available']:
                self.books[book_id]['available'] = True
                self.add_loan_history(customer_id, book_id, 'Returned')
                self.save_book()
                print(f"Book with ID {book_id} returned successfully!")
            else:
                print("Book not borrowed or not found")
        else:
            book_name = book_identifier
            for book_id, book_info in self.books.items():
                if book_info['title'] == book_name and not book_info['available']:
                    book_info['available'] = True
                    self.add_loan_history(customer_id, book_id, 'Returned')
                    self.save_book()
                    print(f"Book '{book_name}' returned successfully!")
                    return
            print("Book not borrowed or not found")


    def return_all_the_customer_books(self, customer_id):
        if customer_id not in self.loan_history:
            print(f"Customer with ID {customer_id} has not borrowed any books.")
            return

        borrowed_books = {book_id: book_info for book_id, book_info in self.loan_history[customer_id]['Books'].items() if book_info['state'] == 'Borrowed'}

        for book_id, book_info in borrowed_books.items():
            self.books[book_id]['available'] = True
            self.loan_history[customer_id]['Books'][book_id]['state'] = 'Returned'
            self.loan_history[customer_id]['Books'][book_id]['returned_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.save_book()
            self.save_loan_history() 
            print(f"Book with ID {book_id} returned successfully!")
    
    def main_menu(self):
        while True:
            print("""
        Welcome to the Library!
        {:<20} {:<20}
        {:<20} {:<20}
        {:<20} {:<20}
        {:<20} {:<20}
        {:<20} {:<20}
        {:<20} {:<20}
        {:<20} {:<20}
        """.format(
            '1. Add a new customer', '     8. Display late loans',
            '2. Add a new book', '      9. Find book by name',
            '3. Loan a book', '      10. Find customer by name',
            '4. Return a book', '      11. Remove book',
            '5. Display all books', '      12. Remove customer',
            '6. Display all customers', '  13. Exit',
            '7. Display all loans', ''
        ))


            choice = input('Enter your choice: ')
            if choice == '1':
                name = input("Enter customer's name: ")
                age = input("Enter customer's age: ")
                address = input("Enter customer's address: ")
                email = input("Enter customer's email: ")
                self.add_new_customer(name, age, address, email)
                self.save_customer()
                

                
            elif choice == '2':
                book_type = input("Enter book's type: ")
                series = input("Enter book's series: ")
                title = input("Enter book's title: ")
                author = input("Enter book's author: ")
                year = input("Enter book's year: ")
                self.add_book(book_type, series, title, author, year)
                self.save_book()
            
            elif choice == '3':
                customer_id = input('Enter the customer ID: ')
                book_id = input('Enter the book ID: ')
                self.borrow_book(customer_id, book_id)
                self.save_book()    
                self.save_customer()
                self.save_loan_history()


            elif choice == '4':
                customer_id = input('Enter the customer ID: ')
                book_id = input('Enter the book ID: ')
                self.return_book(customer_id, book_id)
                self.save_book()
                self.save_customer()
                self.save_loan_history()
                
            elif choice == '5':
                self.display_all_books()
            elif choice == '6':
                self.display_all_customers()
            elif choice == '7':
                self.display_all_borrowed_books()
            elif choice == '8':
                self.display_late_borrowed_books()
            elif choice == '9':
                book_name = input("Enter book's title: ")
                self.find_book_by_name(book_name)
            elif choice == '10':
                customer_name = input("Enter customer's name: ")
                self.find_customer_by_name(customer_name)
            elif choice == '11':
                book_id = str(input("Enter book's ID: "))
                self.remove_book(book_id)
            elif choice == '12':
                customer_id = str(input("Enter customer's ID: "))
                self.remove_customer(customer_id)
            elif choice == '13':
                print('Thank you for using the Library!')
                break
            elif choice == '14':
                customer_id = str(input("Enter customer's ID: "))
                self.return_all_the_customer_books(customer_id)

            else:
                print('Invalid choice. Please try again.')
                

if __name__ == "__main__":
    ui = Library("My Library", "123 Main Street")
    ui.main_menu()

