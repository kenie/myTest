#!/usr/bin/env python
#-*- coding:UTF-8 -*-

'''题目：将一个数组逆序输出。
程序分析：用第一个与最后一个交换。'''

'''if __name__ == "__main__":
    a = [9,5,6,8,7,2,4,3]
    N = len(a)
    print "*****原始数组*****"
    for i in range(N):
        print a[i],
    print
    print "*****逆序后数组*****"
    for i in range(N):
        print a[-i-1],
    print'''

'''答案：'''
if __name__ == "__main__":
    a = [9,5,6,8,7,2,4,3]
    N = len(a)
    print a,
    print
    for i in range(N/2):
        a[i],a[N-i-1] = a[N-i-1],a[i]
    print a,
    print