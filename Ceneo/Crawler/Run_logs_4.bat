cd Crawler\search_page
scrapy crawl search_page_spider -a product_number=4 -s product_number=4
cd ..
cd list_of_products
scrapy crawl list_of_products_spider -a product_number=4 -s product_number=4
exit