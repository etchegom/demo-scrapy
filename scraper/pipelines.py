# -*- coding: utf-8 -*-

from pprint import pformat

from scrapy import Spider

from scraper.items import ScraperItem


class PrinterPipeline(object):
    def process_item(self, item: ScraperItem, spider: Spider) -> ScraperItem:
        spider.log(pformat(dict(item), indent=4))
        return item
