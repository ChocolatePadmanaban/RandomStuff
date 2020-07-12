
from selenium import webdriver
import time
PATH="C:\Program Files (x86)\chromedriver.exe"

driver  = webdriver.Chrome(PATH)

driver.get("https://www.bigbasket.com/cl/fruits-vegetables/")
print(driver.title)
time.sleep(30)
driver.quit()