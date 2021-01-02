def open_account():
  print("New Account is created")

open_account()

def deposit(balance, money):
  print("New cash is saved. Your new balance is {0} dollar.".format(balance))
  return balance + money

def withdraw(balance, money):
  if balance >= money:
    print("Complete the transaction. Your balance is {0} dollars.".format(balance - money))
    return balance - money
  else:
    print("Imcompleted transaction. Your balance is {0} dollars.".format(balance))

def withdraw_night(balance, money):
  commission = 100
  return commission, balance - money - commission

balance = 0
balance = deposit(balance, 1000)
#balance = withdraw(balance, 2000)
commission, balance = withdraw_night(balance, 500)
print("Commission fee is {0} dollar, and balance is {1} dollars.".format(commission, balance))