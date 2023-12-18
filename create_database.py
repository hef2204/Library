import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()


create_table = "CREATE TABLE IF NOT EXISTS Books (ID INTEGER PRIMARY KEY, Type TEXT, Series TEXT, Title Text, Author TEXT, Year TEXT, Available TEXT)"

cursor.execute(create_table)
