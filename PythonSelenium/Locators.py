import time

from select import select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# For Chrome browser
service_obj = Service("C:\\Users\Abhishek\Desktop\MY\Learning\Python\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")

# Types of locators - ID, Xpath, CSSSelector, Name, ID, Classname, LinkText

driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Tom")
driver.find_element(By.NAME,"email").send_keys("tester@yopmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("tester123")
driver.find_element(By.ID,"exampleCheck1").click()
driver.find_element(By.CSS_SELECTOR, "input[id='inlineRadio1']")

#Static Dropdown


dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_index(1)
dropdown.select_by_visible_text("Female")
time.sleep(5)



# Syntax to create xpath --- //tagname[@attribute='value]
#Syntax to locate element using css-- tagname[attribute='']
driver.find_element(By.XPATH,"//input[@type='submit']").click()
message = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
print(message)


assert "Success" in message

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Hello Again")

