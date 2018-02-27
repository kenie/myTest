#!/usr/bin/env python
#-*- coding:UTF-8 -*-

'''题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同'''

'''x = int(raw_input("数入一个5位数："))
a = x/10000
b = x%10
c = x/1000%10
d = x%100/10
print a,b,c,d
if a == b and c == d:
    print"%d 是回文数！"%x
else:
    print"%d 不是回文数！"%x'''

'''答案'''
a = int(raw_input("请输入一个数字："))
x = str(a)
flag = True

for i in range(len(x)/2):
    if x[i] != x[-i-1]:
        flag = False
        break
if flag:
    print "%d 是一个回文数！"%a
else:
    print "%d 不是一个回文数！"%a
