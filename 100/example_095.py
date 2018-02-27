#!/usr/bin/env python
#-*- coding:UTF-8 -*-

'''题目：字符串日期转换为易读的日期格式。'''

from dateutil import parser
dt = parser.parse("Aug 28 2018 12:00AM")
print dt