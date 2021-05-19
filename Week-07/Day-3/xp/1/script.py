# import random

# colors = ['red','yellow','red']

# current_color = random.choice(colors)

# if current_color == 'green':
#     print('you can drive')
# elif current_color == 'red':
#     print('Stop the car')
# else:
#     print('slow down')



# x = random.randint(1,3)
# traffic_light = int(x)

# while True:
#     if x == 1:
#         print('green_light')
#     elif x == 2:
#         print('yellow_light')
#     else :
#         print('red_light')

# for i in range(1,2500,5):
#     print(i)

# for i in range(1001,3000):
#     if i% 7 == 0:
#         print(i)


# name_list = ['chaim', 'shimon', 'lila', 'ronny','micheal', 'jonathan', 'eliyahu', 'shmuel']

# for n in name_list:
#     if 'a' in n:
#     # name_list.sort()
#         print(n)

# for n in name_list:
#     for i in n:
#         if i == 'a':
#             # name_list.sort()
#             print(n)


# list_1 = [5,'d',8,'r',6,'u']
# char_list = []
# num_list = []

# while True:
#     if int in list_1:
#         num_list.append()
#         print(num_list)
#         print(list_1)

# counter = 0
# while counter != 20 :
#     print(f'{counter}: still running')
#     counter +=1
# print('complete')

#####EXERCISES############

# for i in range(20):
#     print(i)

#4----------------------------------------------------------------

# num_list = []
# for float(i) in range(1.5,5,0.5):
#     num_list.append()
#     print(num_list)

#5----------------------------------------------------------------

# basket = ["Banana", "Apples", "Oranges", "Blueberries"];
# basket.remove('Banana')
# basket.remove('Blueberries')
# basket.append('Kiwi')
# basket.insert(0, 'Apples')
# basket.count('Apples')
# basket.clear()
# print(basket)

#6----------------------------------------------------------------

# name = ''
# while name != "Jonathan":
#     name = input('Enter a name : ')
#     print(f"your name is {name}")
    
#7----------------------------------------------------------------

# for i in range(200):
#     if i %2 == 0:
#         print(f'éven number: {i}')
#     else:
#         print(f'odd number: {i}')


#8----------------------------------------------------------------

# for i in range(1500,2500):
#     if i %5 == 0:
#         print(f'multiple of 5 : {i}')
#     if i %7 == 0:
#         print(f'multiple of 7 : {i}')

#9----------------------------------------------------------------

# favorite_fruits = []

# while True:
#     user_input = input("Add a fruit of your choice : ~separate each item by a space~").split(' ', 2)
#     add_fruit = favorite_fruits.append(user_input)
#     print(favorite_fruits)
#     if add_fruit in list(favorite_fruits):
#         print('You chose one of your favorite fruits! Enjoy')
#     else:
#         print('You chose a new fruit. I hope you enjoy')

#10----------------------------------------------------------------

# topping_list = []
# topping = ''
# price = 10
# while topping != 'quit':
#     topping = input("pick a topping on your pizza: ")
#     print(f'adding {topping} on your pizza!')
#     price += 2.5
#     topping_list.append(topping)

# topping_list.pop()
# price -= 2.5
# print(f'you ordered a pizza with {topping_list} on it! total price = {price}')

#11----------------------------------------------------------------

#12----------------------------------------------------------------

# name_list = ['Conrad','Phil','Jordan']

# while name_list >= age:
#     age = input('enter the age of that member: ')

#===================================================================

# class Vehicle:
#     def __init__(self, vehicle_type):
#         self.vehicle_type = vehicle_type
#         self.parts = []
#     def tires(self, amount):
#         amount_of_tires = f'{amount} tires'
#         self.parts.append(amount_of_tires)
#     def body(self):
#         if self.vehicle_type == 'car':
#             self.parts.append('car body')
#         elif self.vehicle_type == 'truck':
#             self.parts.append('truck body')
#         elif self.vehicle_type == 'motorcycle':
#             self.parts.append('motorcycle body')
#         elif self.vehicle_type == 'plane':
#             self.parts.append('plane body')
#     def specs(self):
#         if self.vehicle_type == 'car':
#             self.parts.append('suspension')
#         elif self.vehicle_type == 'truck':
#             self.parts.append('attached container')
#         elif self.vehicle_type == 'motorcycle':
#             self.parts.append('wheels')
#         elif self.vehicle_type == 'plane':
#             self.parts.append('wings')
#     def display(self):
#         print(f'Parts needed to build your {self.vehicle_type}')
#         for part in self.parts:
#             print(f'{self.parts.index(part) + 1}: {part}')
#     def __add__(self,specs):
#         return self.parts + specs
#     def __repr__(self):
#         return f'type: {self.vehicle_type} parts: {self.parts}'

# v1 = Vehicle('car')
# v2 = Vehicle('motorcycle')
# v3 = Vehicle('plane')

#-------------------------------------------------------------

class Cat:
    def __init__(self, fur_type):
        # self.name = name
        self.fur_type = fur_type
        self.hair = []
    def cat_fur(self):
        if self.fur_type == 'black':
            self.hair.append('black')
        elif self.fur_type == 'red':
            self.hair.append('red')
        elif self.fur_type == 'grey':
            self.hair.append('grey')
        elif self.fur_type == 'white':
            self.hair.append('white')

    def eat(self, food):
        print(f'eat {food} cups of food per days')
    def jump(self,height):
        print(f"can jump {height}'s high")
    def play(self):
        print(f'plays with ball')

    def __repr__(self):
        return f'type of hair: {self.fur_type}'
