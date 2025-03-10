import unittest
from Logic import payment_fee_calc_while_studying, ask_information, payment_fee_calc_after_studying

class TestLogic(unittest.TestCase):

    def test_normal_1_while_studying(self):
        # variables de prueba
        credit_type = 1
        college_enrollment = 10000000
        semesters = 10

        # ejecutar la función
        cuota = payment_fee_calc_while_studying(credit_type, college_enrollment, semesters)

        # resultado esperado
        
        expected = 694940.81

        # verificar el resultado
        self.assertAlmostEqual(cuota, expected, places=2)

    def test_normal_1_after_studying(self):
        # variables de prueba
        credit_type = 1
        college_enrollment = 10000000
        semesters = 10

        # ejecutar la función
        cuota = payment_fee_calc_after_studying(credit_type, college_enrollment, semesters)

        # resultado esperado
        
        expected = 1252587.96

        # verificar el resultado
        self.assertAlmostEqual(cuota, expected, places=2)

    def test_normal_2_while_studying(self):
        # variables de prueba
        credit_type = 2
        college_enrollment = 10500000
        semesters = 9

        # ejecutar la función
        cuota = payment_fee_calc_while_studying(credit_type, college_enrollment, semesters)

        # resultado esperado
        
        expected = 5647814.78

        # verificar el resultado
        self.assertAlmostEqual(cuota, expected, places=2)

  


if __name__ == '__main__':
    unittest.main()