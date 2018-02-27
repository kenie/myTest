#!/usr/bin/env python
#-*- coding:UTF-8 -*-

'''题目：找到年龄最大的人，并输出。请找出程序中有什么问题。'''

if __name__ == "__main__":
    person = {"li":18,"liu":22,"yang":25,"xie":19,"huang":29,"chu":17}
    m = "li"
    for key in person.keys():
        if person[m] < person[key]:
            m = key

    print "%s,%d"%(m,person[m])