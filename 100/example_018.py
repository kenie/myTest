#!/usr/bin/env python
#-*- coding:UTF-8 -*-

'''题目：求s=a+aa+aaa+aaaa+aa..a的值，其中a是一个数字，例如2+22+222+2222+22222(此时共有5个数相加)，几个数
相加由键盘控制。
程序分析：关键是计算出每一项的值。'''

Tn = 0
Sn = []
a = int(raw_input('输入一个数：'))
n = int(raw_input('输入需要相加的项个数：'))
for count in range(n):
    Tn = Tn + a
    a = a * 10
    Sn.append(Tn)
    print Tn
Sn = reduce(lambda x,y:x+y,Sn)
print "求和为：",Sn
