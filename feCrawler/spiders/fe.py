# -*- coding: utf-8 -*-
import scrapy
from urllib import parse
import json 
from items import FecrawlerItem

url = 'https://digital.feprecisionplus.com/ChartData/ChartingData/GetPerformanceDataByTypeCodes/ayers?languageId=3&TypeCodes={}~1%2CXHM%3AAXJ&PriceType=1&MethodType=1&CumulativePerformancePeriodEndType=c&DiscretePerformancePeriodPeriodEndType=m&CurrencyCode=&GrsProjectId=17200132&ProjectName=ayers&ThemeName=ayershk&LanguageCode=zh-sg&SpecialUnitType=&SpecialUnitSetting=0&ProjectRangeId='


class FeSpider(scrapy.Spider):
    name = 'fe'
    allowed_domains = ['digital.feprecisionplus.com']
    code = ['LU0797268264', 'FHM:IVASCS',]
    start_urls = []

    def __init__(self):
        for c in self.code:
            self.start_urls.append(url.format(parse.quote_plus(c)))
        

    def parse(self, response):
        result = json.loads(response.text)
        if 'InstrumentPerformances' in result.keys() and len(result['InstrumentPerformances']) == 2:
            yield FecrawlerItem(
                code=result['InstrumentPerformances'][0]['TypeCode'],
                one_yr=result['InstrumentPerformances'][0]['CumulativePerformance']['_1y'],
                three_yr=result['InstrumentPerformances'][0]['CumulativePerformance']['_3y'],
                five_yr=result['InstrumentPerformances'][0]['CumulativePerformance']['_5y'],
                ten_yr=result['InstrumentPerformances'][0]['CumulativePerformance']['_10y'])
        
        pass
