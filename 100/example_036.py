#!/usr/bin/env python
#-*- coding:UTF-8 -*-

'''题目：求100之内的素数。'''

# 用户输入指定范围
lower = int(raw_input("输入最小区间值："))
upper = int(raw_input("输入最大区间值："))

for num in range(lower,upper + 1):
    if num > 1:
        for i in range(2,num):
            if (num % 2) == 0:
                break
        else:
            print num
