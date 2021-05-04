my_list = input('Enter age separated with spaces : ').split()
total = 0
num1 = 0
num2 = 0
num3 = 0

for age in my_list:
    if int(age) < 3:
        num1 += 1
    if int(age) < 12:
        num2 += 1
        total += 10
    elif int(age) >= 12:
        num3 += 1
        total += 15

print(f'{num1}younger than 3 y.o,{num2} between 3 and 12 y.o,{num3} older than 12 y.o, the total prices is {total}')