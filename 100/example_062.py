#!/usr/bin/env python
#-*- coding:UTF-8 -*-

'''题目：查找字符串。'''

s = raw_input("请输入字符串：")
str = raw_input("输入你需要查找的字符串：")
print "原字符串为：%s\n需要查找的字符串为：%s  在原字符串的第%d位置！"%(s,str,s.find(str))