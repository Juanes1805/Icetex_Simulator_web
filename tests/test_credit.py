import unittest
from decimal import Decimal

import sys
sys.path.append("src")

from model.credit import Credit
from controller.credits_controller import CreditsController

class TestCredit(unittest.TestCase):
    """Test the CreditsController class."""

    # Test Fixture
    def setUp(self):
        """Set up the test case."""
        controller = CreditsController()
        controller.delete_table()
        controller.create_table()

    def test_insert_1(self):
        credit = Credit(
            credit_id="1",
            college_enrollment=10000000,
            semesters=10,
            credit_type="30%",
            payment_fee_while_studying=694940.81,
            payment_fee_after_studying=1252587.96
        )

        controller = CreditsController()
        controller.insert_credit(credit)

        credit_searched = controller.search_credit(credit.credit_id)

        credit.isEqual(credit_searched)

    def test_insert_2(self):
        credit = Credit(
            credit_id="2",
            college_enrollment=10500000,
            semesters=9,
            credit_type="60%",
            payment_fee_while_studying=5647814.78,
            payment_fee_after_studying=3743988.63
        )

        controller = CreditsController()
        controller.insert_credit(credit)

        credit_searched = controller.search_credit(credit.credit_id)

        credit.isEqual(credit_searched)

    def test_insert_3(self):
        credit = Credit(
            credit_id="3",
            college_enrollment=9000000,
            semesters=9,
            credit_type="60%",
            payment_fee_while_studying=4840984.09,
            payment_fee_after_studying=3209133.11
        )

        controller = CreditsController()
        controller.insert_credit(credit)

        credit_searched = controller.search_credit(credit.credit_id)

        credit.isEqual(credit_searched)

    def test_update_1(self):
        credit = Credit(
            credit_id="1",
            college_enrollment=10000000,
            semesters=10,
            credit_type="30%",
            payment_fee_while_studying=673995.60,
            payment_fee_after_studying=1199626.39
        )

        controller = CreditsController()
        controller.insert_credit(credit)

        credit.semesters = 9
        credit.payment_fee_while_studying = Decimal(1234567.89)
        credit.payment_fee_after_studying = Decimal(9876543.21)
        controller.update_credit(credit)

        credit_searched = controller.search_credit(credit.credit_id)

        credit.isEqual(credit_searched)

    def test_update_2(self):
        credit = Credit(
            credit_id="2",
            college_enrollment=10500000,
            semesters=9,
            credit_type="60%",
            payment_fee_while_studying=5647814.78,
            payment_fee_after_studying=3743988.63
        )

        controller = CreditsController()
        controller.insert_credit(credit)

        credit.college_enrollment = 11000000
        credit.payment_fee_while_studying = Decimal(5916758.34)
        credit.payment_fee_after_studying = Decimal(3922273.81)
        controller.update_credit(credit)

        credit_searched = controller.search_credit(credit.credit_id)

        credit.isEqual(credit_searched)

    def test_update_3(self):
        credit = Credit(
            credit_id="3",
            college_enrollment=9000000,
            semesters=9,
            credit_type="60%",
            payment_fee_while_studying=4840984.09,
            payment_fee_after_studying=3209133.11
        )

        controller = CreditsController()
        controller.insert_credit(credit)

        credit.credit_type = "30%"
        credit.payment_fee_while_studying = Decimal(606596.04)
        credit.payment_fee_after_studying = Decimal(1079663.75)
        controller.update_credit(credit)

        credit_searched = controller.search_credit(credit.credit_id)

        credit.isEqual(credit_searched)

    def test_search_1(self):
        credit = Credit(
            credit_id="1",
            college_enrollment=10000000,
            semesters=9,
            credit_type="30%",
            payment_fee_while_studying=1234567.89,
            payment_fee_after_studying=9876543.21
        )

        controller = CreditsController()
        controller.insert_credit(credit)

        credit_searched = controller.search_credit(credit.credit_id)

        credit.isEqual(credit_searched)

    def test_search_2(self):
        credit = Credit(
            credit_id="2",
            college_enrollment=11000000,
            semesters=9,
            credit_type="60%",
            payment_fee_while_studying=5916758.34,
            payment_fee_after_studying=3743988.63
        )

        controller = CreditsController()
        controller.insert_credit(credit)

        credit_searched = controller.search_credit(credit.credit_id)

        credit.isEqual(credit_searched)

    def test_search_3(self):
        credit = Credit(
            credit_id="3",
            college_enrollment=15000000,
            semesters=10,
            credit_type="100%",
            payment_fee_while_studying=14901686.11,
            payment_fee_after_studying=None
        )

        controller = CreditsController()
        controller.insert_credit(credit)

        credit_searched = controller.search_credit(credit.credit_id)

        credit.isEqual(credit_searched)


if __name__ == "__main__":
    unittest.main()
