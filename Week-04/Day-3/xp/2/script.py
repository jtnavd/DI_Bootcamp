family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total_price = 0

for age in list(family.values()):
    if age <= 3:
        total_price = total_price + 0

    elif age > 3 and age <=12:
        total_price = total_price + 10

    elif age > 12:
        total_price = total_price + 15

print(total_price)