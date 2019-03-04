import scrapy
from learning.items import LearningItem


class Douban(scrapy.Spider):
    name = 'douban_top250'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        url = 'https://movie.douban.com/top250'
        yield scrapy.Request(url, headers=self.headers)

    def parse(self, response):
        item = LearningItem()
        data = response.css('.item')
        for i in data:
            item['name'] = i.css('.title::text').extract_first()
            item['scores'] = i.css('.rating_num::text').extract_first()
            item['comment'] = i.css('.inq::text').extract_first()
            item['cover_img'] = i.css('img::attr(src)').extract_first()
            yield item
        next_url = response.css('.next a::attr(href)').extract_first()
        if next_url is not None:
            yield scrapy.Request(response.urljoin(next_url), self.parse, headers=self.headers)
