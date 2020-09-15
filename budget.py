class Category:
  name = ""

  #To instantiate between objects
  def __init__(self, x):
    self.name = x
    self.balance = 0.0
    self.ledger = list()

  #Deposit method
  def deposit(self, amount, description = ""):
    self.ledger.append({"amount" : amount, "description" : description})
    self.balance = self.balance + float(amount)

  #Withdraw method
  def withdraw(self, amount, description = ""):
    if self.check_funds(amount) == False:
      return False
    else:
      self.ledger.append({"amount" : (0 - amount), "description" : description})
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
      self.withdraw(amount, ("Transfer to " + cat.name))
      cat.deposit(amount, ("Transfer from " + self.name))
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
    fline = self.name
    fline = fline.center(30, "*").rstrip()
    displayer = displayer + fline + '\n'
    for items in self.ledger:
      item = list(items.values())
      spart = item[0]
      spart = str('%.2f'%spart)
      fpart = item[1]
      fpart = fpart[: 23].ljust(23)
      spart = spart[: 7].rjust(7)
      displayer = displayer + fpart + spart + "\n"
    displayer = displayer + "Total: " + str('%.2f'%self.balance)
    return displayer

#Defining bar chart creation functon
length = list()
name = list()
withdrawls = list()
percent = list()
def create_spend_chart(categories):
  for category in categories:
    tmp = 0
    length.append(len(category.name))
    name.append(category.name)
    for items in category.ledger:
      item = list(items.values())
      if item[0] >= 0 :
        continue
      else:
        tmp = tmp + (-(item[0]))
    withdrawls.append(tmp)

  #Calculating Percentage
  total = sum(withdrawls)
  for x in range(len(withdrawls)):
    per = withdrawls[x] / total
    per = int(round(per, 2) * 100)
    percent.append(per)

  #Generating Output
  output = "Percentage spent by category\n"
  tmp = 100
  while  tmp >= 0:
    output = output.rstrip(" ") + str(tmp).rjust(3) + "| "
    for x in range(len(percent)):
      if tmp <= percent[x]:
        output = output + "o" + "  "
      else:
        output = output + "   "
    tmp = tmp - 10
    output = output + "\n"
  output = output.rstrip(" ") + "    -"

  #Generating dashes
  for x in range(len(percent)):
    output = output.rstrip(" ") + "---"
  output = output + "\n"
  
  #Generating names
  for x in range(max(length)):
    output = output.rstrip(" ") + "     "
    for y in range(len(name)):
      try:
        output = output + name[y][x] + "  "
      except:
        output = output + "   "
    if not x == (max(length) - 1):
      output = output + "\n"
  length.clear()
  name.clear()
  withdrawls.clear()
  percent.clear()
  return output
