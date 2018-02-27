#!/usr/bin/env python
#-*- coding:UTF-8 -*-

from xml.dom.minidom import parse
import xml.dom.minidom

# 使用minidom解析器打开 XML 文档
DOMTree = xml.dom.minidom.parse("movies.xml")
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
    print "Root element : %s" % collection.hasAttribute("shelf")

# 在集合中获取所有电影
movies = collection.getElementsByTagName("movie")

# 打印每部电影的详细信息
for movie in movies:
    print "*****Movie*****"
    if movie.hasAttribute("title"):
        print "Title: %s" % movie.getAttribute("title")

    type = movie.getElementsByTagName('type')[0]
    print "Type: %s" % type.childNodes[0].data
    type = movie.getElementsByTagName('format')[0]
    print "format: %s" % type.childNodes[0].data
    type = movie.getElementsByTagName('rating')[0]
    print "rating: %s" % type.childNodes[0].data
    type = movie.getElementsByTagName('description')[0]
    print "description: %s" % type.childNodes[0].data
