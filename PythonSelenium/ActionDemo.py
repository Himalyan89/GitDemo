import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# For Chrome browser
service_obj = Service("C:\\Users\Abhishek\Desktop\MY\Learning\Python\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID,'mousehover')).perform()
time.sleep(4)
action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()

action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()
time.sleep(3)
