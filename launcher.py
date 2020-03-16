from scrapy.crawler import CrawlerProcess
from cheap_scraper.spiders import cheap_spider as spider
from scrapy.utils.project import get_project_settings
import pandas as pd
import datetime
import csv

file_path = 'start_urls.csv'

def get_urls(file_path):
    with open(file_path, encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        keyword_list = list(csv_reader)

    start_urls = []
    for keyword in keyword_list:
        url = 'https://www.google.com/search?q=' + keyword[0] + '&num=100'
        start_urls.append(url)
    print(start_urls)
    return start_urls

def run_scraper(start_urls, csv_name):
    settings = get_project_settings()
    process = CrawlerProcess(settings=settings)
    settings.set("FEED_FORMAT","csv")
    settings.set("FEED_URI", csv_name)
    
    start_urls = get_urls('keywords.csv')
    process.crawl(spider.CheapCrawler, start_urls=start_urls)
    process.start()
    process.stop()

def get_filename(name):
    date = datetime.datetime.now().date()
    filename = name + "-" + str(date) + ".csv"
    return filename

def clean_csv(filename):
    df = pd.read_csv(filename)
    df = df[['keyword', 'rank', 'link']]
    df.columns = ['keyword', 'rank', 'url']
    df.sort_values(by=['keyword','rank'], inplace=True)
    df.to_csv(filename, index=False)

filename = get_filename('rankings')
run_scraper(file_path, filename)
clean_csv(filename)