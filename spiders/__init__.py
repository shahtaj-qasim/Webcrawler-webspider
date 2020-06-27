# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

# Crawler Implementation
Note: Implementation for crawler can be found in:
1. gadetector/gadetector/spiders/GASpider.py
2. gadetector/gadetector/items.py
3. gadetector/gadetector/plotting.py
I used Scrapy Framework for crawling in Python3. A project was created using command:
        scrapy startproject gadetector
After creating the project we need to generate a spider (named GASpider) using command:
        scrapy genspider GASpider
Results were generated in a file named garesults.csv. The
command used for running the spider and generating results is below:
        scrapy crawl -o garesults.csv GASpider
