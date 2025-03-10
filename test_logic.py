import unittest
from Logic import payment_fee_calc_while_studying, ask_information, payment_fee_calc_after_studying
from exceptions import CollegeEnrollmentError, SemestersError, CreditTypeError

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

    def test_normal_2_after_studying(self):
        # variables de prueba
        credit_type = 2
        college_enrollment = 10500000
        semesters = 9

        # ejecutar la función
        cuota = payment_fee_calc_after_studying(credit_type, college_enrollment, semesters)

        # resultado esperado
        
        expected = 3743988.63


        # verificar el resultado
        self.assertAlmostEqual(cuota, expected, places=2)

    def test_normal_3_while_studying(self):
        # variables de prueba
        credit_type = 2
        college_enrollment = 9000000
        semesters = 9

        # ejecutar la función
        cuota = payment_fee_calc_while_studying(credit_type, college_enrollment, semesters)

        # resultado esperado
        
        expected = 4840984.09

        # verificar el resultado
        self.assertAlmostEqual(cuota, expected, places=2)


    def test_normal_3_after_studying(self):
        # variables de prueba
        credit_type = 2
        college_enrollment = 9000000
        semesters = 9

        # ejecutar la función
        cuota = payment_fee_calc_after_studying(credit_type, college_enrollment, semesters)

        # resultado esperado
        
        expected = 3209133.11


        # verificar el resultado
        self.assertAlmostEqual(cuota, expected, places=2)

    def test_extraordinary_1_while_studying(self):
        # variables de prueba
        credit_type = 1
        college_enrollment = 11500000
        semesters = 1

        # ejecutar la función
        cuota = payment_fee_calc_while_studying(credit_type, college_enrollment, semesters)

        # resultado esperado
        
        expected = 598364.26

        # verificar el resultado
        self.assertAlmostEqual(cuota, expected, places=2)

    def test_extraordinary_1_after_studying(self):
        # variables de prueba
        credit_type = 1
        college_enrollment = 11500000
        semesters = 1

        # ejecutar la función
        cuota = payment_fee_calc_after_studying(credit_type, college_enrollment, semesters)

        # resultado esperado
        
        expected = 946658.96

        # verificar el resultado
        self.assertAlmostEqual(cuota, expected, places=2)

    def test_extraordinary_2_while_studying(self):
        # variables de prueba
        credit_type = 3
        college_enrollment = 12000000
        semesters = 10

        # ejecutar la función
        cuota = payment_fee_calc_while_studying(credit_type, college_enrollment, semesters)

        # resultado esperado
        
        expected = 11921348.89

        # verificar el resultado
        self.assertAlmostEqual(cuota, expected, places=2)

    def test_extraordinary_2_after_studying(self):
        # variables de prueba
        credit_type = 3
        college_enrollment = 11500000
        semesters = 1

        # ejecutar la función
        cuota = payment_fee_calc_after_studying(credit_type, college_enrollment, semesters)

        # resultado esperado
        
        expected = None

        # verificar el resultado
        self.assertAlmostEqual(cuota, expected, places=2)

    def test_extraordinary_3_while_studying(self):
        # variables de prueba
        credit_type = 3
        college_enrollment = 15000000
        semesters = 10

        # ejecutar la función
        cuota = payment_fee_calc_while_studying(credit_type, college_enrollment, semesters)

        # resultado esperado
        
        expected = 14901686.11

        # verificar el resultado
        self.assertAlmostEqual(cuota, expected, places=2)

    def test_extraordinary_3_after_studying(self):
        # variables de prueba
        credit_type = 3
        college_enrollment = 15000000
        semesters = 10

        # ejecutar la función
        cuota = payment_fee_calc_after_studying(credit_type, college_enrollment, semesters)

        # resultado esperado
        
        expected = None

        # verificar el resultado
        self.assertAlmostEqual(cuota, expected, places=2)   

    def test_error_1(self):
        # variables de prueba
        credit_type = 1
        college_enrollment = 0 # monto de matrícula inválido
        semesters = 6

        # verificar que lanza una excepción
        with self.assertRaises(CollegeEnrollmentError):
            payment_fee_calc_while_studying(credit_type, college_enrollment, semesters)

    def test_error_2(self):
        # variables de prueba
        credit_type = 2
        college_enrollment = 9750000
        semesters = 0 # número de semestres inválido

        # verificar que lanza una excepción
        with self.assertRaises(SemestersError):
            payment_fee_calc_while_studying(credit_type, college_enrollment, semesters)

    def test_error_3(self):
        # variables de prueba
        credit_type = 2
        college_enrollment = 9750000
        semesters = 11.4 # número de semestres inválido

        # verificar que lanza una excepción
        with self.assertRaises(SemestersError):
            payment_fee_calc_while_studying(credit_type, college_enrollment, semesters)

    def test_error_4(self):
        # variables de prueba
        credit_type = 0 # tipo de crédito inválido
        college_enrollment = 24000000
        semesters = 12

        # verificar que lanza una excepción
        with self.assertRaises(CreditTypeError):
            payment_fee_calc_while_studying(credit_type, college_enrollment, semesters)
   

if __name__ == '__main__':
    unittest.main()