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
    pass

def payment_fee_calc_after_studying(credit_type, college_enrollment, semesters):
    pass