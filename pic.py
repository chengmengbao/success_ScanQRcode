# !/usr/bin/env python
# -*- coding: UTF-8 -*-
# pic.py


import picamera
import time

# 摄像头初始化
camera = picamera.PiCamera()
# camera.resolution = (640, 480)
camera.framerate = 30
# camera.annotate_text = "HKUTANGYU.Inc"
# 垂直翻转
camera.vflip = True
# 水平翻转
camera.hflip = True
camera.start_preview()
time.sleep(2)


# 拍照
def take_pic(i):
    pic_t1 = time.time()

    camera.capture('pic%d.jpg' % i)
    print "拍照完成，第%d张" % i

    pic_t2 = time.time()
    # print "拍照花费时间=%f" % (pic_t2-pic_t1)