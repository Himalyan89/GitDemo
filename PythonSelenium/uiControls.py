import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# For Chrome browser
service_obj = Service("C:\\Users\Abhishek\Desktop\MY\Learning\Python\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
Checkboxes =  driver.find_elements(By.XPATH, "//input[@type = 'checkbox']")

print(len(Checkboxes))

for checkbox in Checkboxes:
    if checkbox.get_attribute('value')== "option2":
        checkbox.click()
        time.sleep(3)
        assert checkbox.is_selected()
        break

'''Radios = driver.find_elements(By.XPATH, "//input[@type= 'radio']")
print(len(Radios))

for radio in Radios:
    if radio.get_attribute('value') == "radio2":
        radio.click()
        time.sleep(2)

        assert radio.is_selected()
        #raise AssertionError("Not selected")
        break'''
Radios = driver.find_elements(By.CSS_SELECTOR, '.radioButton')
Radios[2].click()
assert Radios[2].is_selected()
time.sleep(2)

assert driver.find_element(By.ID, 'displayed-text').is_displayed()
driver.find_element(By.ID,'hide-textbox').click()

assert not driver.find_element(By.ID, 'displayed-text').is_displayed()



