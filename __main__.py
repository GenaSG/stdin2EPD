#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
import argparse
libdir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(libdir)
sys.path.append(os.path.join(libdir,'lib'))

from main import draw_text

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--font_size', dest='font_size', default=24, type=int, help='Set font size. Default 24')
    #parser.add_argument('--partial', dest='partial', type=str, help='insert text with as region StartX,StartY,EndX,Endy')
    args = parser.parse_args()
    text_to_print = ''
    for line in sys.stdin:
        text_to_print += line
    draw_text(text_to_print,args.font_size)
