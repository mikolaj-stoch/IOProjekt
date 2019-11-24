cd search_page
scrapy crawl search_page_spider
copy .\products_from_search_page.db ..\list_of_products\
cd ..
cd list_of_products
scrapy crawl list_of_products_spider
Pause