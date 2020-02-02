# -*- coding: utf-8 -*-
import scrapy


class FeSpider(scrapy.Spider):
    name = 'fe'
    allowed_domains = ['digital.feprecisionplus.com']
    start_urls = ['https://digital.feprecisionplus.com/ChartData/ChartingData/GetPerformanceDataByTypeCodes/ayers/']

    def parse(self, response):
        pass
