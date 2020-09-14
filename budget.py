class Category:
  name = ""
  ledger = list()

  #To instantiate between objects
  def __init__(self, x):
    self.name = x
    self.balance = 0.0

  #Deposit method
  def deposit(self, amount, description = ""):
    self.ledger.append({"amount" : float(amount), "description" : description})
    self.balance = self.balance + float(amount)

  #Withdraw method
  def withdraw(self, amount, description = ""):
    if self.check_funds(amount) == False:
      return False
    else:
      self.ledger.append({"amount" : (0 - float(amount)), "description" : description})
      self.balance = self.balance - float(amount)
      return True

  #Get balance method
  def get_balance(self):
    return self.balance

  #Transfer method
  def transfer(self, amount, cat):
    if self.check_funds(amount) == False:
      return False
    else:
      self.withdraw(amount, ("Transfer to " + cat))
      cat.deposit(amount, ("Transfer from " + cat))
      return True

  #Check funds method
  def check_funds(self, amount):
    if float(amount) > self.balance:
      return False
    else:
      return True

  #Defining return values
  def __str__(self):
    displayer = ""
    fline = self.name.center(30, "*")
    fline = fline.rstrip()
    displayer = displayer + fline + '\n'
    for items in self.ledger:
      item = items.values()
      spart = item[0]
      spart = str('%.2f'%spart)
      fpart = item[1]
      fpart = fpart[: 24].ljust(23)
      spart = spart[: 8].rjust(7)
      displayer = displayer + fpart + spart + "\n"
    displayer = displayer + "Total: " + str('%.2f'%self.balance) 
    return displayer
  
    

def create_spend_chart(categories):