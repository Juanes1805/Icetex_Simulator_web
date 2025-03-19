class CollegeEnrollmentError(Exception):
    def __init__(self, message="Invalid college enrollment"):
        self.message = message

        super().__init__(self.message)

class SemestersError(Exception):
    def __init__(self, message="Invalid number of semesters"):
        self.message = message

        super().__init__(self.message)

class CreditTypeError(Exception):
    def __init__(self, message="Invalid credit type"):
        self.message = message

        super().__init__(self.message)
