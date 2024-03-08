from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set the path to your WebDriver executable (e.g., chromedriver.exe for Chrome)
webdriver_path = "path/to/chromedriver.exe"

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(executable_path=webdriver_path)

# Navigate to Google's homepage
driver.get("https://www.google.com")

# Find the search input element by its name attribute value (in this case, 'q' for the Google search bar)
search_box = driver.find_element("name", "q")

# Type the search query into the search box
search_box.send_keys("Selenium testing with Python")

# Press Enter to perform the search
search_box.send_keys(Keys.RETURN)

# Allow some time for the search results to load
time.sleep(3)

# Verify that the page title contains the search query
assert "Selenium testing with Python" in driver.title

# Print the title of the page
print("Page title:", driver.title)

# Close the browser window
driver.quit()
