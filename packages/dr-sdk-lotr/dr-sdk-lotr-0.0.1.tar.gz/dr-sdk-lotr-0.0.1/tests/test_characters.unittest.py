import unittest
import os
import sys
sys.path.insert(0, os.path.abspath( os.path.join(os.path.dirname(__file__),
                                               '../src/') ))
from dr_sdk_lotr.characters import Characters
from config import access_token


class TestCharacters(unittest.TestCase):

    def test_get_characters(self):
        characters = Characters(self.api_key)
        test_get_characters = characters.get_all_characters()
        self.assertEqual(len(test_get_characters), 933)

    def test_get_character_by_id(self):
        characters = Characters(self.api_key)
        test_get_character_by_id = characters.get_character_by_id('5cd99d4bde30eff6ebccfbed')
        self.assertEqual(test_get_character_by_id['name'], "Aranuir")
        self.assertEqual(test_get_character_by_id['race'], "Human")
        self.assertEqual(test_get_character_by_id['_id'], "5cd99d4bde30eff6ebccfbed")

    def test_get_quotes_by_character_id(self):
        characters = Characters(self.api_key)
        test_get_quotes_by_character_id = characters.get_quotes_by_character_id('5cdbdf477ed9587226e7949b')
        self.assertEqual(test_get_quotes_by_character_id[1]['dialog'], "Faramir! Orcs have taken the eastern shore. Their numbers are too great. By nightfall we will be overrun.")
        self.assertEqual(len(test_get_quotes_by_character_id), 7)

    def test_get_character_by_name(self):
        characters = Characters(self.api_key)
        test_get_character_by_name = characters.get_character_by_name('Gandalf')
        self.assertEqual(test_get_character_by_name['name'], 'Gandalf')
        

if __name__ == '__main__':
    TestCharacters.api_key = access_token
    unittest.main()
