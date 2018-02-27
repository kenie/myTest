#!/usr/bin/python
# -*- coding:UTF-8 -*-

import calendar

cal = calendar.month(2017,12)
print "以下输出2017年12月份的日历："
print cal

count = calendar.leapdays(1999,2017)
print count