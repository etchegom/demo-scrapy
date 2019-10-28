from scrapy import Field, Item


class ScraperItem(Item):
    title = Field()
    url = Field()
    url_hash = Field()
