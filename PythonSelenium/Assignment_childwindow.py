import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# For Chrome browser
service_obj = Service("C:\\Users\Abhishek\Desktop\MY\Learning\Python\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.XPATH,"//a[@class='blinkingText']").click()

WindowOp = driver.window_handles

driver.switch_to.window(WindowOp[1])
mail = driver.find_element(By.XPATH,"//p[@class='im-para red']").text
print(mail)
split_text = mail.split(' ')
confirm_mail = split_text[4]
print(confirm_mail)

driver.switch_to.window(WindowOp[0])
driver.find_element(By.ID,"username").send_keys(confirm_mail)

driver.find_element(By.ID,"password").send_keys("password")
time.sleep(3)
driver.find_elements(By.XPATH,"//span[@class='checkmark']")[1].click()
time.sleep(3)
driver.find_element(By.ID,"terms").click()
driver.find_element(By.ID,"signInBtn").click()
time.sleep(3)







time.sleep(2)