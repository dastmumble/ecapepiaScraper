import scrapy

from ecapepia_scraper.items import EcapepiaScraperItem

class ecapepiaSpider(scrapy.Spider):
    name = "PigDetail"
    allowed_domains = ["https://www.ekapepia.com/"] #축산유통정보
    start_urls = [
        "https://www.ekapepia.com/priceStat/period/pigPeriodDetailView.do?menuId=menu100017&boardInfoNo=" #산지경매가격 - 기간별 - 돼지도체 - 상세보기
        ]
    
    def parse(self, response):
        self.browser.get(response.url)
        html = self.browser.find_element_by_xpath('//*').get_attribute('outerHTML')
        selector = Selector(text=html)
        url = response.url
        title = response.css('h1::text').get()
        print(f"URL is: {url}")
        print(f"Title is: {title}")

ecapepiaSpider.start_urls