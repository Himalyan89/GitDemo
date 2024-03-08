import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# For Chrome browser
service_obj = Service("C:\\Users\Abhishek\Desktop\MY\Learning\Python\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID, 'autosuggest').send_keys("Ind")
time.sleep(2)
Countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(Countries))

for country in Countries:
    if country.text == 'India':
        country.click()
        break

assert driver.find_element(By.ID, 'autosuggest').get_attribute("value") == "India"