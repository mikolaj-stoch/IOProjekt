# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

# Pipeline sluzy nam do przychwytywania w czasie crawlowania obiektow i zapisywania ich do baz dancyh
# Komendy z sq3lite, chyba raczej easy do zrozumienia
class ListOfProductsPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("products_final.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""drop table if exists products""")
        self.curr.execute("""create table products(
                             object_name text,
                             price int,
                             website_link text,
                             shop_rating int,
                             shop_reviews_number int
                             )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self,item):
        self.curr.execute(""" insert into products values (?,?,?,?,?)""",(
            item['name_of_object'],
            item['price_one_product'],
            item['website_link'],
            item['shop_rating'],
            item['number_of_reviews']
        ))
        self.conn.commit()
