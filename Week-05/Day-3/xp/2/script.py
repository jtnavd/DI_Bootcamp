class Currency():
  def __init__(self, money_type, amount = 0):
    self.money_type = money_type
    self.amount = amount
      
    # make difference between currencies
  def __add__(self, other):
    return self.amount + other.amount if self.money_type == other.money_type else ValueError 

    #  turn the currency into string
  def __str__(self):
    return f'{self.money_type} {self.amount}'

    #  
  def __repr__(self):
    return f'{self.money_type} {self.amount}'
  
  def __int__(self):
    return f'{self.amount}'

c1 = Currency("dollar", 5)
c2 = Currency("dollar", 10)
c3 = Currency("shekel", 1)
c4 = Currency("shekel", 10)

print(Currency)
print(c1 + c2)
print(c1)
print(c1 +=5)
print(c1 += c2)
print(c1 + c3)