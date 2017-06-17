import scrapy
import time

# urls = ['http://www.worldfootball.net/schedule/eng-premier-league-2016-2017-spieltag/' + str(x + 1) for x in range(20)]# print(urls)

URL = "https://techcrunch.com"

class NewsSpider(scrapy.Spider):
    name = 'tablespider'
    start_urls = ["https://techcrunch.com/2017/06/08/confirmed-verizon-will-cut-15-of-aol-yahoo-staff-after-merger-closes/", "https://techcrunch.com/2017/06/07/uber-exec-is-out-after-violating-riders-privacy/"]


    def parse(self, response):
        for row in response.css('.l-main'):
            yield {
                'title': response.css('header > h1').extract_first(),
                'text': response.css('div.article-entry.text').extract_first()
            }