import unittest
import os
import sys
sys.path.insert(0, os.path.abspath( os.path.join(os.path.dirname(__file__),
                                               '../src/') ))
from dr_sdk_lotr.books import Books
from config import access_token

class TestBooks(unittest.TestCase):

    def test_get_books(self):
        books = Books(self.api_key)
        test_get_books = books.get_books()
        self.assertEqual(test_get_books["total"], 3)
        print(test_get_books)

    def test_get_book_by_id(self):
        books = Books(self.api_key)
        test_book_by_id = books.get_book_by_id('5cf58077b53e011a64671583')
        self.assertEqual(test_book_by_id["_id"], '5cf58077b53e011a64671583')
        self.assertEqual(test_book_by_id["name"], "The Two Towers")

    def test_get_all_chapters_of_book(self):
        books = Books(self.api_key)
        test_get_all_chapters_of_book = books.get_all_chapters_of_book('5cf58077b53e011a64671583')
        self.assertEqual(len(test_get_all_chapters_of_book), 21)
        self.assertEqual(test_get_all_chapters_of_book[0]['chapterName'], "The Departure of Boromir")

if __name__ == '__main__':
    TestBooks.api_key = access_token
    unittest.main()
