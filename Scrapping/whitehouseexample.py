# python whitehouseexample.py

# from website
# https://www.whitehouse.gov/briefings-statements/

import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.whitehouse.gov/briefings-statements/")
src = result.content
soup = BeautifulSoup(src,'lxml')
