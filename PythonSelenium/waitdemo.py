import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

name = "Abhishek"
# For Chrome browser
service_obj = Service("C:\\Users\Abhishek\Desktop\MY\Learning\Python\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, '.search-keyword').send_keys("ber")
time.sleep(5)
results = driver.find_elements(By.XPATH, "//div[@class= 'products']/div")
print(len(results))
count = len(results)
assert count ==3

for result in results:
    result.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()= 'PROCEED TO CHECKOUT']").click()


#Sum Validation----------------
Prices = driver.find_elements(By.XPATH,"//tr/td[5]/p")
Sum = 0
for price in Prices:
    Sum= Sum+ int(price.text)
print(Sum)








time.sleep(5)
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CSS_SELECTOR,".promoInfo").text)

TotalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)

assert Sum == TotalAmount

DiscountPrice = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)

print(DiscountPrice)

assert TotalAmount > DiscountPrice





