#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os

import logging
import argparse
from waveshare_epd import epd7in5_V2
from PIL import Image,ImageDraw,ImageFont
#import traceback

#logging.basicConfig(level=logging.DEBUG)

def draw_text(text_to_print,font_size=24):
    epd = epd7in5_V2.EPD()
    epd.init()
#    epd.Clear()

    font = ImageFont.truetype('DejaVuSansMono.ttf', font_size)

    Himage = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(Himage)
    #draw.text((10, 0), text_to_print, font = font, fill = 0)
    #if partial:
    #    epd.init_fast()
    #    offsets = [int(n) for n in args.partial.split(",")]
    #    draw.rectangle((offsets[0],offsets[1],offsets[2],offsets[3]), fill=255)
    #    draw.text((offsets[0],offsets[1]), text_to_print, font = font, fill = 0)
    #    epd.display_Partial(epd.getbuffer(Himage),offsets[0],offsets[1],offsets[2],offsets[3])
    #else:
    draw.text((10, 0), text_to_print, font = font, fill = 0)
    epd.display(epd.getbuffer(Himage))
    #epd.display_Partial(epd.getbuffer(Himage),0, 0, epd.width, epd.height)
    return

if __name__=='__main__':
#    print('main')
    parser = argparse.ArgumentParser()
    parser.add_argument('--font_size', dest='font_size', default=24, type=int, help='Set font size. Default 24')
    #parser.add_argument('--partial', dest='partial', type=str, help='insert text with as region StartX,StartY,EndX,Endy')
    args = parser.parse_args()
    text_to_print = ''
    for line in sys.stdin:
        text_to_print += line
    draw_text(text_to_print,args.font_size)
