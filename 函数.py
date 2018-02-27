#!/usr/bin/python
# -*- coding:UTF-8 -*-

import calendar

def calleap(x,y):
    leapcount = calendar.leapdays(x,y)
    return leapcount

print calleap(1988,2017)

def changeIn(a):
    a = 10

b = 2
changeIn(b)
print b

#关键字参数
def printme(str):
    "打印任何传入的字符串"
    print str
    return

#调用printme函数
printme(str = "My string")

#不定长参数
def printinfo(arg1,*vartuple):
    "打印任何传入的参数"
    print "输出："
    print arg1
    for var in vartuple:
        print var
    return

printinfo(10)
printinfo(70,60,50)

#匿名函数lambda
'''
lambda只是一个表达式，函数体比def简单很多。
lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。
虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
'''
sum =  lambda arg1,arg2:arg1 + arg2

print "相加后的值为：",sum(10,20)
print "相加后的值为：",sum(20,30)