import scrapy
import csv
from ..items import CheapScraperItem

class CheapCrawler(scrapy.Spider):
    name = "cheap_spider"

    def parse(self, response):
        items = CheapScraperItem()
        
        rank = 1 
        links = response.css('div.g div.rc div.r a')

        for link in links:
            ranking_link = link.css("a::attr(href)").get()
            url = response.request.url
            if ranking_link != "#" and '/search?q=' not in ranking_link:
                items['url'] = url
                items['link'] = ranking_link
                items['rank'] = rank
            
                rank += 1
                yield items