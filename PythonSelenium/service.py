from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# For Chrome browser
service_obj = Service("C:\\Users\Abhishek\Desktop\MY\Learning\Python\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# Fire Fox
#service_obj = Service("C:\\Users\Abhishek\Desktop\MY\Learning\Python\Drivers\geckodriver-v0.34.0-win-aarch64\geckodriver.exe")
#driver = webdriver.Firefox(service=service_obj)

# For Edge
#service_obj = Service("C:\\Users\Abhishek\Desktop\MY\Learning\Python\Drivers\edgedriver_win64\msedgedriver.exe")
#driver = webdriver.Edge(service=service_obj)


driver.maximize_window()
driver.get("https://algomau.ca/")
print(driver.title)
Tit = driver.title
driver.get("https://algomau.ca/contact/")
#driver.minimize_window()
#driver.back()
#driver.refresh()
#driver.implicitly_wait(3000)
#driver.forward()




if Tit != "Home - Algoma":
    raise Exception(" Title does not match")

print(driver.current_url)
driver.close()