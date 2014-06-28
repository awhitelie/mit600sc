# Lower Bound = Balance / 12
# Upper Bound = (Balance * (1 + Annual Interest Rate / 12) ** 12) / 12
#
#
# When first solution is found, becomes new upper bound
# Last checked becomes new lower bound
#
#
#

def apply_min_payment(balance,payment):
  balance = balance + (balance * monthly_interest_rate) - payment
  return balance

def bisect(low,high):
  return (low + high) / 2



original_balance = float(raw_input("What is the initial balance on the card? "))
annual_interest_rate = float(raw_input("What is the annual interest rate? "))
monthly_interest_rate = annual_interest_rate / 12
low = original_balance / 12
high = (original_balance * (1 + monthly_interest_rate) ** 12) / 12

balance = original_balance
monthly_payment = low
e = .001

while e < abs(balance):
  balance = original_balance
  month = 1
  monthly_payment = bisect(low,high)
  for month in range (1,13):
    balance = apply_min_payment(balance,monthly_payment)
    print "Month " + str(month) + " balance is " + str(balance)
  if balance > 0:
    low = monthly_payment
  if balance < 0:
    high = monthly_payment


print ""
print "Monthly payment needed to pay off in one year: " + str(round(monthly_payment,2))
print "Number of months needed: ", month
print "Balance: " + str(round(balance,2))
