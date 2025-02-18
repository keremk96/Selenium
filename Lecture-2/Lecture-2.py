
# Importing Module
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Creating object for Chrome class
driver = webdriver.Chrome()

#Opening URL
driver.get("https://www.saucedemo.com/")
 
#Maximize the browser window
driver.maximize_window()

# ID Locater
id = driver.find_element(By.ID, "user-name")
id.send_keys("standard_user")

#Name locater
name = driver.find_element(By.NAME, "user-name")
name.send_keys("standard_user")

# Opening URL
driver.get("https://www.facebook.com/")
driver.maximize_window()

# LINK_TEXT
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.LINK_TEXT, "Forgotten password?")))

link_text = driver.find_element(By.LINK_TEXT, "Forgotten password?")
link_text.click()

# PARTIAL_LINK_TEXT Locater
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Forgotten")))

partial_link_text = driver.find_element(By.PARTIAL_LINK_TEXT, "Forgotten")
partial_link_text.click()

# Opening URL
driver.get("https://www.google.com.tr/")
driver.maximize_window()

# Class Name Locater
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf")))

class_name = driver.find_element(By.CLASS_NAME, "gLFyf")
class_name.send_keys("Selenium")

time.sleep(1000)
driver.quit()