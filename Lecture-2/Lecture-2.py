
# Importing Module
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Creating object for Chrome class
driver = webdriver.Chrome()

# Opening URL
driver.get("https://www.nopcommerce.com/en/demo")

# Maximize browser window
driver.maximize_window() 

time.sleep(1000)
driver.quit()