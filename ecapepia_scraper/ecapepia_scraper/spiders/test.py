import scrapy

class ecapepiaSpider(scrapy.Spider):
    name = "PigDetail"
    def start_requests(self):
        urls = [
            "https://www.ekapepia.com/priceStat/period/pigPeriodDetailView.do?menuId=menu100017&boardInfoNo=" #산지경매가격 - 기간별 - 돼지도체 - 상세보기
        ]

        return [scrapy.Request(url=url, callback=self.parse) for url in urls]
        #혹은
        #for url in urls:
        #   yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        url = response.url
        rows = response.xpath('//*[@class="table-list"]/table/tbody/tr')
        print(f"URL is: {url}")
        for row in rows:
            print(f"{row}\n")
