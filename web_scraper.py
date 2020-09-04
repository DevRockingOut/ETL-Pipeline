import pyderman as dr
import time
import sys

# using selenium library to get content of dynamic web page
from selenium import webdriver  
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import database


def installDriver():
    # check if the Chromedriver is installed and, if not, downloads everything required
    path = dr.install(browser=dr.chrome, file_directory='./lib/', verbose=True, chmod=True, overwrite=False, version=None, filename=None, return_info=False)
    print('Installed chromedriver to path: %s' % path)
    return path

def getPageContents(url):
    # get chrome driver path
    path = installDriver()

    # open chrome as a background process
    chrome_options = Options()
    chrome_options.add_argument('--headless') 

    driver = webdriver.Chrome(
        executable_path = path,
        options = chrome_options
    )

    # load page
    driver.get(url)

    timeout = 3
    try:
        # wait until critical products table is loaded
        element_present = EC.presence_of_element_located((By.CLASS_NAME, 'critical-product-table-container'))
        WebDriverWait(driver, timeout).until(element_present)

        # get data from web page
        products = getData(driver)

        # close chrome driver
        driver.quit()

        # store critical products in database
        database.storeProducts(products)
        
    except TimeoutException:
        print("Timed out waiting for page to load")
        driver.quit()
    

def getData(driver):
    # get Critical Products info
    critical_products = driver.find_elements_by_class_name('critical-product-table-container')[0]

    products_name = critical_products.find_elements_by_class_name('line-item-title')
    products_total_available = critical_products.find_elements_by_class_name('available')

    products = []

    for i in range(len(products_name)):
        products.append([products_name[i].text, products_total_available[i].text])
    
    # return the list of critical products
    return products
    
    
def run(i, secs):
    while i > 0:
        getPageContents('https://www.rrpcanada.org/#/')
        time.sleep(secs)  # wait x seconds before getting new data
        i -= 1


if len(sys.argv) > 1:
    run(int(sys.argv[1]), int(sys.argv[2]))
else:
    run(1, 0)