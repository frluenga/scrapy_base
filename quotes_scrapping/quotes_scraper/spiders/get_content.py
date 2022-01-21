import scrapy

class GetContent(scrapy.Spider):
    name = 'content'
    start_urls = ['http://quotes.toscrape.com/page/1/']

    def parse(self,response):
        with open("../content.html", "w", encoding="utf-8") as f:
            f.write(response.text)
