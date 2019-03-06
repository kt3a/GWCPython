from math import *

####################### Problem 1 ##################################

##answer = int(input("Tell me a number in inches"))
##inches = answer
##cent = (answer *2.54)
##feet = answer/12
##meters = answer/39.37
##print("Inches: ",inches)
##print("Centimeters: ", cent)
##print("Feet: ",feet)
##print("Meters: {0:.3f}".format(meters))


#function answer for cool kids
def convert():
    answer = int(input("Give me a number in inches"))
    inches = answer
    cent = (answer *2.54)
    feet = answer/12
    meters = answer/39.37
    print("Inches: ",inches)
    print("Centimeters: ", cent)
    print("Feet: ",feet)
    print("Meters: {0:.3f}".format(meters))
convert()



####################### Problem 2 ##################################

def fn1():
    n = int(input("Enter an interger 'n'"))
    for i in range (0, n):
        for a in range(1,4):
            k = (5*"*"+5*" ")
            print(k*n)
        for a in range(1,4):
            u = (5*" "+5*"*")
            print(u*n)
#fn1()  







####################### Problem 3 ##################################


def reverse1(astr):
    new = ""
    for i in range(1,len(astr) +1):
        new += astr[len(astr) -i]
    print(new)
#reverse1("Hello World!")


##here is an altertative answer using string slicing and recursion 
def reverse2(s): 
    if len(s) == 0: 
        return s 
    else: 
        return reverse(s[1:]) + s[0]
#print(reverse2("katie"))






