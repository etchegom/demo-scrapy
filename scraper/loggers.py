import logging
from typing import Any

from scrapy import Spider, logformatter
from scrapy.http import Response


class CustomLogFormatter(logformatter.LogFormatter):
    def dropped(
        self, item: Any, exception: Exception, response: Response, spider: Spider
    ) -> dict:
        return {
            "level": logging.ERROR,
            "msg": logformatter.DROPPEDMSG,
            "args": {"exception": exception, "item": item.get("url", item)},
        }
