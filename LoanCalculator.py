##################################
"""
Practice Python Scripts
Loan Calculator

Created by: Nowell Tiongco

History (latest on top):
2025-08-24          Export to Excel          
2025-08-17          Add error handling in input
2025-08-09          Changed loan_amount datatype to float
                    Changed loan_term to number of months instead of years
                    Changed interest_rate datatype to float
2025-08-06  Initial Creation
"""
##################################

import math
import pandas as pd
import os

print()
print("-------------------------------------------------------")
print()
print("Loan Calculator")
print()
print("Created by: github.com/nowell-dev")
print()
print("-------------------------------------------------------")
print()

while True:
    try:
        loan_amount = float(input("Loan Amount: "))
        break
    except ValueError:
        print("⚠️ Please enter a valid number.")
while True:
    try:
        loan_term = int(input("Loan Term (months): "))
        if loan_term < 1 or loan_term > 360:
            print("⚠️ Please enter a value between 1 and 360.")
            continue
        break
    except ValueError:
        print("⚠️ Please enter a valid whole number (months).")
while True:
    try:
        interest_rate = float(input("Interest Rate (percentage): "))
        break
    except ValueError:
        print("⚠️ Please enter a valid number.")
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
        n = self.loan_term
        i = r / 12
        A = P * (i / (1 - math.pow(1 + i, -n)))
        return A

    def amortization_schedule(self):
        balance = self.loan_amount
        monthly_payment = self.monthly_amortization()
        r = self.interest_rate / 100
        i = r / 12
        n = self.loan_term
        total_payment = 0
        total_interest = 0
        total_principal = 0

        # Store data for export
        schedule = []

        print(f"{'Month':<6}{'Payment':>18}{'Principal':>18}{'Interest':>18}{'Balance':>20}")
        for month in range(1, n + 1):
            interest_payment = balance * i
            principal_payment = monthly_payment - interest_payment
            balance -= principal_payment

            print(f"{month:<6}{monthly_payment:>18,.2f}{principal_payment:>18,.2f}{interest_payment:>18,.2f}{balance:>20,.2f}")
            schedule.append({"Month": month,"Payment": round(monthly_payment, 2),"Principal": round(principal_payment, 2),"Interest": round(interest_payment, 2),"Balance": round(balance, 2)})

            total_payment += monthly_payment
            total_interest += interest_payment
            total_principal += principal_payment

        print(f"{'':6}{'Total Payment':>18}{'Total Principal':>18}{'Total Interest':>20}")
        print(f"{'':6}{total_payment:>18,.2f}{total_principal:>18,.2f}{total_interest:>20,.2f}")
        # Add label row for totals
        schedule.append({"Month": "","Payment": "Total Payment","Principal": "Total Principal","Interest": "Total Interest","Balance": ""})
        # Add actual totals row
        schedule.append({"Month": "","Payment": round(total_payment, 2),"Principal": round(total_principal, 2),"Interest": round(total_interest, 2),"Balance": ""})

        return schedule

# Create an instance of LoanCalculator
loan = LoanCalculator(loan_amount, loan_term, interest_rate)

print("-------------------------------------------------------")
print()

# Compute Monthly Amortization
monthly_amortization = loan.monthly_amortization()
print(f"Monthly Amortization: {monthly_amortization:,.2f}")
print()

print("-------------------------------------------------------")
print()

# Create Amortization Schedule
schedule = loan.amortization_schedule()
print()

print("-------------------------------------------------------")
print()

# Ask user if they want to export
choice = input("Would you like to export this to Excel (Y/N)? ").strip().upper()

if choice == "Y":
    df = pd.DataFrame(schedule)

    # Folder & filename
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filename = f"amortization_schedule__{loan_amount}__{loan_term}__{interest_rate}.xlsx"
    filepath = os.path.join(script_dir, filename)

    # Export to Excel with styling
    with pd.ExcelWriter(filepath, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Amortization")
        workbook = writer.book
        worksheet = writer.sheets["Amortization"]

        from openpyxl.styles import Font

        bold_font = Font(bold=True)

        # Freeze top row
        worksheet.freeze_panes = "A2"  # Freeze row 1

        # Make the last row (totals) bold
        total_row_idx = len(df) + 1  # +1 because Excel rows start at 1, plus header
        for col in range(1, len(df.columns) + 1):
            cell = worksheet.cell(row=total_row_idx, column=col)
            cell.font = bold_font

    print(f"✅ Exported to: ")
    print(f"FOLDER: {script_dir}")
    print(f"FILENAME: {filename}")

else:
    print("❌ Export cancelled.")

print()
input("Press Enter to exit...")
