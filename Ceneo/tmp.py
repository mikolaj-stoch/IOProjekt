import json


def search():
    # example output file
    data = {"sets": [{"products": [{"name": "produkt 1", "quantity": 1, "price": 11, "delivery": 17, "link": "www.wp.pl"}, {"name": "produkt 2", "quantity": 2, "price": 16, "delivery": 13, "link": "www.wp.pl"}, {"name": "produkt 3", "quantity": 3, "price": 17, "delivery": 13, "link": "www.onet.pl"}, {"name": "produkt 4", "quantity": 4, "price": 10, "delivery": 10, "link": "www.onet.pl"}, {"name": "produkt 5", "quantity": 5, "price": 2, "delivery": 17, "link": "www.google.com"}], "costs": 214}, {"products": [{"name": "produkt 1", "quantity": 1, "price": 11, "delivery": 17, "link": "www.wp.pl"}, {"name": "produkt 2", "quantity": 2, "price": 16, "delivery": 13, "link": "www.wp.pl"}, {"name": "produkt 3", "quantity": 3, "price": 17, "delivery": 13, "link": "www.onet.pl"}, {"name": "produkt 4", "quantity": 4, "price": 10, "delivery": 10, "link": "www.onet.pl"}, {"name": "produkt 5", "quantity": 5, "price": 2, "delivery": 17, "link": "www.google.com"}], "costs": 214}, {"products": [{"name": "produkt 1", "quantity": 1, "price": 11, "delivery": 17, "link": "www.wp.pl"}, {"name": "produkt 2", "quantity": 2, "price": 16, "delivery": 13, "link": "www.wp.pl"}, {"name": "produkt 3", "quantity": 3, "price": 17, "delivery": 13, "link": "www.onet.pl"}, {"name": "produkt 4", "quantity": 4, "price": 10, "delivery": 10, "link": "www.onet.pl"}, {"name": "produkt 5", "quantity": 5, "price": 2, "delivery": 17, "link": "www.google.com"}], "costs": 214}]}
    with open('./tmp/output_data.txt', 'w') as file:
        json.dump(data, file)
