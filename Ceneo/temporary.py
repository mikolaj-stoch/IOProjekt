import random
import json


def search():
    result = []
    sum_of_costs = 0
    output_data = {'products': [], 'costs': int}
    with open('input_data.txt') as json_file:
        input_data = json.load(json_file)

        for product in input_data['products']:
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
                output_data['products'].append({
                    'name': name,
                    'quantity': quantity,
                    'price': price,
                    'delivery': delivery_cost,
                    'link': link
                })
            output_data['costs'] = sum_of_costs
        with open('output_data.txt', 'w') as file:
            json.dump(output_data, file)
