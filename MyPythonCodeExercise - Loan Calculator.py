##################################
"""
Practice Python Scripts
Loan Calculator

Created by: Nowell Angelo S. Tiongco

History (latest on top):
2025-08-17  TODO:   Add error handling in input
2025-08-09          Changed loan_amount datatype to float
                    Changed loan_term to number of months instead of years
                    Changed interest_rate datatype to float
2025-08-06  Initial Creation
"""
##################################

import math
import pandas as pd

print()
print("-------------------------------------------------------")
print()
print("Practice Python Scripts")
print("Loan Calculator")
print()
print("Created by: Nowell Angelo S. Tiongco")
print()
print("-------------------------------------------------------")
print()

loan_amount = float(input("Loan Amount: "))
loan_term = int(input("Loan Term (months): "))
interest_rate = float(input("Interest Rate (percentage): "))
print()

class LoanCalculator:
    def __init__(self, loan_amount, loan_term, interest_rate):
        self.loan_amount = loan_amount
        self.loan_term = loan_term
        self.interest_rate = interest_rate
    def define(self):
        print("Loan Amount: ", self.loan_amount)
        print("Loan Term (months): ", self.loan_term)
        print("Interest Rate (percentage)): ", self.interest_rate)
    def monthly_amortization(self):
        P = self.loan_amount
        r = self.interest_rate / 100
        #n = self.loan_term * 12
        n = self.loan_term
        i = r / 12
        A = P * (i / (1 - math.pow(1 + i, -n)))
        return A
    def amortization_schedule(self):
        balance = self.loan_amount
        monthly_payment = self.monthly_amortization()
        r = self.interest_rate / 100
        i = r / 12
        #n = self.loan_term * 12
        n = self.loan_term
        total_payment = 0
        total_interest = 0
        total_principal = 0
        print(f"{'Month':<6}{'Payment':>18}{'Principal':>18}{'Interest':>18}{'Balance':>20}")
        for month in range(1, n + 1):
            interest_payment = balance * i
            principal_payment = monthly_payment - interest_payment
            balance -= principal_payment
            print(f"{month:<6}{monthly_payment:>18,.2f}{principal_payment:>18,.2f}{interest_payment:>18,.2f}{balance:>20,.2f}")
            total_payment = total_payment + monthly_payment
            total_interest = total_interest + interest_payment
            total_principal = total_principal + principal_payment
        print(f"{'':6}{'Total Payment':>18}{'Total Principal':>18}{'Total Interest':>20}")
        print(f"{'':6}{total_payment:>18,.2f}{total_principal:>18,.2f}{total_interest:>20,.2f}")

# Create an instance of LoanCalculator
loan = LoanCalculator(loan_amount, loan_term, interest_rate)

# define method
# loan.define()
# print()

print("-------------------------------------------------------")
print()

# monthly_amortization method
monthly_amortization=loan.monthly_amortization()
print(f"Monthly Amortization: {monthly_amortization:,.2f}")
print()

# amortization_schedule method
loan.amortization_schedule()

print("-------------------------------------------------------")
print()

input("Press Enter to exit...")
