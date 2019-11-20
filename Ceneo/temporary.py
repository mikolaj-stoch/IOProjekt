import random


def search(input_data):
    result = []
    sum_of_costs = 0
    for row in input_data:
        tmp = []
        name = None
        name = row[0]
        quantity = None
        min_price = None
        max_price = None
        if name:
            try:
                quantity = int(float(row[1]))
                min_price = int(float(row[2]))
                max_price = int(float(row[3]))
            except ValueError:
                print("error")
            if min_price and max_price:
                price = random.randint(min_price, max_price)
            else:
                price = random.randint(10, 200)
            link = random.choice(["www.google.com", "www.onet.pl", "www.facebook.com", "www.wp.pl"])
            sum_of_costs = sum_of_costs + price*quantity + random.randint(10, 20)
            tmp.append(name)
            tmp.append(price)
            tmp.append(link)
            result.append(tmp)
        result.append(sum_of_costs)
    return result
