##Dice Project

import random 

def dice():
    abool = False
    
    while(True):
        task = input("would you like to roll the dice, type 'yes' or type 'no'")
    
        if (task == "yes"):
            num = random.randint(1,6+1)
            print("You rolled a" , num)
            abool = True
        elif(task == "no"):
            break

        
dice()
