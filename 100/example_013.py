#!/usr/bin/env python
#-*- coding:UTF-8 -*-

'''题目：打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数本身。
例如：153是一个“水仙花数”，因为153=1的三次方+5的三次方+3的三次方。
程序分析：利用循环控制100-999个数，每个数分解出个位，十位，百位。'''

for i in range(100,1000):
    s = str(i)
    if (int(s[0]) ** 3) + (int(s[1]) ** 3) + (int(s[2]) ** 3) == i:
        print i