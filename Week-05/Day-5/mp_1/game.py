import random


cpu_score = 0
user_score = 0
class Game():
    def __init__(self):
        self.user_choice = ""
        self.cpu_choice = ""
    def get_user_item(self):
        active = True
        while active:
            self.user_choice = input("Select (r)ock or (p)aper or (s)cissors")
            self.user_choice.lower()
            if self.user_choice == "r" or self.user_choice == "p" or self.user_choice == "s":
                # funct 
                active=False
            return self.user_choice
        # while user_choice != "r" or user_choice != "P" or user_choice != "s":
        #     user_choice = input("Please enter only 's' for scissor, 'r' for rock, or 'p' for paper: ")
game1= Game()
game1.get_user_item()
print(game1.user_choice)


###########################################################################################################
# class Game():
#     def __init__(self,user,cpu):
#         self.user = user
#         self.cpu = cpu

#     def get_user_item(self):
#         user_choice = input(f'Rock {r}, Paper {p}or Scissors{s} : ')
#         else:
#             print("not valid, try again")
#             get_user_menu_choice()
#         return user_choice
#         print("the user make his choice")
        
#     # def get_computer_item(self):
#     #     cpu_choice = random.randint(1,3)
#     #     if cpu_choice == 1 :
#     #         cpu_choice = "r"
#     #     elif cpu_choice == 2 :
#     #         cpu_choice = "p"
#     #     else:
#     #         cpu_choice = "s"
#     #     return cpu_choice

# r1 = Game.get_user_item(self.user)
# print(r1)
# # test1 = Game.get_user_item(self.user)
# # test2 = Game.get_computer_item(self.cpu)
# # cpu_score = 0
# # user_score = 0

# # def get_user_choice():
# #     user_choice = input('Rock, Paper or Scissors : ')
#     if user_choice in ["rock", "r"]:
#         user_choice = "r"
#     elif user_choice in ["paper", "p"]:
#         user_choice = "p"
#     elif user_choice in ["scissor", "s"]:
#         user_choice = "s"
#     else:
#         print("not valid, try again")
#         get_user_menu_choice()
#     return user_choice

# def get_cpu_choice():
#     cpu_choice = random.randint(1,3)
#     if cpu_choice == 1 :
#         cpu_choice = "r"
#     elif cpu_choice == 2 :
#         cpu_choice = "p"
#     else:
#         cpu_choice = "s"
#     return cpu_choice

# while True:
#     print('')
#     user_choice = get_user_choice()
#     cpu_choice = get_cpu_choice()
#     print('')
    
# if user_choice == 'r':
#     if cpu_choice == 's':
#         print('Rock break Scissors, you win one point ') 

# if user_choice == 'r':
#     if cpu_choice == 'p':
#         print('Rock break Scissors, you lose') 

# if user_choice == 's':
#     if cpu_choice == 'p':
#         print('Scissors cut paper, you win')

# if user_choice == 's':
#     if cpu_choice == 'p':
#         print('Scissors cut paper, you win')
        
# else:
#     print('You chose the same item, its a Draw') 
    










