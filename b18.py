import turtle
turtle.Screen().bgcolor("red")
turtle.Screen().setup(300,400)
polygon=turtle.Turtle()
n=6
l=70
a=360/n
for i in range(n):
    polygon.forward(l)
    polygon.right(a)
turtle.done()