#!/usr/bin/env python
#-*- coding:UTF-8 -*-

'''题目：输出一个随机数.'''

import random
a = random.uniform(10,20)   # 输出10-20之间的随机数
b = random.random()         # 输出0-1之间的随机数
c = random.randint(10,20)   # 输出10-20之间的随机整数
print "random.uniform(10,20) = %s\nrandom.random() = %s\nrandom.randint(10,20) = %s"%(a,b,c)