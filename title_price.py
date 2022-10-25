#importing all the required libraries

from bs4 import BeautifulSoup       #for scraping web data
import requests                     #for handling web requests


#FUNCTION DEFINITIONS


#checking validity of link and prints error msg if wrong (returns boolean)
def validLink(link):
    valid = True
    
    if(('http' or 'com') not in link):
        print("*****************************")
        print("Please enter a valid link (starting with http or https)")
        print("*****************************")
        
        valid = False

    elif('amazon' not in link):
        print("*****************************")
        print("Please enter only amazon link")
        print("*****************************")  

        valid = False

    return (valid)

#cleaning link (returns link)
def cleanLink(link):
    if('?' in link):
        ch = '?'
        link = link.split(ch, 1)[0]
    else:
        link = link.split()
    
    return(link)

#this function takes url and return title and price
def scrape(url):
    URL = link

    header ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}

    #getting page using requests module

    page = requests.get(URL, headers=header)


    #getting html content with proper formatting 

    soup1 = BeautifulSoup(page.content, "html.parser")

    #defining title and price

    title = soup1.find(id='productTitle').get_text()
    price = soup1.find('span', attrs={'class':'a-price-whole'}).get_text()


    #cleaning title and price

    title = title.strip()
    price = price.strip()

    price = price[:-1]

    return (title,price)

#this function takes title,price and starts printing output 
def printData(title,price):
    
    print("The Product is : ", end="")
    print(title)
    print("-" * (17 + len(title)))
    print("The Price of Product is : ", end="")
    print(price)

#this function prints extras like cleanlink, estimated time 
def printExtra():
    if(validLink(link) == True):

        #displaying clean url
        print("\n")
        clink = cleanLink(link)
        print("The cleaner url is : ",end="")
        print(clink)
        print("\n")

        #printing estimated time for user
        print("Estimated Maximum time for running script : 5 seconds")



#OPERATOR CODE


#printing scraping script name 
print("\n")
result = "SCRAPE AMAZON"
print(result)
print("\n")


#taking input from user
link = input("Enter the link of Amazon Product Page : ")

printExtra()

if(validLink(link) == True):
    url = cleanLink(link)
    title , price = scrape(url)
    
    print("\n")
    printData(title, price)
    
    print("\n")
    print(f"Thanks a lot for using the tool !!")
    print(f"If you have any feedback, follow up here : ", end="")
    print(f"https://github.com/adhirajpandey")
    print("\n")


