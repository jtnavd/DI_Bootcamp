import random

cpu_score = 0
user_score = 0

def get_user_choice():
    user_choice = input('Rock, Paper or Scissors : ')
    if user_choice in ["rock", "r"]:
        user_choice = "r"
    elif user_choice in ["paper", "p"]:
        user_choice = "p"
    elif user_choice in ["scissor", "s"]:
        user_choice = "s"
    else:
        print("not valid, try again")
        get_user_menu_choice()
    return user_choice

def get_cpu_choice():
    cpu_choice = random.randint(1,3)
    if cpu_choice == 1 :
        cpu_choice = "r"
    elif cpu_choice == 2 :
        cpu_choice = "p"
    else:
        cpu_choice = "s"
    return cpu_choice

while True:
    print('')
    user_choice = get_user_choice()
    cpu_choice = get_cpu_choice()
    print('')
    
if user_choice == 'r':
    if cpu_choice == 's':
        print('Rock break Scissors, you win one point ') 

if user_choice == 'r':
    if cpu_choice == 'p':
        print('Rock break Scissors, you lose') 

if user_choice == 's':
    if cpu_choice == 'p':
        print('Scissors cut paper, you win')

if user_choice == 's':
    if cpu_choice == 'p':
        print('Scissors cut paper, you win')
        
else:
    print('You chose the same item, its a Draw') 
    