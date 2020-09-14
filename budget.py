class Category:
  name = ""
  ledger = list()
  balance = float(0)

  #To instantiate between objects
  def __init__(self, x):
    self.name = x

  #Deposit method
  def deposit(self, amount, description = ""):
    self.ledger.append({"amount" : float(amount), "description" : description})
    self.balance = self.balance + float(amount)

  #Withdraw method
  def withdraw(self, amount, description = ""):
    if self.check_funds(amount):
      return False
    else:
      self.ledger.append({"amount" : (0 - float(amount)), "description" : description})
      self.balance = self.balance - float(amount)
      return True

  #Get balance method
  def get_balance(self):
    return balance

  #Transfer method
  def transfer(self, amount, cat):
    if self.check_funds(amount):
      return False
    else:
      self.withdraw(amount, ("Transfer to " + cat))
      cat.deposit(amount, ("Transfer from " + cat))
      return True

  #Check funds method
  def check_funds(self, amount):
    if float(amount) > balance:
      return False
    else:
      return True

  


def create_spend_chart(categories):