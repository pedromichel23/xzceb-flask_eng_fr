import unittest
#from machinetranslation.translator import english_to_french, french_to_english
#from machinetranslation.translator import english_to_french, french_to_english
from translator import english_to_french, french_to_english
#import machinetranslation.translator


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
        expected = "Type a text in English"
        self.assertEqual(english_to_french(test_case), expected)

    def test_FrenchToEnglish_null(self):
        test_case = None
        expected = "Type a text in French"
        self.assertEqual(french_to_english(test_case), expected)


if __name__ == '__main__':
    unittest.main()
    