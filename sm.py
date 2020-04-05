from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC

opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1")

chromedriver = 'C:\\chromedriver.exe'
browser = webdriver.Chrome(chromedriver, chrome_options=opts)

browser.get('https://www.microsoft.com/en-gb/software-download/windows10ISO')
edition_dropdown = browser.find_element_by_id('product-edition')
edition_options = edition_dropdown.find_elements_by_tag_name("option")
print(edition_options)
for option in edition_options:
    print(option.get_attribute("value"))
    option.click()

browser.find_element_by_id('submit-product-edition').click()

language_dropdown = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "product-languages"))
    )
#language_dropdown = browser.find_element_by_id('product-languages')
language_options = edition_dropdown.find_elements_by_tag_name("option")
print(language_options)
language_options.find_element_by_xpath("//div[@label='English']").click()

browser.find_element_by_id('submit-sku').click()
