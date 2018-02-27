#!/usr/bin/python
#-*- coding:UTF-8 -*-

list = ['physics','cheistry',1997,2000]

print "Value available at index 2 ："
print list[2]
list[2] = 2001          #列表2元素的值
print "New value available at index 2 ："
print list[2]

#删除列表元素
del list[2]
print "After deleting value at index 2 ："
print list