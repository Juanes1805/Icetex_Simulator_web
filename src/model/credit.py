class Credit:
    def __init__(self, credit_id: str, college_enrollment: float, semesters: int, credit_type: int, 
                 payment_fee_while_studying: float, payment_fee_after_studying: float):
        """
        Initialize a Credit object with the given parameters.
        """

        self.credit_id = credit_id
        self.college_enrollment = college_enrollment
        self.semesters = semesters
        self.credit_type = credit_type
        self.payment_fee_while_studying = payment_fee_while_studying
        self.payment_fee_after_studying = payment_fee_after_studying

    def isEqual(self, other) -> bool:
        """
        Check if two Credit objects are equal based on their attributes.
        """
        assert self.credit_id == other.credit_id, "Credit IDs do not match"
        assert self.college_enrollment == other.college_enrollment, "College enrollments do not match"
        assert self.semesters == other.semesters, "Semesters do not match"
        assert self.credit_type == other.credit_type, "Credit types do not match"
        assert self.payment_fee_while_studying == other.payment_fee_while_studying, "Payment fees while studying do not match"
        assert self.payment_fee_after_studying == other.payment_fee_after_studying, "Payment fees after studying do not match"

        return True