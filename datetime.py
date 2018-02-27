#!/usr/bin/python
# -*- coding:UTF-8 -*-

import time         #引入time模块

ticks = time.time()
print "当前时间截：",ticks

location = time.localtime(time.time())
print "本地时间为：",location

localtime = time.asctime(time.localtime(time.time()))
print "本地时间为：",localtime

#格式化成2017-12-11 11:45:39形式
print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())