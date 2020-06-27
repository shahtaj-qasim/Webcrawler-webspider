# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from gadetector.items import GadetectorItem


class GaspiderSpider(scrapy.Spider):
    name = 'GASpider'
    allowed_domains = [
        'https://www.businessinsider.de/',
        'https://de.wikipedia.org/',
        'https://edition.cnn.com/',
        'https://www.reddit.com/'
    ]
    start_urls = [
        'https://www.businessinsider.de/?r=US&IR=T',
        'https://de.wikipedia.org/wiki/Deutschland',
        'https://edition.cnn.com/',
        'https://www.reddit.com/'
    ]

    def parse(self, response):
        i = GadetectorItem()
        i['url'] = response.url
        i['hasGA'] = 'FALSE'
        i['hasIPAnon'] = 'FALSE'
        sel = Selector(response)

        ga = sel.xpath('//script[contains(text(), "google-analytics.com/analytics.js")]').getall()
        if ga is not None:
            stringga = str(ga)
            # checking if there is google analytics being used
            if '//www.google-analytics.com/analytics.js' in stringga:
                i['hasGA'] = 'TRUE'
            # checking if IP anonymization is enabled
            if stringga.find("gaTracker('set', 'anonymizeIp', true)"):
                i['hasIPAnon'] = 'TRUE'
            else:
                i['hasIPAnon'] = 'FALSE'
        return i
