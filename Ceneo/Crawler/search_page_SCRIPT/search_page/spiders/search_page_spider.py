# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess
from Ceneo.Crawler.search_page_SCRIPT.search_page.items import SearchPageItem
import json
import os
from scrapy.utils.project import get_project_settings
import sys

class SearchPageSpiderSpider(scrapy.Spider):
    name = 'search_page_spider'

    def __init__(self, product_number='', **kwargs):
        super().__init__(**kwargs)
        self.product_number = int(product_number)
        path = '../../../../tmp'
        with open(os.path.join(path, "input_data.txt")) as json_file:
            data = json.load(json_file)
            info = data['products'][self.product_number]
            name_of_product = info['name']
            min_price = info['minimum_price']
            max_price = info['maximum_price']

        name_of_product = name_of_product.replace(" ", "+")
        if min_price == '':
            min_price = 0
        if max_price == '':
            price_range = ";m" + str(min_price) + ";n"
        else:
            price_range = ";m" + str(min_price) + ";n" + str(max_price)

        url = 'https://www.ceneo.pl/;szukaj-' + name_of_product + price_range + ';0112-0.htm'
        self.start_urls = [url]

    def parse(self, response):
        items = SearchPageItem()
        counter_button = 0
        all_products = response.css('.cat-prod-row-content')

        for product in all_products:
            # CSS - wylapywanie znacznikow itp.
            object_name = product.css('.js_conv::text').extract()
            price = product.css('.value::text').extract()
            button_name = product.css('.js_force-conv::text').extract()
            website_link = product.css('.js_force-conv::attr(href)').get()
            number_of_shops = product.css('.shop-numb::text').extract()
            penny = product.css('.penny::text').extract()
            if button_name == ['Porównaj ceny']:
                counter_button = counter_button + 1
                if website_link[-9:] != 'promotion':
                    items['object_name'] = object_name
                    # print(penny[1:])
                    items['price'] = float(price[0]) + float(penny[0][1:]) * 0.01
                    items['website_link'] = website_link
                    items['number_of_shops'] = number_of_shops[0][2:4]
                    yield items
        if counter_button == 0:
            print("Na stronie znajduja sie same oferty z przysciskiem 'Kup teraz'.")

        if all_products == []:
            all_products_first_search_forced_list_view = response.url + ";0191"
            yield response.follow(all_products_first_search_forced_list_view, callback=self.parse)


def run_search_page_spider(product_number):
    s = get_project_settings()
    s['product_number'] = product_number
    process = CrawlerProcess(s)
    process.crawl(SearchPageSpiderSpider, product_number=str(product_number))
    process.start()


if __name__ == "__main__":
    run_search_page_spider(int(sys.argv[1]))




