import os

def products_maker(number):
    search_command = "search_page_spider.py " + str(number)
    list_of_products_command = "list_of_products_spider.py " + str(number)
    os.chdir('./search_page_SCRIPT/search_page/spiders')
    os.system(search_command)
    os.chdir('../../../list_of_products_SCRIPT/list_of_products/spiders')
    os.system(list_of_products_command)
    os.chdir('../../..')


if __name__ == "__main__":
    products_maker(0)
    products_maker(1)
    products_maker(2)
    products_maker(3)
    products_maker(4)
