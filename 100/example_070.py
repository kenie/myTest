#!/usr/bin/env python
#-*- coding:UTF-8 -*-

'''题目：写一个函数，求一个字符串的长度，在main函数中输入字符串，并输出其长度。'''

def calc(str):
    return len(str)

if __name__ == "__main__":
    str = raw_input("请输入需要计算的字符串：")
    print "该字符串长度为：",calc(str)