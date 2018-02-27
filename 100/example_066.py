#!/usr/bin/env python
#-*- coding:UTF-8 -*-

'''题目：输入3个数a,b,c,按大小顺序输出。'''

def Change(a):
    '''for i in range(0,len(a)):            # 不能比较不同位数
        for j in range(0,i):
            if a[i] < a[j]:
                a[i],a[j] = a[j],a[i]'''
    for i in range(len(a)):
        print min(a),
        a.remove(min(a))

if __name__ == "__main__":
    a = []
    for i in range(3):
        b = raw_input("输入第%d个数："%(i+1))
        a.append(b)
    Change(a)
