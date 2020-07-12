from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH="C:\Program Files (x86)\chromedriver.exe"
driver  = webdriver.Chrome(PATH)

driver.get("https://www.bigbasket.com/cl/fruits-vegetables/")
# search = driver.find_element(by='id',value='input')
# search.send_keys("Mango")
# search.send_keys(Keys.RETURN)




try:
    main = driver.find_elements_by_class_name("ng-binding")
    for element in main:
        print(element.text)
except Exception as e :
    print(e)


time.sleep(30)
driver.quit()