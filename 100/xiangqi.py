#!/usr/bin/env python
#-*- coding:UTF-8 -*-

import turtle                           # 画象棋棋盘
import math

i = 0
x = -200
y = -200

turtle.color("black")
turtle.hideturtle()
turtle.speed(20)
turtle.pensize(3)

def draw(i):
    for _ in range(8):
        #if i % 2 == 0:
            #turtle.begin_fill()
        turtle.left(90)
        turtle.forward(40)
        turtle.right(90)
        turtle.forward(40)
        turtle.right(90)
        turtle.forward(40)
        turtle.right(90)
        turtle.forward(40)
        #if i % 2 == 0:
            #turtle.end_fill()
        turtle.penup()
        turtle.right(180)
        turtle.forward(40)
        turtle.pendown()
        i += 1

loop = 0

def drawt():
    turtle.left(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(320)
    turtle.right(90)
    turtle.forward(40)
    turtle.penup()
    turtle.right(180)
    turtle.forward(40)
    turtle.right(90)
    turtle.pendown()

for _ in range(9):
    turtle.penup()
    turtle.goto(x, y + loop)
    turtle.pendown()
    if i == 4:
        drawt()
    else:
        draw(i)
    i += 1
    loop += 40

turtle.penup()
turtle.goto(-80,160)
turtle.pendown()
turtle.right(45)
turtle.forward(2*(math.sqrt(3200)))

turtle.penup()
turtle.goto(0,160)
turtle.pendown()
turtle.right(90)
turtle.forward(2*(math.sqrt(3200)))

turtle.penup()
turtle.goto(0,-200)
turtle.pendown()
turtle.right(90)
turtle.forward(2*(math.sqrt(3200)))

turtle.penup()
turtle.goto(-80,-200)
turtle.pendown()
turtle.right(90)
turtle.forward(2*(math.sqrt(3200)))

turtle.done()



