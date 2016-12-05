# !/usr/bin/env python
# -*- coding: UTF-8 -*-
# parse.py

import zbar
import Image
import os
import picamera
import time
# import io

# create a reader
scanner = zbar.ImageScanner()
# configure the reader
scanner.parse_config('enable')

# 解二维码
def lesen(i):
    parse_t0 = time.time()

    # obtain image data
    pil = Image.open("/home/pi/camera_zbarcode/pic%d.jpg" % i).convert('L')
    width, height = pil.size
    print(width, height)
    raw = pil.tostring()
    
    parse_t1 = time.time()
    print "打开图片花费时间=%f" % (parse_t1-parse_t0)

    # my_stream = io.BytesIO()
    # camera.capture(my_stream, 'jpeg')
    # pil = Image.open(io.BytesIO(my_stream.getvalue())).convert('L')

    # wrap image data
    image = zbar.Image(width, height, 'Y800', raw)

    # scan the image for barcodes
    scanner.scan(image)

    parse_t2 = time.time()
    print "扫描图片花费时间=%f" % (parse_t2 - parse_t1)

    # extract result
    t = None
    for symbol in image:
        t = symbol
        # do something useful with results
        print 'decodef', symbol.type, 'symbol', '''%s''' % symbol.data
    if not t:
        print "解码不成功或未扫描到二维码"
        # os.remove("pic%d.jpg" % i)
    else:
        print "解码成功"
        os.rename("pic%d.jpg" % i, "pic_success%d.jpg" % i)

    parse_t3 = time.time()
    print "解码花费时间=%f" % (parse_t3 - parse_t2)

    # clean up
    del (image)