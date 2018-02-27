#!/usr/bin/env python
#-*- coding:UTF-8 -*-

'''题目：输入三个整数x,y,z,请把这三个数由小到大输出'''

L = []
for i in range(3):
    x = int(raw_input('integer:\n'))
    L.append(x)
L.sort()
for j in range(len(L)):
    print L[j]