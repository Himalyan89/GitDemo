import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# For Chrome browser
service_obj = Service("C:\\Users\Abhishek\Desktop\MY\Learning\Python\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame('mce_0_ifr')
driver.find_element(By.XPATH,"//body[@id='tinymce']").clear()
driver.find_element(By.XPATH,"//body[@id='tinymce']").send_keys("Hello, I am inside Iframe")

driver.switch_to.default_content()


print(driver.find_element(By.CSS_SELECTOR,'h3').text)

assert  "An iFrame containing the TinyMCE WYSIWYG Editor"  == driver.find_element(By.CSS_SELECTOR,'h3').text