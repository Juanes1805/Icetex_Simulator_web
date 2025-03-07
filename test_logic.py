import unittest
from Logic import payment_fee_calc_while_studying 

class TestLogic(unittest.TestCase):

    def test_normal_1(self):
        cuota = payment_fee_calc_while_studying(1, 10000000, 10)
        self.assertEqual(cuota, 53682.34) 

if __name__ == '__main__':
    unittest.main()