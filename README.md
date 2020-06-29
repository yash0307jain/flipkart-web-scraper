# Flipkart web scraper

This is `Flipkart Product Web Scraper` build using `scrapy` module of `python`

# Features
It extracts the following:

  * Product Name
  * Product Price
  * Product highlights
  * Product Specifications in detail
  * Product Rating
  * Product Url

# Execute Flipkart scraper
### For Windows users
```sh
run.bat
```

### For Linux or Mac users
```sh
sh ./run.sh
```

### Or can run the following command
```bash
scrapy crawl amazon_scraper -o ./data/data.json
```

It will create `data.json` file inside the `data` folder containing all the scraped data in `JSON` format and all the images will be saved in `data/img/full` folder.

# Sample Data
Already fetched sample data is available in `data` folder

# Troubleshooting
If `data.json` file doesn't generate in proper format then just delete `data.json` file and `img` folder.  
Now you good to go ;)

# Preresuisites
- you have to install `scrapy`
- you have to install `pillow`

## Small example in Beautiful Soup - bs4
> It is extracting only `gaming laptop details` into a `laptop_data_.csv` file

[MIT]