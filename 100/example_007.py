#!/usr/bin/env python
#-*- coding:UTF-8 -*-

'''题目：将一个列表的数复制到另一个列表中'''

a = [1,2,3,4,5,6]
b = a
a[0] = 0
print a
print b

a = [1,2,3,4]
b = a[:]
print b