# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess
from list_of_products.items import ListOfProductsItem # Importujemy liste wartosci z items - tak jak w search_page
from list_of_products.database_connector import connect_old_database # Moja klasa sluzaca do odycztu z bazy danych
from selenium import webdriver # To w fazie beta - ma pozwolic w JavaScripcie do "klikniecia" danego przycisku i wydobycia z niego informacji
# Uzycie do zdobycia informaacji o dostawie - to co pislaem w poscie.

class ListOfProductsSpiderSpider(scrapy.Spider):
    # Drugi Crawler który skrapuje produkt z bazy danych otrzymanej od search page - z listy wyszukiwan.
    # Dziala ciut inaczej niz tamtem - w funkcji parse.
    print("Podaj widelki")
    price_min = input()
    price_max = input()
    product_id = connect_old_database(price_min,price_max) # Odczytujemy najtanszy ( znajdujacy sie w widelkach ! ) produkt - bierzemy jego storne.
    # Tak bylo w zalozeniach w poscie na grupie
    url = 'http://ceneo.pl' + product_id # Link
    start_urls = [url] # Link

    def __init__(self):
        self.driver = webdriver.Chrome()

    def parse(self, response):
        items = ListOfProductsItem()
        # Kombinowanie z css aby odczytac wartosci - dziala
        name_of_object = response.css('.short-name__txt::text').extract()
        price_one_product = response.css('.product-price.go-to-shop .value::text').extract()
        website_link = response.css('.cell-actions .btn-cta::attr(href)').extract()
        shop_rating = response.css('.js_no-conv .score-marker--s::attr(style)').extract()
        # delivery_information = response.css('.js_deliveryInfo::text').extract()
        number_of_reviews = response.css('.dotted-link.js_no-conv::text').extract()

        # Ten for jest po to aby odczytac ocene sklepu - jest ona zapisywana w postaci tekstu np: width: 100% gdzie 100 % sprawia ze wyswietla sie 5 gwiazdek
        # 90 % width - 4.5 80 % - 4.0 itp. Ocena sklepu jest z dokladnoscia do 0.5. Tak jest na calym ceneo.
        for x in range(len(shop_rating)):
            if shop_rating[x] == 'width: 100%;':
                shop_rating[x] = '5'
            else:
                shop_rating[x] = int(shop_rating[x][7:9]) / 20
        # number of reviews - dostajemy w postaci np. 2137 opinii - ten for ucina napis "opinii" badz "opinie"
        for x in range(len(number_of_reviews)):
            number_of_reviews[x] = number_of_reviews[x][:-7]

        # Trying selenium - ma to sluzyc do delivery_information - w fazie beta
        '''
        self.driver.get(response.url)
        while True:
            next = self.driver.find_element_by_css_selector('.view-offer-details')
            print('walach_TV')
            print(next)
            try:
                next.click()
                print("WALACH_TV")
                print(next)
            except:
                break

        self.driver.close()
        '''
        # -> kazdy response.css zwraca liste np. 15 obiektow. Jedziemy kazdego po kolei i zwracamy do items
        for x in range(len(name_of_object)):
            items['name_of_object'] = name_of_object[x]
            items['price_one_product'] = price_one_product[x]
            items['website_link'] = website_link[x]
            items['shop_rating'] = shop_rating[x]
            items['number_of_reviews'] = int(number_of_reviews[x])
            yield items # Yield do takie return

