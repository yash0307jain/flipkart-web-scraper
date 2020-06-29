import scrapy
from ..items import Laptop

class FlipkartScraper(scrapy.Spider):
  name = "flipkart_scraper"
  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.2840.71 Safari/539.36'}
  rating = []
  def start_requests(self):
    urls = [
      "https://www.flipkart.com/search?q=gaming+laptop&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_1_7_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_1_7_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=gaming+laptop&requestId=c1937f69-4b94-4090-952f-47478fe51af1&as-searchtext=gaming+&sort=price_asc"
    ]

    for url in urls:
      yield scrapy.Request(url = url, callback = self.parse, headers = self.headers)

  def parse(self, response):
    laptops = response.xpath("//a[@class='_31qSD5']").xpath("@href").getall()
    
    for laptop in laptops:
      laptopUrl = response.urljoin(laptop)
      yield scrapy.Request(url = laptopUrl, callback = self.parse_laptop, headers = self.headers)

  def parse_laptop(self, response):
    laptopName = response.xpath("//span[@class='_35KyD6']//text()").get()
    laptopPrice = response.xpath("//div[@class='_1vC4OE _3qQ9m1']//text()").get()
    laptopHighlights = response.xpath("//div[@class='g2dDAR']/div[@class='_3WHvuP']/ul/li[@class='_2-riNZ']//text()").getall()
    laptopSpec = response.xpath("//div[@class='MocXoX']/div/div[@class='_3Rrcbo V39ti-']/div[@class='_2RngUh']")
    
    laptopSpecifications = []

    for spec in laptopSpec:
      tempSpec = []

      specTitle = spec.xpath("div[@class='_2lzn0o']/text()").get()
      specItems = spec.xpath("table[@class='_3ENrHu']/tbody/tr[@class='_3_6Uyw row']")
      
      tempSpec.append(specTitle)

      detailSpec = []

      for item in specItems:
        tempDetailSpec = []

        specLabel = item.xpath("td[@class='_3-wDH3 col col-3-12']//text()").get()
        specValue = item.xpath("td[@class='_2k4JXJ col col-9-12']//text()").get()

        tempDetailSpec.append(specLabel)
        tempDetailSpec.append(specValue)

        detailSpec.append(tempDetailSpec)

      tempSpec.append(detailSpec)
      laptopSpecifications.append(tempSpec)
    
    laptopRating = response.xpath("//div[@class='col-12-12 _11EBw0']/div[@class='_1i0wk8']//text()").get()
    
    yield Laptop(name = laptopName, price = laptopPrice, highlight = laptopHighlights, specification = laptopSpecifications, rating = laptopRating)
    