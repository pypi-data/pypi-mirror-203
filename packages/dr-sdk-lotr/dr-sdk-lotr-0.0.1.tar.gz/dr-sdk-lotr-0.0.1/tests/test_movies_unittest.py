import unittest
import os
import sys
sys.path.insert(0, os.path.abspath( os.path.join(os.path.dirname(__file__),
                                               '../src/') ))

from dr_sdk_lotr.movies import Movies
from config import access_token


class TestMovies(unittest.TestCase):

    def test_get_movies(self):
        movies = Movies(self.api_key)
        test_get_movies = movies.get_movies()
        print(test_get_movies)
        self.assertEqual(len(test_get_movies), 8)

    def test_get_movie_by_id(self):
        movies = Movies(self.api_key)
        test_get_movie_by_id = movies.get_movie_by_id('5cd95395de30eff6ebccde56')
        self.assertEqual(test_get_movie_by_id['name'], "The Lord of the Rings Series")
        self.assertEqual(test_get_movie_by_id['_id'],'5cd95395de30eff6ebccde56' )

    def test_get_all_quotes_by_movie(self):
        movies = Movies(self.api_key)
        test_get_all_quotes_by_movie = movies.get_all_quotes_by_movie('5cd95395de30eff6ebccde5c')
        self.assertEqual(len(test_get_all_quotes_by_movie), 503)


if __name__ == '__main__':
    TestMovies.api_key = access_token
    unittest.main()
