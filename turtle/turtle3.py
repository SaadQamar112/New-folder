import turtle
win=turtle.Screen()
win.bgcolor("red")

turt=turtle.Turtle()
size=0
while True:
    for i in range(4):
        turt.fd(size+1)
        turt.left(90)
        size=size-5
    size=size+1
    
        