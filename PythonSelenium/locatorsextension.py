from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# For Chrome browser
service_obj = Service("C:\\Users\Abhishek\Desktop\MY\Learning\Python\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/client")
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("tom_tester@yopmail.com")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("Tom@12345")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Tom@12345")
driver.find_element(By.XPATH, "//button[@type = 'submit']").click()
