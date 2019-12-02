import sqlite3
import itertools


class Product:
    delivery_price = float('NaN')

    def __init__(self, row):
        self.object_name = row[0]
        self.price = row[1]
        self.delivery_info = row[2]
        self.website_link = row[3]
        self.shop_name = row[4]
        self.shop_rating = row[5]
        self.shop_reviews_number = row[6]
        self.calculate_delivery_price()
        #self.total_price = round(self.price + self.delivery_price, 2)

    def calculate_delivery_price(self):
        if "Darmowa" in self.delivery_info:
            self.delivery_price = 0
        elif "szczegóły" not in self.delivery_info:
            tmp = ""
            for i in range(len("Z wysyłką od\r\n"),
                           len(self.delivery_info)):  # in str(list(range(10))).strip('[]').replace(' ', ''):
                if self.delivery_info[i] in "0123456789,":
                    tmp += self.delivery_info[i]
            tmp = float(tmp.replace(",", "."))
            self.delivery_price = round(tmp - self.price, 2)


def database_to_object(path):
    con = sqlite3.connect(path)
    obj_list = []
    sql_request = """   SELECT * FROM products 
                            WHERE shop_rating >= 4 
                                AND shop_reviews_number > 20 
                                AND delivery_info NOT LIKE 'szczegóły dostawy' 
                            ORDER BY price;     """
    for row in con.execute(sql_request):
        obj_list.append(Product(row))

    # Sort list by total price (product + delivery)
    #obj_list = sorted(obj_list, key=lambda obj: obj.total_price)
    return obj_list


def list_of_products(database_name):
    product_list = []
    for i in range(len(database_name)):
        product_list.append(database_to_object(database_name[i]))

    # TO DELETE:
    # for product in product_list:
    #     print(database_name)
    #     for i in range(len(product)):
    #         print(product[i].price, product[i].delivery_price, product[i].total_price)
    #     print('\n\n')
    return product_list


def find_optimal(product_list):
    possibility = []
    for sequence in itertools.product(*product_list):
        possibility.append(sequence)

    final_list = []
    for product in possibility:
        del_pri = {}
        final_price = 0
        for i in range(len(product)):
            if product[i].shop_name not in del_pri:
                del_pri[product[i].shop_name] = product[i].delivery_price
            elif del_pri[product[i].shop_name] < product[i].delivery_price:
                del_pri[product[i].shop_name] = product[i].delivery_price
            final_price += product[i].price
        final_price += sum(del_pri.values())
        final_list.append([product, round(final_price, 2)])

    final_list = sorted(final_list, key=lambda row: row[1])
    return final_list


def main():
    input_db = ['chleb.db', 'Huawei P30.db', 'DLUGOPIS.db', 'Nokia telefon.db', 'xiaomi redmi note.db']
    product_list = list_of_products(input_db)
    final_list = find_optimal(product_list)

    # for i in final_list:
    #     print(i)
    print(final_list[0][1], end='\n\n')
    for o in final_list[0][0]:
        print(o.shop_name, o.delivery_price, o.object_name)


if __name__ == '__main__':
    main()
