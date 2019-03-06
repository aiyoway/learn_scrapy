import scrapy
import re

from learning.items import QiushiItem


class Qiushi(scrapy.Spider):
    name = 'qiushi'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        url = 'http://www.qiushibaike.com/history/'
        yield scrapy.Request(url, headers=self.headers)

    def parse(self, response):
        item = QiushiItem()
        data = response.css('.article')
        for i in data:
            thumb = i.css('.thumb').extract_first()
            if thumb:
                continue
            item['unique'] = re.sub(r'[^\d]', '', i.css('.article::attr(id)').extract_first())
            item['author'] = i.css('.author h2::text').extract_first()
            item['sex'] = re.findall(r'man|women', i.css('.articleGender::attr(class)').extract_first())[0] if i.css(
                '.articleGender::attr(class)').extract_first() else ''
            item['content'] = re.sub(r'</?span>|<br>', '', i.css('.content span').extract_first())
            item['starts'] = i.css('.stats-vote .number::text').extract_first()
            item['comments_num'] = i.css('.stats-comments .number::text').extract_first()
            yield item
        next_url = response.css('.pagination .next').extract_first()
        if next_url is not None:
            url = response.urljoin(response.css('.pagination a::attr(href)').extract()[:1][0])
            print(url)
            yield scrapy.Request(url, self.parse, headers=self.headers)
