from Logic import payment_fee_calc_while_studying, ask_information, payment_fee_calc_after_studying
def main():
    print("---- Welcome to the ICETEX simulator :p ----")
    while True:
        credit_type, college_enrollment, semesters = ask_information()
        fee_while_studying = payment_fee_calc_while_studying(credit_type, college_enrollment, semesters)
        print(f"Your monthly fee while studying is: {fee_while_studying}")
        fee_after_studying = payment_fee_calc_after_studying(credit_type, college_enrollment, semesters)
        print(f"Your monthly fee after studying is: {fee_after_studying}")

        if input("Do you want to calculate another fee? (yes/no): ").lower() != "yes":
            print("Thanks for using the ICETEX simulator. Goodbye!")   
            break

if __name__ == '__main__':
    main()

