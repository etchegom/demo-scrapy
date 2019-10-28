# -*- coding: utf-8 -*-

import os

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

ITEM_PIPELINES = {
    "scraper.pipelines.CheckerPipeline": 300,
    "scraper.pipelines.HasherPipeline": 400,
    "scraper.pipelines.PGPipeline": 500,
    "scraper.pipelines.PrinterPipeline": 600,
}

# Middlewares
DOWNLOADER_MIDDLEWARES = {"scraper.middlewares.PGCheckExistMiddleware": 500}


try:
    from .local_settings import *  # noqa
except ImportError:
    pass
