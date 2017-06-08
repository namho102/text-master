import scrapy
import time

# urls = ['http://www.worldfootball.net/schedule/eng-premier-league-2016-2017-spieltag/' + str(x + 1) for x in range(20)]# print(urls)

URL = "https://techcrunch.com/page/%d"

class NewsSpider(scrapy.Spider):
    name = 'tablespider'
    start_urls = [URL % 1]
    page_number = 1


    def parse(self, response):

        text = ''
        for row in response.css('div.article-entry.text'):
            text += row.css('p').extract_first() + ''

        yield {
            'text': text
        }

        for row in response.css('.post-title'):
            next_page = response.css('a ::attr(href)').extract_first()
            yield scrapy.Request(next_page, callback = self.parse)


        self.page_number += 1
        if self.page_number <= 2:
            yield scrapy.Request(URL % self.page_number, callback = self.parse)