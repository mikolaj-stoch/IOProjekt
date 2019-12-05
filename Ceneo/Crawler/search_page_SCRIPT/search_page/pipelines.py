# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3
# Przechwytujemy dane ze strumienia i zapisujemy do bazy danych. Komendy z sq3lite.

class SearchPagePipeline(object):
    def __init__(self,product_number):
        self.product_number = str(product_number)
        self.create_connection()
        self.create_table()


    def create_connection(self):
        path = r'..\..\..\..\tmp\products_from_search_page_' + self.product_number + '.db'
        self.conn = sqlite3.connect(path)
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""drop table if exists products""")
        self.curr.execute("""create table products(
                             object_name text,
                             price float,
                             website_link text,
                             number_of_shops int
                             )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self,item):
        self.curr.execute(""" insert into products values (?,?,?,?)""",(
            item['object_name'][0],
            item['price'],
            item['website_link'],
            item['number_of_shops'][0]
        ))
        self.conn.commit()

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        product_number = settings.get('product_number')
        print(product_number)
        return cls(product_number)