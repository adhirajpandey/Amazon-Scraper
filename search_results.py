from bs4 import BeautifulSoup
import requests

def scrape_search_page(url):
    #saves all the links in a list
    link = url 
    
    links_in_page , temp = [] , []

    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}

    page = requests.get(link, headers = header)

    soup = BeautifulSoup(page.content , "html.parser")

    soup1 = BeautifulSoup(soup.prettify(), "lxml")

    links = soup.find_all("a", attrs={'class':'a-link-normal s-no-outline'})    

    for link in links:
        temp.append(link.get('href'))

    #cleaning an filtering links and crap links
    for i in temp:
        i = i.strip()
        if('sspa' not in i):
            links_in_page.append(i)

    return links_in_page


def create_text_file(list,name):
    #prints list of links in txt file of user defined name line by line
    with open(f'{name}.txt', 'w') as f:
        for item in list:
            f.write("https://www.amazon.in" + item + "\n")



#OPERATOR CODE 

search_term = input("Enter the search term (keyword) : ")

n_page = input("Enter the number of pages you want to search upto (max-20) : ")

output_name = input("Enter the name of the output txt file (without extension) : ")


search_term = search_term.replace(" ", "+")

base_page = "https://www.amazon.in/s?k=" + search_term


#generate links for further scraping 
input_links = []

for i in range(1,int(n_page)+1):
    query = base_page + "&page=" + str(i)
    input_links.append(query)

#https://www.amazon.in/s?k=pendrive&page=7

#saving ALL the links in one single list 
final = []

for i in input_links:
    print(f"Currently on page number : {input_links.index(i) + 1}")
    temp = scrape_search_page(i)
    final.extend(temp)

#genrating txt file
create_text_file(final, output_name)


