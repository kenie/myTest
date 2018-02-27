#!/usr/bin/env python
#-*- coding:UTF-8 -*-

'''题目：时间函数举例。'''

# 例子一
'''if __name__ == "__main__":
    import time
    print time.ctime(time.time())
    print time.asctime(time.localtime(time.time()))
    print time.asctime(time.gmtime(time.time()))'''

# 列子二
'''if __name__ == "__main__":
    import time
    start = time.time()
    for i in range(3000):
        print i
    end = time.time()

    print end - start'''

# 例子三
if __name__ == "__main__":
    import time
    start = time.clock()
    for i in range(10000):
        print i
    end = time.clock()
    print "different is %6.3f "%(end - start)