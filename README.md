# Webcrawler-webspider
Web Spider or Web Crawler using Python and Scrapy

Web Spider for detecting if some site is using google analytics, and has enabled IP anonymization

### Technologies:
1. PyCharm
2. Python 3
3. Scrapy

### Crawler Implementation
Note: Implementation for crawler can be found in:
1. spiders/GASpider.py
2. items.py
3. plotting.py
I used Scrapy Framework for crawling in Python3. A project was created using command:
        scrapy startproject gadetector
After creating the project we need to generate a spider (named GASpider) using command:
        scrapy genspider GASpider
Results were generated in a file named garesults.csv. The
command used for running the spider and generating results is below:
        scrapy crawl -o garesults.csv GASpider
