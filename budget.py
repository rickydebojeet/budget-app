class Category:
  name = ""
  ledger = list()

  def __init__(self, x):
    self.name = x

  def deposit(self, amount, description = ""):
    self.ledger.append({"amount" : float(amount), "description" : description})


def create_spend_chart(categories):