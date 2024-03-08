

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


Chrome_Options = webdriver.ChromeOptions()
Chrome_Options.add_argument("--start-maximize")
Chrome_Options.add_argument("headless")
Chrome_Options.add_argument("--ignore-certificate-errors")
# For Chrome browser
service_obj = Service("C:\\Users\Abhishek\Desktop\MY\Learning\Python\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options= Chrome_Options)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()

print(driver.title)
