import sqlite3
import sys
import json
'''
def connect_old_database():
    conn = sqlite3.connect('products_from_search_page.db')
    curr = conn.cursor()
    curr.execute("""SELECT website_link FROM products order by price , number_of_shops DESC;""", (
    ))
    return curr.fetchone()[0]
'''
number_of_used_links = 0

def get_row():
    conn = sqlite3.connect('products_from_search_page.db')
    curr = conn.cursor()
    curr.execute("""SELECT count(*) FROM products order by number_of_shops DESC, price;""",())
    number_of_rows = curr.fetchone()
    curr.execute("""SELECT website_link FROM products order by number_of_shops DESC, price;""", (
    ))
    websites_links = curr.fetchmany(int(number_of_rows[0]))
    try:
        str = ''.join(websites_links[number_of_used_links])
    except IndexError:
        str = ''
    return str

def check():
    with open ('input_data.txt') as json_file:
        data = json.load(json_file)
        for info in data['input']:
            reputation = info['reputation']
            print(reputation)
    conn = sqlite3.connect('products_final.db')
    curr = conn.cursor()
    curr.execute("""SELECT count(*) FROM products where shop_rating > ? and shop_reviews_number > 20;""", (
        [reputation]
    ))
    result = int(curr.fetchone()[0])
    return result

def add_next_link():
    global number_of_used_links
    number_of_used_links = number_of_used_links + 1