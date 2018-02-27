#!/usr/bin/env python
#-*- coding:UTF-8 -*-

'''题目：按逗号分隔列表。'''

s = ['one','two','three','five']
for i in range(len(s)):
    print "%s,"%s[i],

'''答案：'''
L = [1,2,3,4,5,6,7]
s1 = ','.join(str(n) for n in L)
print s1