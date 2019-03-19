## Lesson 8 Strings, Psuedo-code, practice with functions 10/30/18
aString = "Hello World"

print(aString[0])
print(aString[0:5])
print(aString[6:11])

bString = "Katie"
for i in bString:
    print(i)

def counter1(bstr):
    count = 0
    vowels = "aeiouAEIOU"
    for i in bstr:
        if i in vowels:
            count += 1
    print(count)

#counter1("apples")

print("\n")     #will just make a space between the outputs

#count the vowels in a string
def counter(astr):
    count = 0
    vowels = "aeiouAEIOU"
    for i in range(len(astr)):
        if astr[i] in vowels:
            count += 1
    print(count)
    
#counter("marquette")
#counter("katie")


##project answer
def password(aString):
    vowels = "aeiou"   #all the vowels i will need to loop through
    newString = ""          #empty string variable 

    for i in range(len(aString)):
        if aString[i] in vowels:
            newString += "*"
            
        else:
            newString += aString[i]
        
print(newString)
    
password("katie")
password("mArquette")

## another way to do this:
def password(aString):
    newString = ""          
    
    for i in aString:
        if i in "aeiouAEIOU":      
            newString += "*"
            
        else:
            newString += i
            
    print(newString)
    
password("katie")
password("mArquette")


def change():
    alist = [1,2,3,4,5]
    for i in range(len(alist)):
        if alist[i]%2 ==0:
            alist[i] = "*"
    print(alist)
    
change()
