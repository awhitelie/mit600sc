# Problem Set 1a
# Name: CZ
# Collaborators:
# Time Spent: 0:10


# Write a program to calculate the credit card balance after one year
# if the person only pays the minimum on the card.
#
# Inputs:
# outstanding balance on the card
# annual interest rate
# minimum monthly payment rate

# Min monthly payment = min monthly payment rate * balance
# Interest paid = annual interest rate / 12 * balance
# Principal paid = min monthly payment - interest paid
# Remaining balance = principal paid - interest paid


# PROBLEM 1 ---------------------------------------------------------------

def calculate_remaining_balance(balance, annual_interest_rate, min_monthly_payment_rate):
  min_payment = min_monthly_payment_rate * balance
  interest_paid = annual_interest_rate / 12 * balance
  principal_paid = min_payment - interest_paid
  balance = balance - principal_paid

  print "Your minimum payment is: $" + str(round(min_payment,2))
  print "Your interest paid is: $" + str(round(interest_paid,2))
  print "Your principal paid is : $" + str(round(principal_paid,2))
  print "Your remaining balance is : $" + str(round(balance,2))
  print " "
  return balance


balance = float(raw_input("What is the initial balance on the card? "))
annual_interest_rate = float(raw_input("What is the annual interest rate? "))
min_monthly_payment_rate = float(raw_input("What is the minimum monthly payment rate? "))
month = 1

# while month <= 12:
#   print "Month " + str(month)
#   balance = calculate_remaining_balance(balance, annual_interest_rate,min_monthly_payment_rate)
#   month += 1

for month in range (1,13):
  print "Month " + str(month)
  balance = calculate_remaining_balance(balance, annual_interest_rate,min_monthly_payment_rate)
