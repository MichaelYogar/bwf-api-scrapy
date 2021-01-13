# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from scrapy.item import Item, Field
from scrapy.loader.processors import MapCompose, TakeFirst
from datetime import datetime


class ApiItem(Item):
    rank = Field()
    country = Field()
    player = Field()
    rank_change = Field()
    win_loss = Field()
    prize =  Field()
    points = Field() 
    category = Field()
    parsed_url = Field()
