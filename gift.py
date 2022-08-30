import turtle
from turtle import *

screen = turtle.Screen()
screen.title("@her_devil_cat")

t = turtle.Turtle()
speed(0)

#background for the gift
t.penup()
t.goto(0, -300)
t.pendown()
t.color("black")
t.begin_fill()
t.circle(300)
t.end_fill()

#lid on gift
t.penup()
t.goto(-180, 20)
t.pendown()
t.color("red")
t.begin_fill()
for i in range(2):
    t.forward(360)
    t.left(90)
    t.forward(60)
    t.left(90)
t.end_fill()

#bottom of the gift
t.penup()
t.goto(-160, 0)
t.pendown()
t.begin_fill()
for i in range(2):
    t.forward(320)
    t.right(90)
    t.forward(210)
    t.right(90)
t.end_fill()

#right ribbon of the gift
t.penup()
t.goto(10, 100)
t.pendown()
t.pensize(10)
t.color("green")
for i in range(90):
    t.forward(1)
    t.left(0.4)
for i in range(90):
    t.forward(1)
    t.left(2)
for i in range(90):
    t.forward(1)
    t.left(0.4)

#left ribbon of the gift
t.penup()
t.goto(10, 100)
t.pendown()
t.pensize(10)
t.color("green")
t.right(70)
for i in range(90):
    t.forward(1)
    t.right(0.4)
for i in range(90):
    t.forward(1)
    t.right(2)
for i in range(90):
    t.forward(1)
    t.right(0.4)

#Message above the gift
t.penup()
t.goto(-160, 210)
t.pendown()
t.color("white")
t.write("HAPPY BIRTHDAY", font = ("Arial",23, "bold"))

turtle.done()