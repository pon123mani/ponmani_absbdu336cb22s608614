
class BankAccount:
  def__init__(self,account_number,account_holder_name,initial_balance=0.0):
  self.__account_number=account_number
  self.__account_holder_name=account_holder_name
  self.__accountbalance=initial_balance
def deposit(self,amount):
  if amount>0:
    self.__account_balance+=amount
    print("deposite ₹{}.new      balance:₹{}".format(amount,self.__account_balance))
  else:
    print("invaild deposite amount .please deposite a positive amount:")
def withdraw(self,amount):
  if amount>0 and amount<=self.__account_balance:
    self.__account_balance-=amount
    print("withdraw ₹{}.new balance:₹{}".format(amount,self.__account_balance))
  else:
    print("invaild withdraw amount or insufficient balance")
  def display_balance(self):
    print("Account balance for{}(account#{}:₹{}".format(self.__account))
account=BankAccount(account_number=123456,amount_holder_name="ponmani",initial amount=5000.0)
account.display_balance()
account.deposit(500)
account.withdraw(200)
account.display_balance()