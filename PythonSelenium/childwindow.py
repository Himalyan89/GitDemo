import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# For Chrome browser
service_obj = Service("C:\\Users\Abhishek\Desktop\MY\Learning\Python\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT,"Click Here").click()


WindowOpened = driver.window_handles
driver.switch_to.window(WindowOpened[1])
time.sleep(3)
print(driver.find_element(By.XPATH,"//h3").text)
driver.switch_to.window(WindowOpened[0])

assert "Opening a new window" == driver.find_element(By.XPATH,'//h3').text
