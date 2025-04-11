"""This module contains the custom exceptions for the model module."""
class CollegeEnrollmentError(Exception):
    """Exception raised for errors in the college enrollment amount."""
    def __init__(self, message="Invalid college enrollment"):
        self.message = message

        super().__init__(self.message)

class CollegeEnrollmentMenorThanZeroError(Exception):
    """Exception raised for errors in the college enrollment amount."""
    def __init__(self, message="College enrollment cannot be less than zero."):
        self.message = message 

        super().__init__(self.message)

class SemestersError(Exception):
    """Exception raised for errors in the number of semesters."""
    def __init__(self, message="Invalid number of semesters"):
        self.message = message

        super().__init__(self.message)

class CreditTypeError(Exception):
    """Exception raised for errors in the credit type."""
    def __init__(self, message="Invalid credit type"):
        self.message = message

        super().__init__(self.message)

class NotPressBottonError(Exception):
    def __init__(self, message="Not press botton of credit type."):
        self.message = message
        
class NotCollegeEnrollmentError(Exception):
    """Exception raised for errors in the college enrollment amount."""
    def __init__(self, message="Invalid college enrollment"):
        self.message = message

        super().__init__(self.message)