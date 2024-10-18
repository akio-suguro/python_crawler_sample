import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from scraper.items import ScrapedDataItem

class ExampleSpider(scrapy.Spider):
    name = 'example'
    start_urls = ['https://example.com']

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)

    def parse(self, response):
        self.driver.get(response.url)
        title = self.driver.title
        url = response.url
        content = self.driver.page_source

        item = ScrapedDataItem()
        item['title'] = title
        item['url'] = url
        item['content'] = content
        yield item

    def close(self, reason):
        self.driver.quit()
