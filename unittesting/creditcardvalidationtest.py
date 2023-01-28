import unittest
from creditcardvalidation import *


class CreditCardValidationTest(unittest.TestCase):
    def setUp(self):
        print('setup')

    def test_validateCard_valid(self):
        result = validateCard(date(2024,2,2))
        self.assertEqual('valid', result)

    """def test_validateCard_expired(self):
        result = validateCard(date(2020,2,2))
        self.assertEqual('expired', result)"""

    def test_validateCard_expired(self):
        with self.assertRaises(RuntimeError):
            validateCard(date(2022,2,2))

    def tearDown(self):
        print("tear down")


if __name__ == '__main__':
    unittest.main()

