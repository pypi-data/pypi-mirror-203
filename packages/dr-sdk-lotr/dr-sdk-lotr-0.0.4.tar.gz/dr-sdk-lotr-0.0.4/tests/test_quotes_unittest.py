import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dr_sdk_lotr.quotes import Quotes
from config import access_token


class TestQuotes(unittest.TestCase):

    def test_get_all_movie_quotes(self):
        quotes = Quotes(self.api_key)
        test_get_all_movie_quotes = quotes.get_all_movie_quotes()
        self.assertEqual(len(test_get_all_movie_quotes), 1000)

    def test_get_one_movie_quote_by_id(self):
        quotes = Quotes(self.api_key)
        test_get_one_movie_quote_by_id = quotes.get_one_movie_quote_by_id('5cd96e05de30eff6ebccebce')
        self.assertEqual(test_get_one_movie_quote_by_id['id'], "5cd96e05de30eff6ebccebce")
        self.assertEqual(test_get_one_movie_quote_by_id['dialog'],'Tell me what happened and I will ease your passing.' )

if __name__ == '__main__':
    TestQuotes.api_key = access_token
    unittest.main()
