#loops and lists 
##class demo 
#lists
alist = [1,2,3,"a","b"]         #lists can hold any variable type

blist = [alist,10]              #you can put a list inside of a list
#print(blist)

#accessing items in a list
#print(alist[4])

#reassign items in a list
blist[0] = "Zero"
#print(blist)


#loops
for i in range(0,5):            #i represents the index number in a range of numbers the loop currently deals with 
   # print(i)


for a in range(0,10,2):         #make sure you nest the print statement and have a colon after the loop statement
    #print(a)


for b in range(10,0,-1):        #you can loop in reverse order if you add a third perameter
    print(b)



##class activity answer key
#1: what element is at index 3 in the list 
lista = ["katie",23,4.5,"A"]
print("Index 3 of lista is:",lista[3])

#2: what is the output of the following code?
for i in range(0,4):
    print("hi")

#3: take the list and change index 4 to "a"
alist = [1,2,3,4,5]
alist[4] = "a"
print("The new list is:",alist)


#4: write a loop that will print out your name 5 times
my_name = "katie"
for a in range(5):
    print(my_name)

#5 review: make a loop that will print out hi and your name 5 times if a user input number is between 0 and 5
my_name1 = "Katie"
x = int(input("choose a number"))
if x<=5:
    print(my_name1)
else:
    print(x)
    
    
    
#6
sum = 0
for b in range(0,5):
    sum = sum + b
print(sum)
    


#7
clist = [2,3,4,5,6]
the_sum = 0
for i in clist:
   the_sum += i
print(the_sum)
