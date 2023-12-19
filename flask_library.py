import flask
from flask import Flask, render_template
from Library_project import Library

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

library = Library("dd", "ff")

@app.route('/display_all_books')
def display_all_books():
    return render_template('display_all_books.html' , books = Library.display_all_books())
    

def display_all_customers():
    return render_template('display_all_customers.html' , customers = Library.display_all_customers())

@app.route('/display_all_loans')
def display_all_loans():
    return render_template('display_all_loans.html' , loans = Library.display_all_books())

if __name__ == '__main__':
    app.run()