 # Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field

class MoviescraperItem(scrapy.Item):
        title = Field()
        original_title = Field()
        imdb = Field()
        country = Field()
        duration = Field()
        description = Field()

