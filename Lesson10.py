## Lesson 10 Giant Review Session
aword = "marquette"
count_e = 0
for i in range(len(aword)):
    if aword[i] in "e":
        count_e += 1
        
#print(count_e)


def repeat():
    
    while True:
        x = input("What day of the week is it?")
        
        if x == "Monday":
            print("It's the first day of the week!")
        
        elif x == "Saturday":
            print("Its the weekend, yay!")
           #put a statement here to stop the program
  
        
#function call here
    
def repeat1():
    
    while True:
        x = int(input("give me a number"))
        
        if x > 6 and x<13 and x!=9:
            print(str(x) + " is greater than 6!")
        elif x >13 and x<15:
            print("nice!")
            continue
        elif x == 9:
            break
     
repeat1()

#how to use the number randomizer

import random 

num = random.randint(1,6+1)
#print(num)
    
