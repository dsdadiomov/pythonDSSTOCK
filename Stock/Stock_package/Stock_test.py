import unittest
from Stock import *

class TestStock(unittest.TestCase):
    def test_stock_price(self):
        self.assertEqual(stock_price('TSLA'),1004.29)  # add assertion here


if __name__ == '__main__':
    unittest.main()
