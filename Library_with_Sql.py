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
    

def add_book_to_db(ID, Type, series, Title, author, year, Available):
    # Connect to the SQLite database
    conn = sqlite3.connect('data.db')

    # Create a cursor object
    c = conn.cursor()

    # SQL command to insert a book into the 'books' table
    sql = '''INSERT INTO Books(ID, Type, series, Title, author, year, Available)
             VALUES(?,?,?,?,?,?,?)'''

    # Execute the SQL command
    c.execute(sql, (ID, Type, series, Title, author, year, Available))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()





def add_customer_to_db(CustomerID, Name, Year):
    # Connect to the SQLite database
    conn = sqlite3.connect('data.db')

    # Create a cursor object
    c = conn.cursor()

    # SQL command to insert a customer into the 'customers' table
    sql = '''INSERT INTO customers(CustomerID, Name, Year)
             VALUES(?,?,?)'''

    # Execute the SQL command
    c.execute(sql, (CustomerID, Name, Year))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()


def change_available_status(book_id, Available):
    # Connect to the SQLite database
    conn = sqlite3.connect('data.db')

    # Create a cursor object
    c = conn.cursor()

    # Check if the book exists in the database
    c.execute("SELECT * FROM Books WHERE ID = ?", (book_id,))
    book = c.fetchone()

    if book is None:
        print(f"No book found with ID {book_id}")
        return

    # SQL command to update the available status of a book
    sql = '''UPDATE Books SET Available = ? WHERE ID = ?'''

    # Execute the SQL command
    c.execute(sql, (Available, book_id))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# change_available_status(1, 'Yes')


def search_book_by_title(title):
    # Connect to the SQLite database
    conn = sqlite3.connect('data.db')

    # Create a cursor object
    c = conn.cursor()

    # SQL command to search for a book by title
    sql = '''SELECT * FROM Books WHERE Title = ?'''

    # Execute the SQL command
    c.execute(sql, (title,))

    # Fetch all the rows
    books = c.fetchall()

    # Print the rows
    for book in books:
        print(book)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()


def search_book_by_author(author):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    c.execute('SELECT * FROM Books WHERE author = ?', (author,))

    books = c.fetchall()

    for book in books:
        print(book)

    conn.commit()
    conn.close()

def search_book_by_year(year):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    c.execute('SELECT * FROM Books WHERE year = ?', (year,))

    books = c.fetchall()

    for book in books:
        print(book)

    conn.commit()
    conn.close()


def search_book_by_series(series):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    c.execute('SELECT * FROM Books WHERE series = ?', (series,))

    books = c.fetchall()

    for book in books:
        print(book)

    conn.commit()
    conn.close()

def loan_a_book(BookID, CustomerID):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    # Get the current date

    c.execute('''
        INSERT INTO Loans (BookID, CustomerID)
        VALUES (?, ?)
    ''', (BookID, CustomerID))

    # Update the book's availability
    c.execute('''
        UPDATE Books SET Available = 'No' WHERE ID = ?
    ''', (BookID,))

    conn.commit()
    conn.close()

def return_a_book(book_id):
    conn = sqlite3.connect('data.db')

    c = conn.cursor()
    c.execute("SELECT * FROM Books WHERE ID = ?", (book_id,))
    book = c.fetchone()

    if book is None:
        print(f"No book found with ID {book_id}")
        return

    sql = '''UPDATE Books SET Available = ?, Customer_ID = ? WHERE ID = ?'''

    c.execute(sql, ('Yes', None, book_id))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

def display_all_books():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    c.execute('SELECT * FROM Books')

    books = c.fetchall()

    for book in books:
        print(book)

    conn.commit()
    conn.close()

display_all_books()
    


#     def main_menu(self):
#         while True:
#             print("""
#         Welcome to the Library!
#         {:<20} {:<20}
#         {:<20} {:<20}
#         {:<20} {:<20}
#         {:<20} {:<20}
#         {:<20} {:<20}
#         {:<20} {:<20}
#         {:<20} {:<20}
#         """.format(
#             '1. Add a new customer', '     8. Display late loans',
#             '2. Add a new book', '      9. Find book by name',
#             '3. Loan a book', '      10. Find customer by name',
#             '4. Return a book', '      11. Remove book',
#             '5. Display all books', '      12. Remove customer',
#             '6. Display all customers', '  13. Return all the customer books',
#             '7. Display all loans', '      14. Exit '
#         ))


#             choice = input('Enter your choice: ')
#             if choice == '1':
                

                
#             elif choice == '2':

            
#             elif choice == '3':



#             elif choice == '4':

                
#             elif choice == '5':
#                 
#             elif choice == '6':
#                
#             elif choice == '7':
#                 
#             elif choice == '8':
#                 
#             elif choice == '9':
#                 
#             elif choice == '10':
#                 
#             elif choice == '11':
#                
#             elif choice == '12':
#                 
#             elif choice == '13':
#                 
#             elif choice == '14':
#                 print('Goodbye!')
            
#             else:
#                 print('Invalid choice. Please try again.')
                

# if __name__ == "__main__":
#     ui = Library("My Library", "123 Main Street")
#     ui.main_menu()