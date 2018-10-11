import scrapy


class baiduBaikeSpider(scrapy.Spider):
    name = "baidu_baike"

    start_urls = [
        'https://baike.baidu.com/item/%E9%AB%98%E5%9C%86%E5%9C%86',
    ]

    # headers = {
    #   //////  'host': 'image.baidu.com',
    #     'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0'
    #
    # }

    # def start_requests(self):
    #     yield scrapy.Request(url, headers=self.headers)

    def parse(self, response):
        title = response.css('title::text').extract_first()
        title = title.split('_')[0]
        person_info = response.css('.lemmaWgt-lemmaSummary::text').extract()
        base_info = response.css('.basic-info .basicInfo-block dd::text').extract()


        print(title)
        print(person_info)
        print(base_info)