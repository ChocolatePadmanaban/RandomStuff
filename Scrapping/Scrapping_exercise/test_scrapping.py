# test_scrapping.py

import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.google.com")

#print status code 
print("Stadus code",result.status_code)

# for status code refer https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

#print headers
#print("Headers: ", result.headers)
#https://en.wikipedia.org/wiki/List_of_HTTP_header_fields

#source of the page
src = result.content
#print("\n Source : ",src)


#create Beautiful soup object from src
soup = BeautifulSoup(src, 'lxml')

#find all the links
links= soup.find_all('a')
#print(links, '\n')

for link in links:
    if "About" in link.text:
        print(link)
        print(link.attrs['href'])
