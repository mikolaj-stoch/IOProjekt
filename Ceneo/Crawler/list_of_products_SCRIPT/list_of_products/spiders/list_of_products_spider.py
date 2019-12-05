# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess
from list_of_products.items import ListOfProductsItem
from list_of_products.database_connector import get_row
from list_of_products.database_connector import check
from list_of_products.database_connector import add_next_link


class ListOfProductsSpiderSpider(scrapy.Spider):

    name = 'list_of_products_spider'

    def __init__(self, product_number='', **kwargs):
        super().__init__(**kwargs)
        self.product_number = int(product_number)
        self.product_id = get_row(str(self.product_number))
        url = 'http://ceneo.pl' + self.product_id # Link
        self.start_urls = [url] # Link

    def parse(self, response):
        if self.product_id != '':
            items = ListOfProductsItem()

            backup_name = response.css('.default-cursor::text').extract()
            name_of_object = response.css('.short-name__txt::text').extract()
            price_one_product = response.css('.product-price.go-to-shop .value::text').extract()
            penny = response.css('.penny::text').extract()
            # website_link = response.css('.cell-actions .btn-cta::attr(href)').extract()
            website_link = response.css('.btn-cta.go-to-shop::attr(href)').extract()
            shop_name = response.css('.js_product-offer-link::text').extract()
            shop_rating = response.css('.js_no-conv .score-marker--s::attr(style)').extract()
            delivery_information = response.css('.js_deliveryInfo::text').extract()
            number_of_reviews = response.css('.dotted-link.js_no-conv::text').extract()

            final_delivery_information = []

            for x in range(len(delivery_information) - 1):
                if delivery_information[x] == '\r\n' and delivery_information[x+1] == '                ':
                    final_delivery_information.append("Darmowa wysylka")
                if delivery_information[x] != '\r\n' and delivery_information[x] != '                ':
                    final_delivery_information.append(delivery_information[x].strip())

            if len(final_delivery_information) != len(name_of_object):
                final_delivery_information.append(delivery_information[len(delivery_information) - 1])

            for x in range(len(shop_name)):
                shop_name[x] = shop_name[x][9:]

            for x in range(len(shop_rating)):
                if shop_rating[x] == 'width: 100%;':
                    shop_rating[x] = '5'
                if shop_rating[x] == 'width: 0%;':
                    shop_rating[x] = '0'
                if shop_rating[x] != 'width: 100%;' and shop_rating[x] != 'width: 0%;' and shop_rating[x] != '5' and shop_rating[x] != '0':
                    shop_rating[x] = float(shop_rating[x][7:9])/20

            for x in range(len(number_of_reviews)):
                number_of_reviews[x] = number_of_reviews[x][:-7]

            for x in range (len(name_of_object)):
                if name_of_object[x] == 'Odpowiedź jest pomocna?':
                    name_of_object[x] = backup_name[0]

            for x in range(len(price_one_product)):
                items['name_of_object'] = name_of_object[x]
                items['price_one_product'] = float(price_one_product[x]) + float(penny[x][1:]) * 0.01
                items['website_link'] = website_link[x]
                items['shop_name'] = shop_name[x]
                items['delivery_info'] = final_delivery_information[x]
                items['shop_rating'] = shop_rating[x]
                items['number_of_reviews'] = int(number_of_reviews[x])
                yield items # Yield do takie return

            if check(self.product_number) < 5:
                add_next_link()
                url_new = 'http://ceneo.pl' + get_row(str(self.product_number))
                yield response.follow(url_new, callback=self.parse)

        else:
            print("Na stronie nie ma wystaczajacej liczby informacji.")