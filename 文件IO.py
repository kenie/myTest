#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import os

#raw_input([prompt])函数从标准输入读取一个行，并返回一个字符串(去掉结尾的换行行为):
'''str = raw_input("请输入：")
print "你输入的结果是：",str'''

#input([prompt])函数和raw_input([prompt])函数基本类似，但是input可以接收一个Python表达式作为输入，并将运算结果返回。
'''strtwo = input("Please enter:")
print "Your input is:",strtwo'''

#mkdir()方法，在当前目录下创建新的目录们。
#os.mkdir("newdir")

#chdir()方法，改变当前的目录。
#os.chdir("/home/newdir")

#getcwd()方法，显示当前的工作目录。
#print os.getcwd()

#rmdir()方法，删除目录。
os.rmdir("newdir")



