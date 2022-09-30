import unittest
from translator import french_to_english, english_to_french

class E2FTest(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french(' '), ' ')
        self.assertNotEqual(english_to_french('Hello'), 'Hola')

class F2ETest(unittest.TestCase):
    def test_french_to_english(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english(' '), ' ')
        self.assertNotEqual(french_to_english('Bonjour'), 'Ciao')

unittest.main()