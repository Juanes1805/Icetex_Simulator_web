import unittest
from Logic import payment_fee_calc_while_studying, ask_information, payment_fee_calc_after_studying

class TestLogic(unittest.TestCase):

    def test_normal_1(self):
        cuota = payment_fee_calc_while_studying(1, 10000000, 10)
        self.assertAlmostEqual(cuota, 69494.08, places=2) 

if __name__ == '__main__':
    unittest.main()