from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher
from scrapy import signals
import datetime

from NewsArticlesScraper.Scrapers import TheGuardianSpider


def _print(item):
    if item["title"] == "" or item["author_name"] == "":
        print(item)


def main():
    dispatcher.connect(_print, signal=signals.item_passed)
    crawler = CrawlerProcess()
    crawler.crawl(TheGuardianSpider, datetime.datetime.fromtimestamp(1617235200), datetime.datetime.fromtimestamp(1617321600))
    crawler.start()


if __name__ == "__main__":
    main()
