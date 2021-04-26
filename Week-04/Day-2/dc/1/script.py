date_list = []
birth_date = input("Whats your birthdate (DD/MM/YYYY) ? : ")


year = birth_date[6:10]

age = 2021 - int(year)
last_num = age % 1

print(last_num)

 
# print(
# '       ___________       '
# '      |:H:a:p:p:y:|      '
# '    __|___________|__    '
# '   |^^^^^^^^^^^^^^^^^|   '
# '   |:B:i:r:t:h:d:a:y:|   ' 
# '   |                 |   '
# '   ~~~~~~~~~~~~~~~~~~~   '
# )

# The number of candles on the cake should be the last number of the users age, if they are 53, then add 3 candles.

# Bonus : If they were born on a leap year, display two cakes !