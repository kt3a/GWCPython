##Simplified Hangman

import random
alist = ["santa","elves","rudolph"]
choice = random.choice(alist)

while(True):
    user = input("give me a letter or press Q to quit ")

    if user == "Q":
        print("Thanks for Playing")
        break
    else:
        if user in choice:
            print("the word is: " , choice)
                
