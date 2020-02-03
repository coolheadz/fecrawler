# -*- coding: utf-8 -*-
import scrapy
from urllib import parse
import json 
from ..items import FecrawlerItem

url = 'https://digital.feprecisionplus.com/ChartData/ChartingData/GetPerformanceDataByTypeCodes/ayers?languageId=3&TypeCodes={}~1%2CXHM%3AAXJ&PriceType=1&MethodType=1&CumulativePerformancePeriodEndType=c&DiscretePerformancePeriodPeriodEndType=m&CurrencyCode=&GrsProjectId=17200132&ProjectName=ayers&ThemeName=ayershk&LanguageCode=zh-sg&SpecialUnitType=&SpecialUnitSetting=0&ProjectRangeId='


class FeSpider(scrapy.Spider):
    name = 'fe'
    allowed_domains = ['digital.feprecisionplus.com']
    custom_settings = {
        'ITEM_PIPELINES': {
            'feCrawler.pipelines.FecrawlerPipeline': 300
        }
    }
    start_urls = []
    codes = {}

    def __init__(self):
        with open('ISIN_TypeCode.txt', 'r') as f:
            for line in f.readlines(): 
                c = line.strip().split(',')
                if len(c) == 2 and c[1]:
                    self.start_urls.append(url.format(parse.quote_plus(c[1])))
                    self.codes[c[1]] = c[0]
        

    def parse(self, response):
        result = json.loads(response.text)
        if 'InstrumentPerformances' in result.keys() and len(result['InstrumentPerformances']) == 2:
            yield FecrawlerItem(
                code=self.codes[result['InstrumentPerformances'][0]['TypeCode']],
                name=result['InstrumentPerformances'][0]['Instrument'],
                ytd=result['InstrumentPerformances'][0]['CumulativePerformance']['YTD'],
                one_yr=result['InstrumentPerformances'][0]['CumulativePerformance']['_1y'],
                three_yr=result['InstrumentPerformances'][0]['CumulativePerformance']['_3y'],
                five_yr=result['InstrumentPerformances'][0]['CumulativePerformance']['_5y'])

