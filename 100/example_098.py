#!/usr/bin/env python
#-*- coding:UTF-8 -*-

'''题目：从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件’test'中保存。'''

if __name__ == "__main__":
    filename = raw_input("请输入文件名：")
    fp = open(filename,'w')
    str = raw_input("请输入字符串：")
    fp.write(str.upper())
    fp = open(filename,'r')
    print fp.read()
    fp.close()
