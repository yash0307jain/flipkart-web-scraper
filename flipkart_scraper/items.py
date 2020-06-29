# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Laptop(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # page = scrapy.Field()
    url = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    highlight = scrapy.Field()
    specification = scrapy.Field()
    rating = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
