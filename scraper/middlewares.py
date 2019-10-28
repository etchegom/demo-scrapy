# -*- coding: utf-8 -*-

from typing import Optional, Tuple

from scrapy import Spider, signals
from scrapy.exceptions import IgnoreRequest
from scrapy.http import Request, Response

from scraper import database as db
from scraper import utils


class PGCheckExistMiddleware(object):
    def __init__(self, pg_settings: dict):
        self.session_factory = db.session_factory(pg_settings)
        self.force = False

    @classmethod
    def from_crawler(cls, crawler):  # type: ignore
        s = cls(pg_settings=crawler.settings.get("PG_SETTINGS"))
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def spider_opened(self, spider: Spider) -> None:
        self.force = getattr(spider, "force", False)
        spider.logger.info("force option is set to {}".format(self.force))

    def process_request(
        self, request: Request, spider: Spider
    ) -> Optional[Tuple[Response, Request]]:

        if self.force:
            return None

        url_hash = utils.hash_value(request.url)

        session = self.session_factory()
        try:
            if db.item_exists(session=session, url_hash=url_hash):
                spider.logger.info(
                    "item with url_hash {} already exists in database".format(url_hash)
                )
                raise IgnoreRequest()
        except IgnoreRequest:
            session.rollback()
            raise
        finally:
            session.close()

        return None
