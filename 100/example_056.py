#!/usr/bin/env python
#-*- coding:UTF-8 -*-

'''题目：画图，学用circle画圆形'''

'''if __name__ == "__main__":
    from Tkinter import *

    canvas = Canvas(width = 800,height = 600,bg = 'green')
    canvas.pack(expand = YES,fill = BOTH)
    k = 1
    j = 1
    for i in range(0,26):
        canvas.create_oval(310 - k,250 - k,310 + k,250 + k,width = 1)
        k += j
        j += 0.3

    mainloop()'''

'''if __name__ == '__main__':
    import turtle
    turtle.title("画圆")
    turtle.setup(800,600,0,0)
    pen=turtle.Turtle()
    pen.color("yellow")
    pen.width(5)
    pen.shape("turtle")
    pen.speed(1)
    pen.circle(100)'''

'''if __name__ == "__main__":          # 画五边形
    import turtle
    a = 160
    for i in range(1,6):
        turtle.forward(a)
        turtle.left(72)'''

'''if __name__ == "__main__":                 # 画一个五角星
    import turtle
    a = 160
    turtle.speed(1)
    turtle.fillcolor("red")
    turtle.fill(True)
    turtle.right(36)
    turtle.forward(a)
    for i in range(1,10):
        if i in (1,3,5,7,9):
            turtle.left(144)
            turtle.forward(a)
        else:
            turtle.right(72)
            turtle.forward(a)
    turtle.fill(False)'''



