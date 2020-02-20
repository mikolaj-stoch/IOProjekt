# IO Projekt - Ceneo Shopping Optimizer

Ceneo Shoppping Optimizer written in Python 3.8 made for Inzyniera Oprogramowania subject.

## Technologies

* Flask - for frontend and backend integration.
* Scrapy - for Web Crawler.

## Setup

* Install Flask module and Scrapy using pip3.
* Run app.py from Ceneo folder.
* Connect to http://127.0.0.1:5000/ using any web browser.

## Features

* Search up to five products from Ceneo website based on input data given by user - name of the item, price range, quantity and seller reputation.
* In about 10 seconds we will find best options and try to put them together so that they were from one seller (if possible).
* Mechanism of collecting logs.

## How it works

* Input data given in front-end is proceed to Web-Crawler scrapy by JSON components.
* Scrapy reads JSON and start searching on Ceneo website. Then, it returns results in databses files .db.
* Optimalizer reads databases and calculates best sets.

## Screenshots

### Main Page

![Main page](https://github.com/miko083/IOProjekt/blob/master/images/main_page.png)

### Search Page

![Search page](https://github.com/miko083/IOProjekt/blob/master/images/search_page.png)

### Results - Option 1

![Results Option 1](https://github.com/miko083/IOProjekt/blob/master/images/results_1.png)

### Results - Option 2

![Results Option 2](https://github.com/miko083/IOProjekt/blob/master/images/results_2.png)

## Authors

* [Paweł Czaja](https://github.com/GitHub-Pawel) - process of optimization and return of final options.
* [Mateusz Morawiec](https://github.com/mmorawiec03) - website design and flask integration.
* [Mikołaj Stoch](https://github.com/miko083) - web-crawler and logs mechanism.
