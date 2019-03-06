from turtle import *
import math
import random

bob = Turtle()

##THIS TAKES A REALLY LONG TIME SO INCREASE THE SPEED

bob.speed(10)

for i in range(2000):
	bob.forward(10)
	bob.left(math.sin(i/10)*25)
	bob.left(20)

done()

