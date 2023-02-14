# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EcapepiaScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # avgPrice_1p = scrapy.Field()
    # avgPrice_1 = scrapy.Field()
    # avgPrice_2 = scrapy.Field()
    # avgPrice_off = scrapy.Field()
    # avgPrice_offX = scrapy.Field()
    grade = scrapy.Field()
    avgPrice = scrapy.Field()
    avgWeight = scrapy.Field()
    totalWeight = scrapy.Field()

    pass
