import unittest
from format_price import format_price




class PriceFormatingTestCase(unittest.TestCase):
    def testInt(self):
        self.assertEqual(format_price(1234567890), '1 234 567 890')


    def testFloat(self):
        self.assertEqual(format_price(1235.024), '1 235.02')
        self.assertEqual(format_price(1235.026), '1 235.03')


    def testStr(self):
        self.assertEqual(format_price('12345.877'), '12 345.88')
        self.assertEqual(format_price('77777,77'), '77 777.77')
        self.assertEqual(format_price('9.999'), '9.99')


if __name__=='__main__':
    unittest.main()