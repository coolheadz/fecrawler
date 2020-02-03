# -*- coding: utf-8 -*-
import scrapy
import json 
from ..items import TypecodecrawlerItem


url = 'https://digitalfundservice.feprecisionplus.com/FundDataService.svc/GetRowIdList?jsonString=%7B%22FilteringOptions%22%3A%7B%22undefined%22%3A0%2C%22SearchText%22%3A%22{}%22%2C%22PerformanceOperator%22%3A%22GREAT%22%2C%22Amc%22%3A%7B%7D%2C%22Yield%22%3A%7B%7D%2C%22RiskScore%22%3A%7B%7D%2C%22FundSize%22%3A%7B%7D%2C%22RangeId%22%3Anull%2C%22RangeName%22%3A%22%22%2C%22CategoryId%22%3Anull%2C%22PriipProductCode%22%3Anull%2C%22DefaultCategoryId%22%3Anull%2C%22ForSaleIn%22%3Anull%2C%22ShowMainUnits%22%3Afalse%2C%22MPCategoryCode%22%3Anull%7D%2C%22ProjectName%22%3A%22ayers%22%2C%22LanguageCode%22%3A%22zh-sg%22%2C%22LanguageId%22%3A%223%22%2C%22Theme%22%3A%22ayershk%22%2C%22SortingStyle%22%3A%221%22%2C%22PageNo%22%3A1%2C%22PageSize%22%3A10%2C%22OrderBy%22%3A%22UnitName%3Ainit%22%2C%22IsAscOrder%22%3Atrue%2C%22OverrideDocumentCountryCode%22%3Anull%2C%22ToolId%22%3A%221%22%2C%22PrefetchPages%22%3A200%2C%22PrefetchPageStart%22%3A1%2C%22OverridenThemeName%22%3A%22ayershk%22%2C%22ForSaleIn%22%3A%22%22%2C%22ValidateFeResearchAccess%22%3Afalse%2C%22HasFeResearchFullAccess%22%3Afalse%2C%22EnableSedolSearch%22%3A%22false%22%2C%22GrsProjectId%22%3A%2217200132%22%2C%22ShowMainUnitExpansion%22%3Afalse%7D'

class TypecodeSpider(scrapy.Spider):
    name = 'typecode'
    allowed_domains = ['digitalfundservice.feprecisionplus.com']
    custom_settings = {
        'ITEM_PIPELINES': {
            'feCrawler.pipelines.TypecodePipeline': 300
        }
    }
    start_urls = []

    def __init__(self):
        with open('ISIN.txt', 'r') as f:
            for line in f.readlines(): 
                codes = line.strip().split(',')
                if len(codes) == 1 or not codes[1]:
                    # code 不存在，需要查找
                    self.start_urls.append(url.format(codes[0])) 
        

    def parse(self, response):
        result = json.loads(response.text)
        if not result['ErrorCode']:
            typecode = json.loads(result['Units'])

            yield TypecodecrawlerItem(
                isin=typecode['DataList'][0]['FundInfo']['ISIN'],
                typecode=typecode['DataList'][0]['FundInfo']['TypeCode'])
        


