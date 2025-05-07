import turtle
turtle.Screen().bgcolor("red")
turtle.Screen().setup(250,300)

poly=turtle.Turtle()

sides=6
length=65
anggle=360.0/sides

for i in range(sides):
    poly.forward(length)
    poly.right(anggle)
