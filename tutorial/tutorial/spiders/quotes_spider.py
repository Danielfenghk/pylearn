# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = [
            'http://www.talapparel.com/',
          ]
      

    def parse(self, response):
        for quote in response.css('div.desktop-lang'):
            yield {
				'eng':quote.css("ul li:nth-child(1) a::text").extract_first(),
				'simplec':quote.css(" ul li:nth-child(2) a::text").extract_first(),
              }
              
        #next_page =response.css("#iso-wrap  div:nth-child(1)  div:nth-child(3) a::attr(href)").extract_first()
        #if next_page is not None:
        #    next_page = response.urljoin(next_page)
        #    yield scrapy.Request(next_page, callback=self.parse)
        yield response.follow(response.css("#iso-wrap  div:nth-child(1)  div:nth-child(3) a")[0])