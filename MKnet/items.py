# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MknetItem(scrapy.Item):
    # 课程名字
    class_name = scrapy.Field()
    # 课程描述
    class_desc = scrapy.Field()
    # 课程困难程度
    class_lev = scrapy.Field()
    # 课程分类
    class_classfy = scrapy.Field()
    # 课表内容
    every_class_name = scrapy.Field()
    # 课程视频url
    video_url = scrapy.Field()
    # 课程详情页
    class_url = scrapy.Field()
    # 课程价格
    class_price = scrapy.Field()


class ClassFyItem(scrapy.Item):
    # 分类名字
    classify_name = scrapy.Field()
    # 分类url
    classify_url = scrapy.Field()
