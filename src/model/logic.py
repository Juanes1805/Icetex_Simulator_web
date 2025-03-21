"""This module contains the logic of the application."""
import sys
from model.exception import CreditTypeError, CollegeEnrollmentError, SemestersError
sys.path.append("src")


MEDIUM_TERM_CREDIT_INTEREST_RATE_30 = 0.0115 #1,15% month expired
MEDIUM_TERM_CREDIT_INTEREST_RATE_60 = 0.099 #0,99% month expired
SHORT_TERM_CREDIT_INTEREST_RATE_100 = 0.099 #0,99% month expired


def ask_information():
    """Ask the user for the information needed to calculate the payment fee."""
    while True:
        credit_type = input("Enter the type of credit you want \n 1 for 30%\n 2 for 60%\n"
        " 3 for 100%\n")
        list_options = ["1", "2", "3"]
        if credit_type in list_options:
            credit_type = int(credit_type)  # We convert to integer after validating the input
            break
        print("Invalid option. Please enter 1, 2, or 3.")

    while True:
        try:
            college_enrollment = float(input("Enter the amount of college enrollment per"
            " semester: "))
            if college_enrollment > 0:  # We make ensure it is a positive number
                break
            else:
                print("Invalid amount. Please enter a positive number.")
        except ValueError:
            print("Invalid option. Please enter a valid number.")

    while True:
        try:
            semesters = int(input("Enter the number of semesters you want to calculate for: "))
            if semesters > 0:  # We ensure that the number of semesters is positive
                break
            else:
                print("Invalid number of semesters. Please enter a positive integer.")
        except ValueError:
            print("Invalid option. Please enter a valid integer.")

    return credit_type, college_enrollment, semesters


def payment_fee_calc_while_studying(credit_type, college_enrollment, semesters):
    """Calculate the payment fee while the student is studying."""
    if credit_type == 1:
        if college_enrollment <= 0:
            raise CollegeEnrollmentError()
        if semesters <= 0 or isinstance(semesters, float):
            raise SemestersError()
        payment_fee = (
            0.3 * college_enrollment * semesters * MEDIUM_TERM_CREDIT_INTEREST_RATE_30
        ) / (
            1 - (1 + MEDIUM_TERM_CREDIT_INTEREST_RATE_30)**(-1 * (semesters/2) * 12)
        )
    elif credit_type == 2:
        if college_enrollment <= 0:
            raise CollegeEnrollmentError()
        if semesters <= 0 or isinstance(semesters, float):
            raise SemestersError()
        payment_fee = (
            0.6 * college_enrollment * semesters * MEDIUM_TERM_CREDIT_INTEREST_RATE_60
        ) / (
            1 - (1 + MEDIUM_TERM_CREDIT_INTEREST_RATE_60)**(-1 * (semesters/2) * 12)
        )
    elif credit_type == 3:
        if college_enrollment <= 0:
            raise CollegeEnrollmentError()
        if semesters <= 0 or isinstance(semesters, float):
            raise SemestersError()
        payment_fee = (
            college_enrollment * semesters * SHORT_TERM_CREDIT_INTEREST_RATE_100
        ) / (
            1 - (1 + SHORT_TERM_CREDIT_INTEREST_RATE_100)**(-1 * (semesters/2) * 12)
        )
    else:
        raise CreditTypeError()
    return payment_fee

def payment_fee_calc_after_studying(credit_type, college_enrollment, semesters):
    """Calculate the payment fee after the student has finished studying."""
    if credit_type == 1:
        if college_enrollment <= 0:
            raise CollegeEnrollmentError()
        if semesters <= 0 or isinstance(semesters, float):
            raise SemestersError()
        payment_fee = (
            0.7 * college_enrollment * semesters * MEDIUM_TERM_CREDIT_INTEREST_RATE_30
        ) / (
            1 - (1 + MEDIUM_TERM_CREDIT_INTEREST_RATE_30)**(-1.5 * (semesters/2) * 12)
        )
    elif credit_type == 2:
        if college_enrollment <= 0:
            raise CollegeEnrollmentError()
        if semesters <= 0 or isinstance(semesters, float):
            raise SemestersError()
        payment_fee = (
            0.4 * college_enrollment * semesters * MEDIUM_TERM_CREDIT_INTEREST_RATE_60
        ) / (
            1 - (1 + MEDIUM_TERM_CREDIT_INTEREST_RATE_60)**(-1.5 * (semesters/2) * 12)
        )
    elif credit_type == 3:
        return None
    else:
        raise CreditTypeError()
    return payment_fee
