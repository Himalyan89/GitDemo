import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
name = "Abhishek"
# For Chrome browser
service_obj = Service("C:\\Users\Abhishek\Desktop\MY\Learning\Python\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")


#to handle java or javascript pop-up(alerts)
driver.find_element(By.ID,"name").send_keys(name)
driver.find_element(By.CSS_SELECTOR,"#alertbtn").click()
time.sleep(3)

alert = driver.switch_to.alert
alerttext = alert.text
print(alerttext)
assert name in alerttext
alert.accept()



time.sleep(3)
