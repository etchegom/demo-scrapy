# -*- coding: utf-8 -*-

import os
from typing import List

BOT_NAME = "demo-scraper"
ROBOTSTXT_OBEY = True

SPIDER_MODULES = ["scraper.spiders"]
NEWSPIDER_MODULE = "scraper.spiders"

CONCURRENT_REQUESTS = 4

HASH_FIELDS = ("url",)
REQUIRED_FIELDS = ("url", "title")

# PostgreSQL
PG_SETTINGS = {
    "user": os.getenv("POSTGRES_USER", "scraper"),
    "passwd": os.getenv("POSTGRES_PASSWORD", "password"),
    "host": os.getenv("POSTGRES_HOST", "localhost"),
    "port": os.getenv("POSTGRES_PORT", "5432"),
    "db_name": os.getenv("POSTGRES_DB", "scraper"),
}

# Logging
LOG_ENABLED = True
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FORMATTER = "scraper.loggers.CustomLogFormatter"

# Pipelines
ITEM_PIPELINES = {
    "scraper.pipelines.CheckerPipeline": 300,
    "scraper.pipelines.HasherPipeline": 400,
    "scraper.pipelines.PGPipeline": 500,
    "scraper.pipelines.PrinterPipeline": 600,
}

# Middlewares
DOWNLOADER_MIDDLEWARES = {
    "scrapy.downloadermiddleware.useragent.UserAgentMiddleware": None,
    "scraper.middlewares.RandomUserAgentMiddleware": 400,
    "scraper.middlewares.BlacklistMiddleware": 500,
    "scraper.middlewares.PGCheckExistMiddleware": 00,
}

USER_AGENT_LIST = [
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A5370a Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko)",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
]

BLACKLIST = []  # type: List[str]

try:
    from .local_settings import *  # noqa
except ImportError:
    pass
