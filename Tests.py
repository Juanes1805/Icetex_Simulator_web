import unittest
from Logic import *

class TestLogic(unittest.TestCase):
    def test_normal_1(self):
        self.assertEqual(payment_fee_calc_while_studying(), 0)


if __name__ == '__main__':
    unittest.main()