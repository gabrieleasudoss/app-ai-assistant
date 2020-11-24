# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    short_desc = scrapy.Field()
    full_title = scrapy.Field()
    author = scrapy.Field()
    url = scrapy.Field()
    tag = scrapy.Field()
    time = scrapy.Field()
    place = scrapy.Field()
    story = scrapy.Field()
    pass
