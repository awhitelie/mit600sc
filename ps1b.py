# Problem Set 1b
# Name: CZ
# Collaborators:
# Time Spent: 0:10

# Now write a program that calculates the minimum fixed monthly payment needed in order pay
# off a credit card balance within 12 months.

# 1.) Get balance and interest rate
# 1.) Start with a $10 minimum monthly payment
# 2.) Pay for a year
# 3.) If balance is still > 0, raise minimum monthly payment by $10, try again

# PROBLEM 2 ---------------------------------------------------------------

def apply_min_payment(balance):
  balance = balance + (balance * monthly_interest_rate) - min_monthly_payment
  return balance

original_balance = float(raw_input("What is the initial balance on the card? "))
annual_interest_rate = float(raw_input("What is the annual interest rate? "))
monthly_interest_rate = annual_interest_rate / 12

min_monthly_payment = 0
balance = original_balance


while balance > 0:
  balance = original_balance
  min_monthly_payment += 10
  month = 1
  for month in range (1,13):
    balance = apply_min_payment(balance)
    # print "Month " + str(month) + " balance is " + str(balance)
    if balance < 0:
      break
print "Monthly payment needed to pay off in one year: " + str(round(min_monthly_payment,2))
print "Number of months needed: " + str(month)
print "Balance: " + str(round(balance,2))
