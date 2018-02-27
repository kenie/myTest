#!/usr/bin/env python
#-*- coding:UTF-8 -*-

'''题目：反向输出一个链表。'''

if __name__ == "__main__":
    ptr = []
    for i in range(5):
        num = raw_input("Please input a number:")
        ptr.append(num)
    ptr.reverse()               # 反向链表
    print ptr
