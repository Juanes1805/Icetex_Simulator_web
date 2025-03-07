while True:
    credit_type = input("Enter the type of credit you want \n 1 for 30%\n 2 for 60%\n 3 for 100%\n")
    
    if credit_type in {"1", "2", "3"}:
        credit_type = int(credit_type)  # Convertimos a entero después de validar
        break
    print("Invalid option. Please enter 1, 2, or 3.")

while True:
    try:
        college_enrollment = float(input("Enter the amount of college enrollment per semester: "))
        if college_enrollment > 0:  # Aseguramos que sea un número positivo
            break
        else:
            print("Invalid amount. Please enter a positive number.")
    except ValueError:
        print("Invalid option. Please enter a valid number.")

while True:
    try:
        semesters = int(input("Enter the number of semesters you want to calculate for: "))
        if semesters > 0:  # Aseguramos que el número de semestres sea positivo
            break
        else:
            print("Invalid number of semesters. Please enter a positive integer.")
    except ValueError:
        print("Invalid option. Please enter a valid integer.")


def payment_fee_calc_while_studying(credit_type, college_enrollment, semesters):
    if credit_type == 1:
        payment_fee =  (0.3 * college_enrollment * 0.0115) / (1 - (1 + 0.0115)**(-1.5 * (semesters/2) * 12))
    elif credit_type == 2:
        payment_fee =  (0.6 * college_enrollment * 0.0115) / (1 - (1 + 0.0115)**(-1.5 * (semesters/2) * 12))
    else:
        payment_fee = (college_enrollment * 0.0115) / (1 - (1 + 0.0115)**(-1.5 * (semesters/2) * 12))
    return payment_fee

def payment_fee_calc_after_studying(credit_type, college_enrollment, semesters):
    if credit_type == 1:
        payment_fee =  (0.7 * college_enrollment * 0.0115) / (1 - (1 + 0.0115)**(-1.5 * (semesters/2) * 12))
    elif credit_type == 2:
        payment_fee =  (0.4 * college_enrollment * 0.0115) / (1 - (1 + 0.0115)**(-1.5 * (semesters/2) * 12))
    else:
        return None
    return payment_fee