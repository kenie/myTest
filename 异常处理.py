#!/usr/bin/env python
#-*- coding:UTF-8 -*-

try:
    fp = open('test.txt','w')
    fp.write('这是一个测试文件，用于测试异常!')
except IOError:
    print "Error:没有找到文件或读取文件失败！"
else:
    print "内容写入文件成功！"
    fp.close()
