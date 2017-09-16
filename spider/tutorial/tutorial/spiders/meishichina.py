# -*- coding: utf-8 -*-

import scrapy

class MeishiSpider(scrapy.Spider):
    name = "meishi"
    allowed_domains = ["www.meishij.net"]
    start_urls = [
        "http://www.meishij.net/chufang/diy/?&page=1"
    ]

    def parse(self, response):
        try:
            #Response = response.xpath('//div[@class="wrap"]//div[@class="space_left"]//ul/li')
            Response = response.xpath('//div[@class="listtyle1"]')
            for sel in Response:
                yield {
                    'title' : sel.xpath('a/@title').extract(),
                    'link' : sel.xpath('a/@href').extract(),
                    'desc' : sel.xpath('a/strong/span/text()').extract()
                    #print (title,link,desc)
                }

            #next page
            next_page_url = response.xpath('//div[@class="listtyle1_page_w"]//a//@href').extract()[-1]
            #print(next_page_url)
            if next_page_url is not None:
                yield scrapy.Request(response.urljoin(next_page_url))
        except Exception as e:
            print(e)

