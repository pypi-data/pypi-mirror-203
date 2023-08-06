import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dr_sdk_lotr.chapters import Chapters
from config import access_token


class TestChapters(unittest.TestCase):

    def test_get_chapters(self):
        chapters = Chapters(self.api_key)
        test_get_chapters = chapters.get_all_book_chapters()
        self.assertEqual(len(test_get_chapters), 62)

    def test_get_chapter_by_id(self):
        chapters = Chapters(self.api_key)
        test_get_chapter_by_id = chapters.get_book_chapter_by_id('6091b6d6d58360f988133bc5')
        self.assertEqual(test_get_chapter_by_id['docs'][0]['chapterName'], "Many Partings")

    def test_get_chapter_by_name(self):
        chapters = Chapters(self.api_key)
        test_get_chapter_by_name = chapters.get_book_chapter_by_name('A Long-expected Party')
        self.assertEqual(test_get_chapter_by_name['A Long-expected Party']['book'], '5cf5805fb53e011a64671582' )

if __name__ == '__main__':
    TestChapters.api_key = access_token
    unittest.main()
