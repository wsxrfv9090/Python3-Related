import turtle
import time


screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)


for x in range(360):
    t.forward(x)
    t.left(44)


screen.tracer(0)
angle = 0

while True:
    t.home()
    t.clear()
    t.setheading(angle)
    
    for x in range(360):
        t.forward(x)
        t.left(43)
    
    screen.update()
    time.sleep(0.1)
    angle += 10

    if angle >= 360:
        angle = 0

turtle.done()
