#!/usr/bin/env python
#-*- coding:UTF-8 -*-

'''题目：文本颜色设置'''

class bcolors:
    HEADER = '0\033[095m'
    OKBLUE = '0\033[094m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print bcolors.WARNING + "警告的颜色字体？" + bcolors.ENDC