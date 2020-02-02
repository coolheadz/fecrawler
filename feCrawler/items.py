# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FecrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    code = scrapy.Field()
    one_yr = scrapy.Field()
    three_yr = scrapy.Field()
    five_yr = scrapy.Field()
    ten_yr = scrapy.Field()
    pass
