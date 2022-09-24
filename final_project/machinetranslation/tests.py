import unittest
import translator 
englishToFrench = translator.englishToFrench
frenchToEnglish = translator.frenchToEnglish
class TestStringMethods(unittest.TestCase):

    def test_null(self):
        self.assertEqual(englishToFrench(null), null)
        self.assertEqual(frenchToEnglish(null), null)


    def test_hello_tr(self):
        self.assertEqual(englishToFrench('hello'), 'Bonjour')
        self.assertEqual(frenchToEnglish('Bonjour'), 'hello')

if __name__ == '__main__':
    unittest.main()