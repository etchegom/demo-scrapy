from scrapy import Field, Item


class ScraperItem(Item):
    url = Field()
    title = Field()
