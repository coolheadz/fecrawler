# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class FecrawlerPipeline(object):
    file = None

    def __init__(self):
        super().__init__()

    def open_spider(self, spider):
        self.file = open('result.csv', 'w', encoding='UTF-8-sig')
        self.file.write('code, name, ytd, 1yr, 3yr, 5yr\n')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        self.file.write('{},{},{},{},{},{}\n'.format(item['code'], item['name'], item['ytd'], item['one_yr'], item['three_yr'], item['five_yr']))
        return item


class TypecodePipeline(object):
    file = None

    def __init__(self):
        super().__init__()

    def open_spider(self, spider):
        self.file = open('ISIN_TypeCode.txt', 'w', encoding='UTF-8')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        self.file.write('{},{}\n'.format(item['isin'], item['typecode']))
        return item