"""
HANDIN 1:

This handin is done by:

    201807850 (Jens Trolle)
    201806389 (Mike Pedersen)
    201805266 (Frederik Thaibert)

Reflection upon solution:

We started the handin by simply letting the user input values for the loan,
interest and payment - and then using the while loop at the bottom. An issue
we didn't see coming, was the fact that the monthly payment has to be larger
than the loan times the interest rate - we fixed this in the while loop which
checks for this condition. We also implemented a check for loans and payments
equal to or below 0. The final while loop prints the time and what's left in
the balance at that time. By using 'i += 1' we increase the value of the time
by 1 after every loop. We haven't taken into account the possibility of the
user inputting a string into the the values of loan_input, monthly_percent and
monthly_payment.

"""


# User inputs.

loan_input = float(input("Initial loan: "))
monthly_percent = float(input("Monthly interest rate in percent: "))
monthly_payment = float(input("Monthly payment: "))

# Turn interest in percent to float - calculation for later test.

monthly_interest = monthly_percent / 100
test = monthly_interest * loan_input

# Check for loan below 0.

while loan_input < 0:
    print("Your loan cannot be below 0.")
    loan_input = float(input("Initial loan: "))

# Check for monthly payment below 0.

while monthly_payment < 0:
    print("Your monthly payment cannot below 0.")
    monthly_p = float(input("Monthly payment: "))

# Check for monthly payment below increase in balance per year.

while monthly_payment <= test:
    print("Your monthly payment cannot be smaller than your "
          "input times the monthly interest rate in percent.")
    loan_input = float(input("Initial loan: "))
    monthly_p = float(input("Monthly payment: "))
    test = monthly_interest * loan_input

# Set balance equal to loan input.

balance = loan_input
i = 0

"""
Check for balance below 0. If true, our loan has been payed off.
Loop prints the year and remaining balance. Also sets i (current year) to 0.
"""

while balance > 0:
    print("This is the remaining size of the loan at month", i, ":", balance)
    balance = (balance * (1 + monthly_interest)) - monthly_payment
    i += 1

# Prints how many months it took to pay off the loan.
print("Your loan has been payed off. It took you", i, "months.")
