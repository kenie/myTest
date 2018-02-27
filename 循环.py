#!/usr/bin/python
# -*- coding:UTF-8 -*-

i = 2
while (i < 100):
    j = 2
    while (j <= (i/j)):
        if not(i%j):break
        j = j + 1
    if(j > (i/j)):print i," 是素数"
    i = i + 1

for letter in 'python':
    if letter == 'h':
        break
    print "当前字母: ",letter

var = 10
while var > 0:
    print "当前数字：",var
    var = var - 1
    if var == 5:
        break

for letter in "Python":
    if letter == "h":
        pass
    print "当前字母：",letter