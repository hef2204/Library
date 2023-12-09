import pytest
import unittest
from Class_Library import Library  # assuming your Library class is in a file named library.py


def library():
    library = Library('My Library', '123 Main Street')
    library.add_book('1', 'series1', 'title1', 'author1', 'year1')
    library.add_customer('1', 'John Doe', '25', '123 Street', 'john.doe@example.com')
    return library

def test_borrow_book_by_id(library): 
    # Test borrowing a book by its ID
    library.borrow_book('1', '1', by_id=True)
    book = library.find_book_by_id('1')
    assert book['available'] == False

def test_borrow_book_by_name(library):
    # Test borrowing a book by its name
    library.borrow_book('1', 'title1', by_id=False)
    book = library.find_book_by_id('1')
    assert book['available'] == False


    library.borrow_book('1', 'title1', by_id=False)
