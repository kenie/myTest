#!/usr/bin/env python
#-*- coding:UTF-8 -*-

'''题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数据中。
程序分析：首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况，插入后此元素之后的数，依次后移一个位置。'''

if __name__ == "__main__":
    # 方法一：0 作为加入数字的占位符
    a = [1,4,6,9,13,16,19,28,40,100]
    print "*****原始数列*****"
    for i in range(len(a)):
        print a[i],
    print
    number = int(raw_input("请输入一个数："))
    a.append(number)
    end = a[9]
    if number > end:
        a[10] = number
    else:
        for i in range(10):
            if a[i] > number:
                temp1 = a[i]
                a[i] = number
                for j in range(i + 1,11):
                    temp2 = a[j]
                    a[j] = temp1
                    temp1 = temp2
                break
    print "*****排序后数列*****"
    for i in range(11):
        print a[i],

'''print "*****原始数列*****"
a = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29]
c = a[:]
l = len(c)
for i in range(l):
   print a[i],
print

b = int(raw_input("请输入一个数："))
a.append(b)

# 从后面开始，如果比倒数第二个数大，那就将新加入的数填在倒数第一的位置，否则倒数第二的数位置后移
for i in range(l,0,-1):
   if (b > c[i-2]):
      c[i-1] = b
      break
   else:
      c[i-1] = c[i-2]
print "****排序后的数列****\n",c'''