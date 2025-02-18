# Importing Module
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()

# Css Selectors

# Tag and ID
tag_id = driver.find_element(By.CSS_SELECTOR, "input#email")
ta_gid = driver.find_element(By.CSS_SELECTOR, "#email") # Usage of Tag name is optional
tag_id.send_keys("abc")

# Tag and Class
tag_class = driver.find_element(By.CSS_SELECTOR, "input.inputtext")
tag_class = driver.find_element(By.CSS_SELECTOR, ".inputtext") # Usage of Tag name is optional
tag_class.send_keys("12345")

# Tag and Attributte
tag_attribute = driver.find_element(By.CSS_SELECTOR, "input[data-testid=royal-email]")
tag_attribute = driver.find_element(By.CSS_SELECTOR, "[data-testid=royal-email]") # Usage of Tag name is optional
tag_attribute.send_keys("abc123")

# Tag and Class - Attribute
tag_CA = driver.find_element(By.CSS_SELECTOR, "input.inputtext[[data-testid=royal-email]]")
tag_CA = driver.find_element(By.CSS_SELECTOR, ".inputtext[data-testid=royal-email]") # Usage of Tag name is optional
tag_CA.send_keys(789)

# XPATH
driver.get("http://www.automationpractice.pl/")
driver.maximize_window()

# Absolute Xpath
Axpath = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div[3]/div/div/div[2]/form/input[4]")
Axpath.send_keys("T-shirt")

button = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div[3]/div/div/div[2]/form/button")
button.click()

# Relative Xpath
Rxpath = driver.find_element(By.XPATH, "//*[@id='search_query_top']")
Rxpath.send_keys("T-shirt")

button = driver.find_element(By.XPATH, "//*[@id='searchbox']/button")
button.click()

# Xpath with OR - AND
Orxpath = driver.find_element(By.XPATH, "//input[@id='search_query_top' or @name='search_query']")
Orxpath.send_keys("T-shirt")

button = driver.find_element(By.XPATH, "//button[@name='submit_search' and @type='submit']")
button.click()

# Xpath with CONTAINS and STARTS-WITH
Cxpath = driver.find_element(By.XPATH, "//input[contains(@id, 'search')]")
Cxpath.send_keys("T-shirt")

button = driver.find_element(By.XPATH, "//button[starts-with(@name, 'submit_')]")
button.click()

# Xpath with TEXT
Txpath = driver.find_element(By.XPATH, "//a[text()= 'Women']")
Txpath.click()

time.sleep(10000000)
driver.quit()
