from bs4 import BeautifulSoup
import requests as req
import csv

url = 'https://www.flipkart.com/search?q=gaming+laptop&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_1_7_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_1_7_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=gaming+laptop&requestId=c1937f69-4b94-4090-952f-47478fe51af1&as-searchtext=gaming+&sort=price_asc'
res = req.get(url)

html = res.content
soup = BeautifulSoup(html, features='lxml')

items = soup.findAll('div', attrs={ 'class': '_3O0U0u'})

list_of_rows = []
for item in items:
  cell = []

  # title of product
  title = item.find('div', attrs={ 'class': '_3wU53n'})
  cell.append(title.text)

  # price of product
  price = item.find('div', attrs={ 'class': '_1vC4OE _2rQ-NK'})
  cell.append("Rs. " + price.text[1:])

  # specs of product
  specs = item.findAll('li', attrs={ 'class': 'tVe95H'})
  firstFlag = False
  for spec in specs:
    if firstFlag:
      cell = []
      cell.append("")
      cell.append("")
    else:
      firstFlag = True
    cell.append(spec.text)
    list_of_rows.append(cell)
    
  list_of_rows.append(["", "", ""])


with open('laptopInfo.csv', 'w', newline='', encoding="utf-8") as file:
  writer = csv.writer(file)
  writer.writerow(["Title", "Price", "Specifications"])
  writer.writerows(list_of_rows)
    