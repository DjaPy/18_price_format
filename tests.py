import unittest
from format_price import format_price


class PriceFormatingTestCase(unittest.TestCase):


    def setUp(self):
        self.test_list = [1, 2]
        self.test_dict = {1: 2, 2: 3}
        self.test_tuple = (1, 2, 3)
        self.test_set = {1, 2, 3, 4}
        self.num_complex = (2 + 3j)
        self.num_negative = -3
        self.fractional_more_three = '1245.5844'
        self.n = None


    def testInt(self):
        self.assertEqual(format_price(1234567890), '1 234 567 890')


    def testFloat(self):
        self.assertEqual(format_price(1235.024), '1 235.02')
        self.assertEqual(format_price(1235.026), '1 235.03')


    def testStr(self):
        self.assertEqual(format_price('12345.877'), '12 345.88')
        self.assertEqual(format_price('77777,77'), '77 777.77')
        self.assertEqual(format_price('9.999'), '9.99')


    def testAnyData(self):
        def test_func():
            pass
        self.assertEqual(format_price(self.test_list), TypeError)
        self.assertEqual(format_price(self.num_complex), TypeError)
        self.assertEqual(format_price(self.test_dict), TypeError)
        self.assertEqual(format_price(self.test_tuple), TypeError)
        self.assertEqual(format_price(test_func()), TypeError)
        self.assertEqual(format_price(self.test_set),TypeError)
        self.assertEqual(format_price(self.num_negative),ValueError)
        self.assertEqual(format_price(self.fractional_more_three), ValueError)
        self.assertEqual(format_price(self.n), TypeError)



if __name__=='__main__':
    unittest.main()