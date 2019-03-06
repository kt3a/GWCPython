from turtle import*
from random import*


pen = Turtle()
pen.color('blue')
pen.fillcolor("deep pink")
pen.begin_fill()

for i in range(39):
  speed(10)
  pen.forward(200)
  pen.left(170)
  
  
pen.end_fill()
done()
