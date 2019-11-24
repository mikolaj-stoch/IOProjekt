import sqlite3


def connect_old_database(price_min, price_maks):
    conn = sqlite3.connect('products_from_search_page.db')
    curr = conn.cursor()
    curr.execute("""SELECT website_link FROM products WHERE price > ? and price  < ? ORDER by price""", (
        price_min,
        price_maks
    ))
    return curr.fetchone()[0]