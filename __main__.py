#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
libdir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(libdir)
sys.path.append(os.path.join(libdir,'lib'))

from main import main

if __name__=='__main__':
    main()
