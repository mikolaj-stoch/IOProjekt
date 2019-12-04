# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3
import json
import os

# Pipeline sluzy nam do przychwytywania w czasie crawlowania obiektow i zapisywania ich do baz dancyh
# Komendy z sq3lite, chyba raczej easy do zrozumienia
class ListOfProductsPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        path = '../../tmp'
        with open(os.path.join(path, "input_data.txt")) as json_file:
            data = json.load(json_file)
            for info in data['input']:
                name = info['name']
        name_database = name + ".db"
        path = r'..\..\tmp\\' + name_database;
        self.conn = sqlite3.connect(path)
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""drop table if exists products""")
        self.curr.execute("""create table products(
                             object_name text,
                             price float,
                             delivery_info text,
                             website_link text,
                             shop_name text,
                             shop_rating int,
                             shop_reviews_number int
                             )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self,item):
        self.curr.execute(""" insert into products values (?,?,?,?,?,?,?)""",(
            item['name_of_object'],
            item['price_one_product'],
            item['delivery_info'],
            item['website_link'],
            item['shop_name'],
            item['shop_rating'],
            item['number_of_reviews']
        ))
        self.conn.commit()
