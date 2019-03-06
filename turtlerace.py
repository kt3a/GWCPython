
from turtle import*
from random import*

penup()
goto(-140,140)

for i in range(15):
  speed(10)
  write(i)
  right(90)
  forward(10)
  pendown()
  forward(150)
  penup()
  backward(160)
  left(90)
  forward(20)


#first turtle object
t1 = Turtle()
t1.color('red')
t1.shape('turtle')
#have the turtle go to the starting line
t1.penup()
t1.goto(-160,100)
t1.pendown()


#second turtle object
t2 = Turtle()
t2.color('purple')
t2.shape('turtle')
#have the turtle go to the starting line
t2.penup()
t2.goto(-160,80)
t2.pendown()

#third turtle object
t3 = Turtle()
t3.color('blue')
t3.shape('turtle')
#have the turtle go to the starting line
t3.penup()
t3.goto(-160,60)
t3.pendown()


#make the turtle do a spin
#I DIDNT DO THIS IN CLASS BUT THIS IS FUN
for i in range(2):
  speed(4)
  t1.right(180)



for turn in range(100):
  t1.forward(randint(1,5))
  t2.forward(randint(1,5))
  t3.forward(randint(1,5))
