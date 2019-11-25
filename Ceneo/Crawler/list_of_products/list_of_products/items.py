# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# Tutaj po prostu okreslamy pola jakie chcemy crawlowac.
class ListOfProductsItem(scrapy.Item):
    name_of_object = scrapy.Field()
    price_one_product = scrapy.Field()
    website_link = scrapy.Field()
    # price_one_product_with_delivery = scrapy.Field()
    shop_rating = scrapy.Field()
    number_of_reviews = scrapy.Field()