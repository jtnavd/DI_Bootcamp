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

# Create the code which will output the results below.
# Hint : When adding 2 currencies which don’t share the same label you should raise an error.
# >>> c1 = Currency('dollar', 5)
# >>> c2 = Currency('dollar', 10)
# >>> c4 = Currency('shekel', 1)
# >>> c3 = Currency('shekel', 10)

# >>> str(c1)
# '5 dollars'

# >>> int(c1)
# 5

# >>> repr(c1)
# '5 dollars'

# >>> c1 + 5
# 10

# >>> c1 + c2
# 15

# >>> c1 
# 5 dollars

# >>> c1 += 5
# >>> c1
# 10 dollars

# >>> c1 += c2
# >>> c1
# 20 dollars

# >>> c1 + c3
# TypeError: Cannot add between Currency type <dollar> and <shekel>