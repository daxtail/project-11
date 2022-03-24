import turtle
import random

def draw_circle():
    radius = int(input('Enter the radius of the circle'))
    color = input('Enter the color')
    turtle.penup()
    turtle.fillcolor(color)
    turtle.goto(random.randint(-150,150)+20,random.randint(-150,150)+20)
    (turtle.begin_fill())
    turtle.circle(radius)
    (turtle.end_fill())
    turtle.pendown()
    turtle.pencolor("black")
    turtle.goto(0,-200)
    turtle.stamp()

draw_circle()
draw_circle()
draw_circle()
draw_circle()
