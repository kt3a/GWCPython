## Lesson 9 Partner Work and Comprehension

alist = [15,20,4,23,35,8]

for i in alist:
    if i%5==0:
        print(i)
    else:
        print("not divisible by 5")


##project answer key
## a function takes a string, and each vowel in the string will be replaced by a number that
## represents the order of vowels of that word

        
##first way to solve
def password(aString):
    vowels = "aeiouAEIOU"   #all the vowels i will need to loop through
    newString = ""          #empty string variable 
    count = 0
    
    
    for i in range(len(aString)):
        if aString[i] in vowels:
            newString += str(count)
            count += 1
            
        else:
            newString += aString[i]
            
    print(newString)
    
password("katie")
password("mArquette")


#second way to solve
def password1():
    
    inputString = input("Give me any string")
    vowels = "aeiouAEIOU"   #all the vowels i will need to loop through
    newString = ""          #empty string variable 
    count = 0
    for i in range(len(inputString)):
        if inputString[i] in vowels:
           newString += str(count)
           count += 1
            
        else:
            newString += inputString[i]
            
    print(newString)
    
#password1()
