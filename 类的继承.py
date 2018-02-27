#!/usr/bin/env python
#-*- coding:UTF-8 -*-

class Parent:       # 定义父类
    parentAttr = 100
    def __init__(self):
        print "调用父类构造函数"

    def parentMethod(self):
        print "调用父类方法"

    def setAttr(self,attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print "父类属性：",Parent.parentAttr

class Child(Parent):        # 定义子类
    def __init__(self):
        print "调用子类构造函数"

    def childMethod(self):
        print "调用子类方法"

print "****************"
c = Child()             # 实例化子类
c.childMethod()         # 调用子类方法
c.parentMethod()        # 调用父类方法
c.setAttr(200)          # 再次调用父类方法 - 设置属性值
c.getAttr()             # 再次调用父类方法 - 获取属性值
print issubclass(Child,Parent)          # 判断一个类是另一个类的子类或子孙类
print isinstance(c,Parent)              # 判断一个实例对象是一个Class类的实例对象