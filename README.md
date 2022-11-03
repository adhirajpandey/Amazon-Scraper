# amazon-scraper

# Description

This Project allows you to scrape data from amazon website.

Below are the scrapers used in this project :

  - product_details.py - Product link as input and Product Title, Price, Rating, Number of Reviews as Output.
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
6. Check `[filename].csv` for Product Details in path provided.

# Examples

1. product_details.py

   ![product_details](https://user-images.githubusercontent.com/87516052/199699951-b1e14af6-af27-4d73-9c8b-99ace5ee68fa.png)
   
2. search_results.py

   ![search_results1](https://user-images.githubusercontent.com/87516052/199700295-c5480652-bb04-468a-924b-927c26c657f0.png)
   
   ![search_results2](https://user-images.githubusercontent.com/87516052/199700511-fac42eee-0510-4b3b-97e3-0e99dc76dfa0.png)

3. links_csv.py
   
   ![links_csv1](https://user-images.githubusercontent.com/87516052/199701273-ab6b2f96-2d55-4321-8535-2ff79e91a0e5.png)
   
   ![links_csv2](https://user-images.githubusercontent.com/87516052/199701499-23999571-ca0c-47d5-ae09-a8da9bd32133.png)

   ![links_csv3](https://user-images.githubusercontent.com/87516052/199702495-02fed760-959f-48f0-b778-2fbeccfbfd0d.png)

   

