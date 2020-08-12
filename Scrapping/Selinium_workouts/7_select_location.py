from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from time import gmtime, strftime

PATH="C:\Program Files (x86)\chromedriver.exe"


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(PATH, chrome_options=options)
#driver  = webdriver.Chrome(PATH)

driver.implicitly_wait(10)

driver.get("https://www.bigbasket.com/")

try:
    

    element = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CLASS_NAME, "hvc")))
    element.click()
    
except Exception as e:
    print(e)

SCROLL_PAUSE_TIME = 2

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

elements = driver.find_elements_by_xpath("//a[contains(@href, 'onion-medium-vengayam')]")
for element in elements:
    print(element.text)

with open(strftime("%Y-%m-%d_%H-%M-%S", gmtime()), 'w') as Fruit_file:
    try:
        main = driver.find_elements_by_class_name("ng-binding")
        for element in main:
            Fruit_file.write(element.text+ "\n")
    except Exception as e :
        print(e)



# html = driver.page_source
# print(html)

driver.close()