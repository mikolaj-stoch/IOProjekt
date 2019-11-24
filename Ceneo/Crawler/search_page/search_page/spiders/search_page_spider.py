# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess
from search_page.search_page.items import SearchPageItem


class SearchPageSpiderSpider(scrapy.Spider):
    name = 'search_page_spider'

    print("Podaj nazwe produktu")
    name_of_product = input()
    name_of_product = name_of_product.replace(" ", "+")

    url = 'https://www.ceneo.pl/;szukaj-' + name_of_product
    start_urls = [url]

    def parse(self, response):
        items = SearchPageItem()

        all_products_first_search_forced_list_view = response.url + ";0191"  # Force list view.
        yield response.follow(all_products_first_search_forced_list_view, callback=self.parse)

        all_products = response.css('.cat-prod-row-content')
        for product in all_products:
            object_name = product.css('.js_conv::text').extract()
            price = product.css('.value::text').extract()
            button_name = product.css('.js_force-conv::text').extract()
            website_link = product.css('.js_force-conv::attr(href)').get()
            if button_name == ['Porównaj ceny']:
                items['object_name'] = object_name
                items['price'] = price
                items['website_link'] = website_link
                yield items


def run_search_page_spider():
    process = CrawlerProcess(settings={
        'FEED_FORMAT': 'json',
        'FEED_URI': 'items.json'
    })
    process.crawl(SearchPageSpiderSpider)
    # process.start()
