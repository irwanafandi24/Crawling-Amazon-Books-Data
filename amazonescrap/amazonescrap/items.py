# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonescrapItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    titles = scrapy.Field()
    authors = scrapy.Field()
    ratings = scrapy.Field()
    prices = scrapy.Field()
    image_urls = scrapy.Field()
    pass
