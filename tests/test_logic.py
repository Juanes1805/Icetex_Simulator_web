import unittest
import sys
sys.path.append("src")
from model.logic import payment_fee_calc_while_studying, ask_information, payment_fee_calc_after_studying
from model.exception import CollegeEnrollmentError, SemestersError, CreditTypeError

class TestLogic(unittest.TestCase):
    def test_normal_1_while_studying(self):
        # test variables
        credit_type = 1
        college_enrollment = 10000000
        semesters = 10

        # execute the function
        cuota = payment_fee_calc_while_studying(credit_type, college_enrollment, semesters)

        # expected result
        expected = 694940.81

        # verify the result
        self.assertAlmostEqual(cuota, expected, places=2)

    def test_normal_1_after_studying(self):
        # test variables
        credit_type = 1
        college_enrollment = 10000000
        semesters = 10

        # execute the function
        cuota = payment_fee_calc_after_studying(credit_type, college_enrollment, semesters)

        # expected result
        expected = 1252587.96

        # verify the result
        self.assertAlmostEqual(cuota, expected, places=2)

    def test_normal_2_while_studying(self):
        # test variables
        credit_type = 2
        college_enrollment = 10500000
        semesters = 9

        # execute the function
        cuota = payment_fee_calc_while_studying(credit_type, college_enrollment, semesters)

        # expected result
        expected = 5647814.78

        # verify the result
        self.assertAlmostEqual(cuota, expected, places=2)

    def test_normal_2_after_studying(self):
        # test variables
        credit_type = 2
        college_enrollment = 10500000
        semesters = 9

        # execute the function
        cuota = payment_fee_calc_after_studying(credit_type, college_enrollment, semesters)

        # expected result
        expected = 3743988.63

        # verify the result
        self.assertAlmostEqual(cuota, expected, places=2)

    def test_normal_3_while_studying(self):
        # test variables
        credit_type = 2
        college_enrollment = 9000000
        semesters = 9

        # execute the function
        cuota = payment_fee_calc_while_studying(credit_type, college_enrollment, semesters)

        # expected result
        expected = 4840984.09

        # verify the result
        self.assertAlmostEqual(cuota, expected, places=2)

    def test_normal_3_after_studying(self):
        # test variables
        credit_type = 2
        college_enrollment = 9000000
        semesters = 9

        # execute the function
        cuota = payment_fee_calc_after_studying(credit_type, college_enrollment, semesters)

        # expected result
        expected = 3209133.11

        # verify the result
        self.assertAlmostEqual(cuota, expected, places=2)

    def test_extraordinary_1_while_studying(self):
        # test variables
        credit_type = 1
        college_enrollment = 11500000
        semesters = 1

        # execute the function
        cuota = payment_fee_calc_while_studying(credit_type, college_enrollment, semesters)

        # expected result
        expected = 598364.26

        # verify the result
        self.assertAlmostEqual(cuota, expected, places=2)

    def test_extraordinary_1_after_studying(self):
        # test variables
        credit_type = 1
        college_enrollment = 11500000
        semesters = 1

        # execute the function
        cuota = payment_fee_calc_after_studying(credit_type, college_enrollment, semesters)

        # expected result
        expected = 946658.96

        # verify the result
        self.assertAlmostEqual(cuota, expected, places=2)

    def test_extraordinary_2_while_studying(self):
        # test variables
        credit_type = 3
        college_enrollment = 12000000
        semesters = 10

        # execute the function
        cuota = payment_fee_calc_while_studying(credit_type, college_enrollment, semesters)

        # expected result
        expected = 11921348.89

        # verify the result
        self.assertAlmostEqual(cuota, expected, places=2)

    def test_extraordinary_2_after_studying(self):
        # test variables
        credit_type = 3
        college_enrollment = 11500000
        semesters = 1

        # execute the function
        cuota = payment_fee_calc_after_studying(credit_type, college_enrollment, semesters)

        # expected result
        expected = None

        # verify the result
        self.assertAlmostEqual(cuota, expected, places=2)

    def test_extraordinary_3_while_studying(self):
        # test variables
        credit_type = 3
        college_enrollment = 15000000
        semesters = 10

        # execute the function
        cuota = payment_fee_calc_while_studying(credit_type, college_enrollment, semesters)

        # expected result
        expected = 14901686.11

        # verify the result
        self.assertAlmostEqual(cuota, expected, places=2)

    def test_extraordinary_3_after_studying(self):
        # test variables
        credit_type = 3
        college_enrollment = 15000000
        semesters = 10

        # execute the function
        cuota = payment_fee_calc_after_studying(credit_type, college_enrollment, semesters)

        # expected result
        expected = None

        # verify the result
        self.assertAlmostEqual(cuota, expected, places=2)

    def test_error_1(self):
        # test variables
        credit_type = 1
        college_enrollment = 0 # invalid enrollment amount
        semesters = 6

        # verify that an exception is raised
        with self.assertRaises(CollegeEnrollmentError):
            payment_fee_calc_while_studying(credit_type, college_enrollment, semesters)

    def test_error_2(self):
        # test variables
        credit_type = 2
        college_enrollment = 9750000
        semesters = 0 # invalid number of semesters

        # verify that an exception is raised
        with self.assertRaises(SemestersError):
            payment_fee_calc_while_studying(credit_type, college_enrollment, semesters)

    def test_error_3(self):
        # test variables
        credit_type = 2
        college_enrollment = 9750000
        semesters = 11.4 # invalid number of semesters

        # verify that an exception is raised
        with self.assertRaises(SemestersError):
            payment_fee_calc_while_studying(credit_type, college_enrollment, semesters)

    def test_error_4(self):
        # test variables
        credit_type = 0 # invalid credit type
        college_enrollment = 24000000
        semesters = 12

        # verify that an exception is raised
        with self.assertRaises(CreditTypeError):
            payment_fee_calc_while_studying(credit_type, college_enrollment, semesters)

if __name__ == '__main__':
    unittest.main()