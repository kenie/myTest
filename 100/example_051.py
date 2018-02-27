#!/usr/bin/env python
#-*- coding:UTF-8 -*-

'''题目：学习使用按位与&。
程序分析：0&0=0,0&1=0,1&0=0,1&1=1.'''

if __name__ == "__main__":
    a = 077                     # 077 = 0000 0011 1111      八进制转换为二进制 7 * 8^1 + 7 * 8^0 = 63
    b = a & 3                   # 3   = 0000 0000 0011
    print "a & b = %d" % b
    b &= 7
    print "a & b = %d" % b
