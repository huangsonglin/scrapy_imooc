#!user/bin/python
#-*- coding: utf-8 -*-
__author__: 'huangsonglin@dcpai.cn'
__Time__: '2019/6/27 18:22'


import sys
import os
import time
from scrapy.cmdline import execute
import os
os.system("scrapy crawl mk_classfy")
time.sleep(10)
os.system("scrapy crawl mk")
