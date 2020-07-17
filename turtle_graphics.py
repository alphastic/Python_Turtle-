#turtle heart
from turtle import *
def curvemove():
    for i in range(200):
        right(1)
        forward(1)
color('red','pink')       
begin_fill()
left(140)
forward(111.65)
curvemove()
left(120)
curvemove()
forward(111.65)
end_fill()
done()

#turtle star
import turtle  
  
star = turtle.Turtle() 

for i in range(100): 
    star.forward(100) 
    star.right(144) 
color('blue','red')       
begin_fill()
forward(100)
right(144)
turtle.done()