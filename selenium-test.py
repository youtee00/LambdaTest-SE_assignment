from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions() 
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(options=options)

# Step 1: Visit amazon.in
driver.get("https://www.amazon.in")

# Step 2: Search for "iPhone 13"
search_box = driver.find_element("name", "field-keywords")
search_box.send_keys("iPhone 13")
search_box.submit()

# Wait for the search results to load
import time
time.sleep(5)

# Step 3: Get the price
try:
    # Locate the first search result (assuming it's the iPhone 13)
    price_element = driver.find_element(By.XPATH, "//span[@class='a-price']/span[@class='a-offscreen']")
    
    # Get the price from the first search result
    price = price_element.get_attribute("innerHTML")
    print("iPhone 13 Price:", price)

except Exception as e:
    print("Error:", e)

# Close the browser
driver.quit()