import pytest
import unittest
from Class_Library import Library


def test_add_book():
    library = Library('My Library', '123 Main Street')
    library.add_book('Fiction', 'Harry Potter', 'The Philosopher\'s Stone', 'J.K. Rowling', '1997')
    book = library.find_book_by_name('The Philosopher\'s Stone')
    assert book is not None
    assert book['title'] == 'The Philosopher\'s Stone'
    assert book['author'] == 'J.K. Rowling'
    assert book['year'] == '1997'


pytest.main()
