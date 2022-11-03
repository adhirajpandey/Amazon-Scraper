# amazon-scraper

# Description

This Project allows you to scrape data from amazon website.

There are three scrapers in this project :

  - product_details.py - Product link as input and Product Title and Price as Output.
  - search_results.py - Search Term as input and txt file of links of listed Products as Output.
  - links_csv.py - Text file of links as input and csv file with details as Output.
  
# Requirements

- python3
- pip3
- requests
- beautifulsoup4

# Usage

1. Clone this project `git clone https://github.com/adhirajpandey/amazon-scraper` and cd into it `cd amazon-scraper`
2. Install Requirements `pip install -r requirements.txt`
3. Run the Script `python product_details.py` or `python search_results.py` or `python links_csv.py`

# Scrape Product Details from Amazon Link

1. `python product_details.py`
2. Enter the link of the Amazon Product Page
3. Check Product deatails in Terminal

# Scrape Product Links from Search Page

1. `python search_results.py`
2. Enter the Search Term
3. Enter the number of pages upto which you want to scrape links
4. Enter the name of the output file
5. Check `[filename].txt` for Product links in Working Directory

# Scrape Details of Multiple Products

1. `python links_csv.py`
2. Enter path of the links txt file
3. Enter the name of the links txt file
4. Enter the output path where csv will be saved
5. Enter the name of desired output csv
6. Check [filename].csv for Product Details in path provided.
