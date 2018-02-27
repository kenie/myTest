#!/usr/bin/env python
#-*- coding:UTF-8 -*-

'''题目：求一个3*3矩阵主对角线元素之和
程序分析：利用双重for循环控制输入二维数组，再将a[i][j]累加后输出。'''

if __name__ == "__main__":
    a = []
    sum = 0.0
    for i in range(3):
        a.append([])
        for j in range(3):
            a[i].append(float(raw_input("输入第%d行第%d个数："%(i+1,j+1))))
    for i in range(3):
        print
        for j in range(3):
            print a[i][j],
    print
    for i in range(3):
        sum += a[i][i]
    print "主对角线和为%d :"%sum