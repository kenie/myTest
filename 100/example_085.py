#!/usr/bin/env python
#-*- coding:UTF-8 -*-

'''题目：输入一个奇数，然后判断最少几个9除于该数的结果为整数。'''

if __name__ == "__main__":
    odd = int(raw_input("input a odd number:"))
    n1 = 1
    c9 = 1
    m9 = 9
    sum = 9
    while n1 != 0:
        if sum % odd == 0:
            n1 = 0
        else:
            m9 *= 10
            sum += m9
            c9 += 1
    print "%d 个 9 可以被 %d 整除：%d"%(c9,odd,sum)
    r = sum / odd
    print "%d / %d = %d"%(sum,odd,r)