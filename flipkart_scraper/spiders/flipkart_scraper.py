import scrapy

class FlipkartScraper(scrapy.Spider):
  name = "flipkart_scraper"
  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.2840.71 Safari/539.36'}
  count = 0

  def start_requests(self):
    urls = [
      "https://www.amazon.in/s?k=gaming+laptops&ref=nb_sb_noss_2",
      "https://www.flipkart.com/search?q=gaming+laptop&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_1_7_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_1_7_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=gaming+laptop&requestId=c1937f69-4b94-4090-952f-47478fe51af1&as-searchtext=gaming+&sort=price_asc"
    ]

    for url in urls:
      yield scrapy.Request(url = url, callback = self.parse, headers = self.headers)

  def parse(self, response):
    self.count = self.count + 1
    filename = 'flipkart_scraper/data/data-%d.html' % self.count
    with open(filename, 'wb') as f:
      f.write(response.body)