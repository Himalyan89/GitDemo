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

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[@href='/angularpractice/shop']").click()
Products = driver.find_elements(By.XPATH,"//div[@class='card h-100']")

for product in Products:
    productName = product.find_element(By.XPATH, "div/h4/a").text
    if productName == "Blackberry":
        product.find_element(By.XPATH,"div/button").click()
driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").click()
driver.find_element(By.XPATH,"//button[@class= 'btn btn-success']").click()
driver.find_element(By.ID,"country").send_keys("Ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH,"//input[@class='btn btn-success btn-lg']").click()
SucessMessage = driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']").text
print(SucessMessage)

assert "Success!" in SucessMessage
