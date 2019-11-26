import random
import json


def search():
    result = []
    sum_of_costs = 0
    with open('input_data.txt') as json_file:
        data = json.load(json_file)

        for product in data['input']:
            tmp = []
            name = None
            name = product['name']
            quantity = None
            min_price = None
            max_price = None
            if name:
                try:
                    quantity = int(float(product['quantity']))
                    min_price = int(float(product['minimum_price']))
                    max_price = int(float(product['maximum_price']))
                except ValueError:
                    print("error")
                if min_price and max_price:
                    price = random.randint(min_price, max_price)
                else:
                    price = random.randint(10, 200)
                link = random.choice(["www.google.com", "www.onet.pl", "www.facebook.com", "www.wp.pl"])
                delivery_cost = random.randint(10, 20)
                sum_of_costs = sum_of_costs + price*quantity + delivery_cost
                tmp.append(name)
                tmp.append(quantity)
                tmp.append(price)
                tmp.append(delivery_cost)
                tmp.append(link)
                result.append(tmp)
            result.append(sum_of_costs)
        return result
