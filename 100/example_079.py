#!/usr/bin/env python
#-*- coding:UTF-8 -*-

'''题目：字符串排序。'''

if __name__ == "__main__":
    str1 = raw_input("input string:")
    str2 = raw_input("input string:")
    str3 = raw_input("input string:")
    print str1,str2,str3

    if str1 > str2 :str1,str2 = str2,str1
    if str1 > str3 :str1,str3 = str3,str1
    if str2 > str3 :str2,str3 = str3,str2
    print str1,str2,str3