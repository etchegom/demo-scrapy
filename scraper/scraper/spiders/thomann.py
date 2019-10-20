# -*- coding: utf-8 -*-

from typing import Generator

from scrapy import Selector, Spider
from scrapy.http import Request, Response

from scraper.items import ScraperItem


class ThomannSpider(Spider):
    name = "thomann"
    allowed_domains = ["https://www.thomann.de/"]
    start_urls = ["https://www.thomann.de/fr/modeles_en_t.html"]

    def parse(self, response: Response) -> Generator[Request, None, None]:
        sel = Selector(response, type="html")

        article_xpath = '//div[contains(@class, "extensible-article")]'
        title_parts = sel.xpath(
            '{}//div[contains(@class, "title-block")]/span/text()'.format(article_xpath)
        ).getall()

        item = ScraperItem()
        item["url"] = response.url
        item["title"] = "".join(title_parts)
        yield item
