color 04
cd Crawler\search_page
scrapy crawl search_page_spider -a product_number=1 -s product_number=1
cd ..
cd list_of_products
scrapy crawl list_of_products_spider -a product_number=1 -s product_number=1
exit