#!/usr/bin/env python
#-*- coding:UTF-8 -*-

'''题目：输入一行字符，分别统计出其中的英文字母、空格、数字和其他字符的个数。
程序分析：利用while语句，条件为输入的字符不为'\n'。'''

import string
str = raw_input('Input a string：\n')
letters = 0
space = 0
digit = 0
others = 0
for i in str:
    if i.isalpha():
        letters += 1
    elif i.isdigit():
        digit += 1
    elif i.isspace():
        space += 1
    else:
        others += 1
print "char = %d,space = %d,digit = %d,others = %d." %(letters,space,digit,others)
