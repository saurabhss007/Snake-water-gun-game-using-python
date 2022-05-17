import random
from tkinter import W

from numpy import true_divide

def game(comp, you):
    if comp == you :
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False
    elif comp == 'g':
        if you == 'w':
            return True
        elif you == 's':
            return False       


i = 1
while i == 1:

    print("computer's turn : choose snake(1), water(2), gun(3) :")
    randNO = random.randint(1,3)
    if randNO == 1:
        comp = 's'
    elif randNO == 2:
        comp = 'w'
    elif randNO == 3:
        comp = 'g' 
    
    
    you  = input("your turn : choose snake(s), water(w), gun(g) :")
    print(f"Computer chose : {comp}")
    print(f"you chose : {you}")
    a = game(comp, you)
    if a == None:
        print("It's a tie")
    elif a == True:
        print("You win!")
    else:
        print("You lost!")
    player = input("Enter (p) to play more or (e) to exit :")
    if player == 'p':
     continue
    elif player == 'e':
        break