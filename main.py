#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os

import logging
from waveshare_epd import epd7in5_V2
from PIL import Image,ImageDraw,ImageFont
#import traceback

#logging.basicConfig(level=logging.DEBUG)

def main():
    text_to_print = ''
    for line in sys.stdin:
        text_to_print += line
    epd = epd7in5_V2.EPD()
    epd.init()
#    epd.Clear()

    font = ImageFont.truetype('DejaVuSansMono.ttf', 24)

    epd.init_fast()
    Himage = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(Himage)
    draw.text((10, 0), text_to_print, font = font, fill = 0)
    epd.display(epd.getbuffer(Himage))
    #epd.display_Partial(epd.getbuffer(Himage),0, 0, epd.width, epd.height)
    return

if __name__=='__main__':
#    print('main')
    main()
