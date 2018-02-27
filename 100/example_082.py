#!/usr/bin/env python
#-*- coding:UTF-8 -*-

'''题目：八进制转换为十进制。'''

if __name__ == "__main__":
    n = 0
    p = raw_input("input a octal number:")
    for i in range(len(p)):
        print "ord('p[i]'):",ord(p[i])
        print "ord('0'):",ord("0")
        n = n * 8 + ord(p[i]) - ord("0")
    print n