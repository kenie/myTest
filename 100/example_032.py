#!/usr/bin/env python
#-*- coding:UTF-8 -*-

'''题目：按相反的顺序输出列表的值。'''

s = ['one','two','three','five']
for i in range(len(s)):
    print s[-i-1]

'''答案：'''
a = ['one','two','three','five']
for i in a[::-1]:
    print i