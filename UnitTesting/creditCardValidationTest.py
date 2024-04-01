import unittest
from creditCardValidation import *

class CreditCardValidationTest(unittest.TestCase):

    def setUp(self):
        print("Setup Method")

    def test_validateCard_valid(self):
        res = validateCard((date(2025,3,31)))
        self.assertEqual('Valid',res)

    def test_validateCard_expired(self):
        with self.assertRaises(RuntimeError):
            validateCard((date(2013, 3, 31)))

        #res = validateCard((date(2013,3,31)))
        #self.assertEqual('Expired',res)

    def tearDown(self):
        print("TearDown")

if __name__ == '__main__':
    unittest.main()
