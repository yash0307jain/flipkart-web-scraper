import scrapy
from ..items import Laptop

class FlipkartScraper(scrapy.Spider):
  name = "flipkart_scraper"
  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.2840.71 Safari/539.36'}
  no_of_pages = 4
  # page_no = 0

  def start_requests(self):
    urls = [
      "https://www.flipkart.com/search?q=gaming+laptop&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_1_7_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_1_7_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=gaming+laptop&requestId=c1937f69-4b94-4090-952f-47478fe51af1&as-searchtext=gaming+&sort=price_asc&page=1"
    ]

    for url in urls:
      yield scrapy.Request(url = url, callback = self.parse, headers = self.headers)

  def parse(self, response):
    self.no_of_pages -= 1
    # self.page_no += 1

    laptops = response.xpath("//div[@class='bhgxx2 col-12-12']/div[@class='_3O0U0u']/div/div[@class='_1UoZlX']/a[@class='_31qSD5']").xpath("@href").getall()
    
    for laptop in laptops:
      laptopUrl = response.urljoin(laptop)
      yield scrapy.Request(url = laptopUrl, callback = self.parse_laptop, headers = self.headers)

    if(self.no_of_pages > 0):
      next_page_all_href = response.xpath("//div[@class='_2zg3yZ']/nav[@class='_1ypTlJ']/a[@class='_3fVaIS']").xpath("@href").getall()
      next_page_href = next_page_all_href[len(next_page_all_href) - 1]
      next_page_url = response.urljoin(next_page_href)
      yield scrapy.Request(url = next_page_url, callback = self.parse, headers = self.headers)

  def parse_laptop(self, response):
    laptopUrl = response.request.url
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
    
    # laptopImageUrl = response.xpath("//div[@class='_3BTv9X _3iN4zu']/img/@src").get()
    
    yield Laptop(url = laptopUrl,name = laptopName, price = laptopPrice, highlight = laptopHighlights, specification = laptopSpecifications, rating = laptopRating)
    