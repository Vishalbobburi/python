"""
Purpose: Bank Loan

    Simple Interest : A = P (1 + rt)

                        A	=	final amount
                        P	=	initial principal balance
                        r	=	annual interest rate
                        t	=	time (in years)

Ref :https://www.calculatorsoup.com/calculators/financial/simple-interest-plus-principal-calculator.php

"""


# Input values
P = float(input("Enter the principal balance (P): "))  # Initial principal balance
r = float(input("Enter the annual interest rate (r) in decimal (e.g., 0.05 for 5%): "))  # Annual interest rate
t = float(input("Enter the time in years (t): "))  # Time in years

# Calculate the final amount using Simple Interest formula
A = P * (1 + r * t)

# Output the result
print(f"The final amount (A) after {t} years is: ₹{A:.2f}")









# Assignment
# 1. Compound Interest Calculation
#     ref: https://www.calculatorsoup.com/calculators/financial/compound-interest-calculator.php

# Input values
P = float(input("Enter the principal balance (P): "))  # Initial principal balance
r = float(input("Enter the annual interest rate (r) in decimal (e.g., 0.05 for 5%): "))  # Annual interest rate
t = float(input("Enter the time in years (t): "))  # Time in years
n = int(input("Enter the number of times interest is compounded per year (n): "))  # Number of times interest is compounded

# Calculate the final amount using Compound Interest formula
A = P * (1 + r / n) ** (n * t)

# Calculate the compound interest
compound_interest = A - P

# Output the results
print(f"The final amount (A) after {t} years is: ₹{A:.2f}")
print(f"The compound interest earned is: ₹{compound_interest:.2f}")
