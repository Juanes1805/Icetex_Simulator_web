"""This module contains the logic of the application."""
import sys
from model.exception import CreditTypeError, CollegeEnrollmentError, SemestersError
sys.path.append("src")


MEDIUM_TERM_CREDIT_INTEREST_RATE_30 = 0.0115 #1,15% month expired
MEDIUM_TERM_CREDIT_INTEREST_RATE_60 = 0.099 #0,99% month expired
SHORT_TERM_CREDIT_INTEREST_RATE_100 = 0.099 #0,99% month expired

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
