#!/usr/bin/env python
#-*- coding:UTF-8 -*-

'''题目：输出9*9乘法口诀表'''


for i in range(1,10):
    print
    for j in range(1,i+1):
        print "%d * %d = %d  " % (j,i,i*j),         # print后+逗号不会自动换行