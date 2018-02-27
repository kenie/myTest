#!/usr/bin/env python
#-*- coding:UTF-8 -*-

'''题目：数字比较。'''

if __name__ == "__main__":
    i = int(raw_input("输入第一个数："))
    j = int(raw_input("输入第二个数："))
    if i > j:
        print "%d 大于 %d" %(i,j)
    elif i == j:
        print "%d 等于 %d" %(i,j)
    elif i < j:
        print "%d 小于 %d" %(i,j)
    else:
        print "未知！？"