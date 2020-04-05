import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC

def get_latest_links():
    opts = Options()
    opts.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1")
    opts.add_argument("--headless")
    opts.add_argument("window-size=1920,1080")
    chromedriver = 'chromedriver.exe'
    browser = webdriver.Chrome(chromedriver, chrome_options=opts)

    browser.get('https://www.microsoft.com/en-gb/software-download/windows10ISO')
    edition_dropdown = browser.find_element_by_id('product-edition')
    edition_options = edition_dropdown.find_elements_by_tag_name("option")
    for option in edition_options:
        option.click()

    browser.find_element_by_id('submit-product-edition').click()
    language_dropdown = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "product-languages"))
        )
    language_dropdown = browser.find_element_by_id('product-languages')
    language_options = language_dropdown.find_elements_by_tag_name("option")
    for option in language_options:
        try:
            if json.loads(option.get_attribute("value"))["language"] == "English":
                option.click()
        except:
            pass

    browser.find_element_by_id('submit-sku').click()
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@class='button button-long button-flat button-purple']")))
    download_btns = browser.find_elements(By.XPATH, "//*[@class='button button-long button-flat button-purple']")
    links = [btn.get_attribute('href') for btn in download_btns]
    bit32 = [l for l in links if "x32.iso" in l][0]
    bit64 = [l for l in links if "x64.iso" in l][0]
    browser.close()
    return bit32, bit64
