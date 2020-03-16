# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
from scrapy.exceptions import DropItem
import urllib.parse

class CheapScraperPipeline(object):
    def process_item(self, item, spider):
        pattern = '^https\S*q=(\S*)&num=100$'
        regex_result = re.match(pattern, item['url'])
        item['keyword'] = regex_result.group(1).replace("+", " ")
        item['keyword'] = urllib.parse.unquote(item['keyword'])
        return item