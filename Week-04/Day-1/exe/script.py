user_num = input("Enter a number between 1 and 100: ")
x = 3
y = 5


if user_num.islower():
    while (user_num <=100 or user_num >=1):

        if user_num % 3 and % 5==0:
            print("FizzBuzz!")

        elif user_num % 3==0:
            print("Fizz!")

        elif user_num % 5==0:
            print("Buzz!")

        else: print("Game Over")

else: print("Enter a number please")
return