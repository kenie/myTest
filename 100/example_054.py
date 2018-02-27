#!/usr/bin/env python
#-*- coding:UTF-8 -*-

'''题目：取一个整数a从右端开始的4-7位。
程序分析：（1）先使a右移4位
         （2）设置一个低4位全为1，其余全为0的数，可用~（~0<<4）
        （3）将上面二者进行&运算。'''

if __name__ == "__main__":
    a = int(raw_input("Input a number:\n"))
    print(bin(a)[2:])                   # bin()以二进制形式输出
    b = a >> 4
    print(bin(b)[2:])
    c = ~(~0 << 4)
    print(bin(c)[2:])
    d = b & c
    print "%o\t%o"%(a,d)