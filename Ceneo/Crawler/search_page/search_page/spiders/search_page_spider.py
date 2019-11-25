# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess
from search_page.items import SearchPageItem
import sqlite3


class SearchPageSpiderSpider(scrapy.Spider):
    name = 'search_page_spider'
    # Nazwa crawlea - sluzy do uruchamiania
    print("Podaj nazwe produktu")
    name_of_product = input()
    name_of_product = name_of_product.replace(" ", "+") # Skladnia ceneo - nie ma spacji w adresie, tylko plusy

    url = 'https://www.ceneo.pl/;szukaj-' + name_of_product
    start_urls = [url]

    def parse(self, response):
        items = SearchPageItem() # Items - w tej klasie wpisujemy jakie chcemy pola crawlowac ( de facto ustalamy tylko ich nazwy )

        all_products_first_search_forced_list_view = response.url + ";0191"  # Force list view. 0191 - zwraca strone w postaci listy !!
        # bo ceneo ma dwa sposoby wyswietlania: box i lista (raz uzywa tego a raz tego )- ten crawler jest zrobiony pod liste !!
        # yield to taki return - wywolujemy funkcje jeszcze raz, ale z linkiem pod liste -- jezeli defaultowo byla lista
        # jezeli defaultowo lista ( np. przy teleonach - zAWsze zwraca liste ) to scrapy wykryje ze to ten sam link i nie wywola jeszcze
        # raz tej funkcji
        yield response.follow(all_products_first_search_forced_list_view, callback=self.parse)

        all_products = response.css('.cat-prod-row-content') # Tutaj odczytujemy kawalek strony zawierajacy interesujace nas dane!!

        # ten for - bierze nasza juz wyciety kawalek strony i jedzie po kolei odyczytujac kazdy parametr i zapisujac do zmiennych
        for product in all_products:
            # CSS - wylapywanie znacznikow itp.
            object_name = product.css('.js_conv::text').extract()
            price = product.css('.value::text').extract()
            button_name = product.css('.js_force-conv::text').extract()
            website_link = product.css('.js_force-conv::attr(href)').get()
            if button_name == ['Porównaj ceny']: # Interesuje nas tylko ten przycisk, a nie kup teraz !
                items['object_name'] = object_name
                items['price'] = price
                items['website_link'] = website_link
                yield items




