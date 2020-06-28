from bs4 import BeautifulSoup

soup = BeautifulSoup("Fru_veg.html", "lxml")

print(soup.prettify())