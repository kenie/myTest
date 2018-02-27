#!/usr/bin/env python
#-*- coding:UTF-8 -*-

'''题目：对10个数进行排序
程序分析：可以利用选择法，即从后9个比较过程中，选择一个最小的与第一个元素交换，
下次类推，即用第二个与后8个进行比较，并进行交换。'''

if __name__ == "__main__":
    N = 10
    print "*****输入10个数字*****"
    L = []
    for i in range(N):
        i += 1
        d = int(raw_input("输入第%d个数："%i))
        L.append(d)
    print
    for i in range(N):
        print L[i],
    print

    # 排序10个数字
    for i in range(N - 1):
        min = i
        for j in range(i+1,N):
            if L[min] > L[j]:min = j
        L[i],L[min] = L[min],L[i]
    print "*****排序之后*****"
    for i in range(N):
        print L[i],