class Category:
  name = ""
  ledger = list()
  balance = float(0)

  def __init__(self, x):
    self.name = x

  def deposit(self, amount, description = ""):
    self.ledger.append({"amount" : float(amount), "description" : description})
    balance = balance + float(amount)

  def withdraw(self, amount, description = ""):
    if float(amount) > balance:
      return False
    else:
      self.ledger.append({"amount" : (0 - float(amount)), "description" : description})
      balance = balance - float(amount)
      return True


def create_spend_chart(categories):