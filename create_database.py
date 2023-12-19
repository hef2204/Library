import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()


create_table = """CREATE TABLE IF NOT EXISTS Loans(CustomerID INTEGER PRIMARY KEY,
            BookID INTEGER,
            Loan_Date TEXT,
            ReturnDate TEXT)"""


# create_table = "drop table if exists Loans"

cursor.execute(create_table)
