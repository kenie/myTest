#!/usr/bin/env python
#-*- coding:UTF-8 -*-

'''题目：请输入星期几的第一个字母判断一下是星期几，如果第一个字母一样，则判断第二个字母。
程序分析：用情况语句比较好，如果第一个字母一样，则判断用情况语句或if语句判断第二个字母。'''

s = raw_input("请输入第一个字母：")
if str(s) == 'M':
    print "输入的是星期一（Monday）！"
elif str(s) == 'T':
    s2 = raw_input("请输入第二个字母：")
    if str(s2) == 'u':
        print "输入的是星期二（Tuesday)！"
    elif str(s2) == 'h':
        print "输入的是星期四（Thursday）！"
    else:
        print "输入有误！"
elif str(s) == 'W':
    print "输入的是星期三（Wednesday）！"
elif str(s) == 'F':
    print "输入的是星期五（Friday）！"
elif str(s) == 'S':
    s2 = raw_input("请输入第二个字母：")
    if str(s2) == 'a':
        print "输入的是星期六（Saturday）！"
    elif str(s2) == 'u':
        print "输入的是星期日（Sunday）！"
    else:
        print "输入有误！"
else:
    print "输入有误！"

