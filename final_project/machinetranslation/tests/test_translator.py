import os, sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import unittest
from translator import english_to_french, french_to_english

class TestMain(unittest.TestCase):

    def test_EnglishToFrench(self):
        test_case = "Hello"
        expected = "Bonjour"        
        self.assertEqual(english_to_french(test_case), expected)

    def test_FrenchToEnglish(self):
        test_case = "Bonjour"
        expected = "Hello"        
        self.assertEqual(french_to_english(test_case), expected)

    def test_EnglishToFrench_null(self):
        test_case = None
        not_expected = None
        self.assertNotEqual(english_to_french(test_case), not_expected)

    def test_FrenchToEnglish_null(self):
        test_case = None
        not_expected = None
        self.assertNotEqual(french_to_english(test_case), not_expected)


if __name__ == '__main__':
    unittest.main()
    