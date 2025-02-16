# Importing Module
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Creating object for Chrome class
driver = webdriver.Chrome()

# Opening URL
driver.get()









time.sleep(1000)
driver.quit()