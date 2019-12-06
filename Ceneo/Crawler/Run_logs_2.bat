color 02
cd Crawler\search_page
scrapy crawl search_page_spider -a product_number=2 -s product_number=2
cd ..
cd list_of_products
scrapy crawl list_of_products_spider -a product_number=2 -s product_number=2
exit