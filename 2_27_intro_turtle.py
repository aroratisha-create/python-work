#import turtle as t
#t.forward(90)
#t.right(90)
#t.forward(50)
#t.right(90)
#t.forward(90)
#t.right(90)
#t.forward(50)
#t.done()

import turtle
a=turtle.Screen()
a.bgcolorimport turtle
polygon = turtle.Turtle()
num_sides = 6
side_length = 70
angle = 360.0 / num_sides
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
turtle.done()