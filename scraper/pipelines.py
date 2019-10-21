# -*- coding: utf-8 -*-

from pprint import pformat
from typing import Tuple

from scrapy import Spider
from scrapy.exceptions import DropItem
from sqlalchemy.exc import InvalidRequestError

import scraper.database as db
from scraper import utils
from scraper.items import ScraperItem
from scraper.models import ScraperItemModel


class PrinterPipeline(object):
    def process_item(self, item: ScraperItem, spider: Spider) -> ScraperItem:
        spider.log(pformat(dict(item), indent=4))
        return item


class CheckerPipeline(object):
    """
    Pipeline in charge of checking scraped fields.
    """

    def __init__(self, required_fields: Tuple[str]):
        self.required_fields = required_fields

    @classmethod
    def from_crawler(cls, crawler):  # type: ignore
        return cls(required_fields=crawler.settings.get("REQUIRED_FIELDS"))

    def process_item(self, item: ScraperItem, spider: Spider) -> ScraperItem:
        for field in self.required_fields:
            if item.get(field, None) is None:
                raise DropItem("Missing field {} in {}".format(field, item))
        return item


class HasherPipeline(object):
    """
    Pipeline in charge of building hash fields from existing fields.
    """

    def __init__(self, hash_fields: Tuple[str]):
        self.hash_fields = hash_fields

    @classmethod
    def from_crawler(cls, crawler):  # type: ignore
        return cls(hash_fields=crawler.settings.get("HASH_FIELDS"))

    def process_item(self, item: ScraperItem, spider: Spider) -> ScraperItem:
        for field in self.hash_fields:
            item["{}_hash".format(field)] = utils.hash_value(item[field])
        return item


class PGPipeline(object):
    """
    Pipeline in charge of recording items into POstgreSQL database.
    """

    def __init__(self, pg_settings: dict):
        self.session_factory = db.session_factory(pg_settings)

    @classmethod
    def from_crawler(cls, crawler):  # type: ignore
        return cls(pg_settings=crawler.settings.get("PG_SETTINGS"))

    def process_item(self, item: ScraperItem, spider: Spider) -> ScraperItem:
        session = self.session_factory()
        try:
            record = db.get_item(session=session, url_hash=item["url_hash"])
            if record:
                record.update(**dict(item))  # type: ignore
            else:
                record = ScraperItemModel()
                record.update(**dict(item))  # type: ignore
                session.add(record)
            session.commit()
        except InvalidRequestError:
            session.rollback()
            raise
        finally:
            session.close()
        return item
