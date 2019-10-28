# -*- coding: utf-8 -*-

from typing import Generator, Optional

from scrapy import Selector, Spider
from scrapy.http import Request, Response

from scraper import utils
from scraper.items import ScraperItem


class ThomannSpider(Spider):
    name = "thomann"
    allowed_domains = ["thomann.de"]
    start_urls = ["https://www.thomann.de/fr/modeles_en_t.html"]

    def parse(self, response: Response) -> Generator[Request, None, None]:
        sel = Selector(response, type="html")
        for url in sel.xpath('//div[@id="defaultResultPage"]//a/@href').getall():
            yield Request(url=url, callback=self.product_page_cb)

            # FIXME: to remove after dev
            break

    def product_page_cb(self, response: Response) -> Optional[ScraperItem]:
        sel = Selector(response, type="html")

        # metadata can help extracting more reliable data (json-ld, microdata, ...)
        meta = utils.extract_metadata(url=response.url)
        self.logger.info(meta)

        item = ScraperItem()
        item["url"] = response.url
        item["title"] = sel.xpath("//h1/text()").get()
        yield item
