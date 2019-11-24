# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

class SearchPagePipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("products_from_search_page.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""drop table if exists products""")
        self.curr.execute("""create table products(
                             object_name text,
                             price int,
                             website_link text
                             )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self,item):
        self.curr.execute(""" insert into products values (?,?,?)""",(
            item['object_name'][0],
            item['price'][0],
            item['website_link']
        ))
        self.conn.commit()