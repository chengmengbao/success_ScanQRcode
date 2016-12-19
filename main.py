# !/usr/bin/env python
# -*- coding: UTF-8 -*-
# main.py


import pic
import parse
import time

i = 1

while True:
    
    main_t1 = time.time()

    input_str = raw_input("输入命令：")

    if ( 'c' == input_str ):
        pic.take_pic(i)
        parse.lesen(i)
        i += 1
        print "#############################################"

    elif ( 'q' == input_str ):
        print "结束"
        break

    elif ( 'c -n 100' == input_str ):
        for n in range(10):
            pic.take_pic(i)
            parse.lesen(i)
            i += 1
            print "#############################################"

    elif ( 'c -n 50' == input_str ):
        for n in range(5):
            pic.take_pic(i)
            parse.lesen(i)
            i += 1
            print "#############################################"
    else:
        print "输入命令错误！！！"
    main_t2 = time.time()
    # print "主程序运行时间=%f" % (main_t2-main_t1)


