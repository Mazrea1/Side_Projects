import time
import turtle
import datetime as dt

t1 = turtle.Turtle()
t2 = turtle.Turtle()

sec = dt.datetime.now().second
mins = dt.datetime.now().minute
hours = dt.datetime.now().hour

Screen = turtle.Screen()
Screen.bgcolor("Black")

t1.pensize(4)
t1.color("white")
t1.penup()

t1.goto(-20,0)
t1.pendown()

for i in range(2):
    t1.forward(300)
    t1.left(90)
    t1.forward(300)
    t1.left(90)

t1.hideturtle()

while True:
    t1.hideturtle()
    t1.clear