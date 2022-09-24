import unittest
import translator 
englishToFrench = translator.englishToFrench
frenchToEnglish = translator.frenchToEnglish
class TestStringMethods(unittest.TestCase):

    def test_null(self):
        self.assertEqual(englishToFrench(''), "")
        self.assertEqual(frenchToEnglish(''), '')


    def test_hello_tr(self):
        self.assertEqual(englishToFrench('hello'), '"Bonjour"')
        self.assertEqual(frenchToEnglish('Bonjour'), '"Hello"')

if __name__ == '__main__':
    unittest.main()