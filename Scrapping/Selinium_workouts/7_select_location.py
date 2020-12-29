from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from time import gmtime, strftime
#just checking the change

def Locating_Location(location):
    PATH="/usr/bin/chromedriver_linux64/chromedriver"


    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(PATH, chrome_options=options)
    #driver  = webdriver.Chrome(PATH)

    driver.implicitly_wait(10)

    driver.get("https://www.bigbasket.com/")

    try:
        

        element = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CLASS_NAME, "hvc")))
        element.click()
        element = driver.find_element_by_xpath("""//*[@id="headerControllerId"]/header/div/div/div/div/ul/li[2]/div/div/div[2]/form/div[1]/div/div/span/span[2]/span""")
        driver.execute_script("$(arguments[0]).click();", element)
        

        
    except Exception as e:
        print(e)



    driver.close()