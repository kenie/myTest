#!/usr/bin/env python
#-*- coding:UTF-8 -*-

'''题目：给一个不多于5位的正整数，要求，一、求它是几位数，二、逆序打印出各位数字。
程序分析：学会分解出每一位数。'''

s = raw_input('Input a number:')
print "数入的数为 %d 位数！" % (len(s))
if len(s) == 1:
    print s
elif len(s) == 2:
    s1 = int(s)/10
    s2 = int(s)%10
    print "逆序为 %d,%d: " %(s2,s1)
elif len(s) == 3:
    s1 = int(s)/100
    s2 = int(s)%100/10
    s3 = int(s)%10
    print "逆序为 %d,%d,%d: " %(s3,s2,s1)
elif len(s) == 4:
    s1 = int(s)/1000
    s2 = int(s)%1000/100
    s3 = int(s)%100/10
    s4 = int(s)%10
    print "逆序为 %d,%d,%d,%d: " %(s4,s3,s2,s1)
elif len(s) == 5:
    s1 = int(s)/10000
    s2 = int(s)%10000/1000
    s3 = int(s)%1000/100
    s4 = int(s)%100/10
    s5 = int(s)%10
    print "逆序为 %d,%d,%d,%d,%d: " %(s5,s4,s3,s2,s1)
else:
    print"数入不符合！"

'''答案:
x = int(raw_input("请输入一个数:\n"))
a = x / 10000
b = x % 10000 / 1000
c = x % 1000 / 100
d = x % 100 / 10
e = x % 10

if a != 0:
    print "5 位数：",e,d,c,b,a
elif b != 0:
    print "4 位数：",e,d,c,b,
elif c != 0:
    print "3 位数：",e,d,c
elif d != 0:
    print "2 位数：",e,d
else:
    print "1 位数：",e'''