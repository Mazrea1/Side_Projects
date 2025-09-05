import time
import turtle
import datetime as dt

from yt_dlp.extractor.lazy_extractors import XMinusIE

t1 = turtle.Turtle()
t2 = turtle.Turtle()

secs = dt.datetime.now().second
mins = dt.datetime.now().minute
hours = dt.datetime.now().hour
amPm = dt.datetime.now().strftime("%p")
Screen = turtle.Screen()
Screen.bgcolor("Black")

t1.pensize(4)
t1.color("white")
t1.penup()

t1.goto(-400,0)
t1.pendown()

for i in range(2):
    t1.forward(900)
    t1.left(90)
    t1.forward(300)
    t1.left(90)

t1.hideturtle()

while True:
    t1.hideturtle()
    t1.clear()

    t1.write(str(hours).zfill(2)
        +":"+str(mins).zfill(2)+":"
        + str(secs).zfill(2)+" "
        + str(amPm).zfill(2),
        font = ("comicsans", 120, "bold"),)
    time.sleep(1)
    secs += 1

    if secs == 60:
        secs = 0
        mins += 1
    if mins == 60:
        mins = 0
        hours += 1
    if hours == 13:
        hr = 1
        if amPm == "PM":
            amPm = "AM"
        elif amPm == "AM":
            amPm = "PM"