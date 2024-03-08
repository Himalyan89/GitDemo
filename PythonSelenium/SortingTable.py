import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# For Chrome browser
service_obj = Service("C:\\Users\Abhishek\Desktop\MY\Learning\Python\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
browserSortedVeg= []
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()

vegiWEBeLE = driver.find_elements(By.XPATH,"//tr/td[1]")
for ele in vegiWEBeLE:
    browserSortedVeg.append(ele.text)

orginalbrowsersortlist = browserSortedVeg.copy()

browserSortedVeg.sort()

assert browserSortedVeg == orginalbrowsersortlist

print(vegiWEBeLE)

sddsaasd