#!/usr/bin/env python
#-*- coding:UTF-8 -*-

'''题目：利用条件运算符的嵌套来完成此题，学习成绩>=90分的同学用A表示，60-89分的同学用B表示，60分以下的用C表示。
程序分析：（a>b)?a:b这是条件运算符的基本例子'''

score = int(raw_input('请输入分数：'))
if score < 60:
    print "C"
elif score >=90:
    print "A"
else:
    print "B"