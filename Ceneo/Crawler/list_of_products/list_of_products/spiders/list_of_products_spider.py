# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess
from list_of_products.items import ListOfProductsItem
from list_of_products.database_connector import connect_old_database

class ListOfProductsSpiderSpider(scrapy.Spider):

    name = 'list_of_products_spider'
    print("Podaj widelki")
    price_min = input()
    price_max = input()
    product_id = connect_old_database(price_min,price_max)
    url = 'http://ceneo.pl' + product_id
    start_urls = [url]

    def parse(self, response):
        items = ListOfProductsItem()
        name_of_object = response.css('.short-name__txt::text').extract()
        price_one_product = response.css('.product-price.go-to-shop .value::text').extract()
        website_link = response.css('.cell-actions .btn-cta::attr(href)').extract()
        shop_rating = response.css('.js_no-conv .score-marker--s::attr(style)').extract()
        # delivery_information = response.css('.offer-content::text').extract()
        # print(delivery_information)
        # print(len(delivery_information))
        number_of_reviews = response.css('.dotted-link.js_no-conv::text').extract()

        for x in range(len(shop_rating)):
            if shop_rating[x] == 'width: 100%;':
                shop_rating[x] = '5'
            else:
                shop_rating[x] = int(shop_rating[x][7:9]) / 20

        for x in range(len(number_of_reviews)):
            number_of_reviews[x] = number_of_reviews[x][:-7]

        for x in range(len(name_of_object)):
            items['name_of_object'] = name_of_object[x]
            items['price_one_product'] = price_one_product[x]
            items['website_link'] = website_link[x]
            items['shop_rating'] = shop_rating[x]
            items['number_of_reviews'] = int(number_of_reviews[x])
            yield items

