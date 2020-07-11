
from selenium import webdriver
PATH="C:\Program Files (x86)\chromedriver.exe"

driver  = webdriver.Chrome(PATH)

driver.get("https://www.bigbasket.com/cl/fruits-vegetables/")
print(driver.title)
driver.quit()