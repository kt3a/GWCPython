from turtle import*
from random import*

#set background color
#wind = Screen()
#wind = bgcolor("black")
speed(0)
colors = ["red","yellow","blue","green"]
for x in range(360):
  pencolor(colors[x%4])
  circle(x)
  left(90)
