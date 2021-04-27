birth_date = input('Please input your birthdate: (format: DD/MM/YYYY)')
d, m, y = list(map(int,birth_date.split('/')))
date = list(map(int, "27/4/2021".split('/')))
age = date[2] - y
birthday_flag = False
if m >= date[1]:
    if date[0] > d:
        age -= 1
if m == date[1] and d == date[0]:
    print("happy birthday!!!")
    birthday_flag = True
print_string = f'you are {age} years old' 
if birthday_flag: print_string += ' today'
print(print_string)
candles = int(age/10)
candle_string = 'i' * candles
while len(candle_string) < 10:
    candle_string += '_'
    candle_string = '_' + candle_string 
if len(candle_string) % 2 == 1:
    candle_string = candle_string[0:-1]
cake = f"""
       _{candle_string}_
# '    |:H:a:p:p:y:|      '
# '  __|___________|__    '
# ' |^^^^^^^^^^^^^^^^^|   '
# ' |:B:i:r:t:h:d:a:y:|   ' 
# ' |                 |   '
# ' ~~~~~~~~~~~~~~~~~~~   '
"""
print (cake)
# The number of candles on the cake should be the last number of the users age, if they are 53, then add 3 candles.

# Bonus : If they were born on a leap year, display two cakes !