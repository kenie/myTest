#!/usr/bin/env python
#-*- coding:UTF-8 -*-

d = []
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i != j) and (j != k) and (i !=k):
                d.append([i,j,k])
                print i,j,k

print "总数量：",len(d)