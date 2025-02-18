from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

# Application Commands 
title = driver.title # to capture the title of currrnt webpage
url = driver.current_url #to capture the current url of webpage
p_source = driver.page_source # to capture source code of webpage

print(title)
print(url)
print(p_source)

# Conditional Commoads
driver.get("https://omayo.blogspot.com/")
driver.maximize_window()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//form[@name='form1']//input[@type='text']")))

fname = driver.find_element(By.XPATH, "//form[@name='form1']//input[@type='text']")
print("Displayed status:", fname.is_displayed())
print("Enabled status: ", fname.is_enabled())

# is_selected
pen = driver.find_element(By.XPATH, "//div[@id='HTML33']//input[1]")
bag = driver.find_element(By.XPATH, "//input[@value='Bag']")

print("default radio button status: ")
print(pen.is_selected())
print(bag.is_selected())
pen.click()
print("After selecting radio button status: ")
print(pen.is_selected())
print(bag.is_selected())

# Browser Commands
#close() -- close single browse window
#quit() -- close all the browser window

# Navigational Comments

#back() - forward() - refresh()
driver.get("https://omayo.blogspot.com/")
driver.get("https://www.saucedemo.com/")
time.sleep(10)
driver.back() # omaya
time.sleep(10)
driver.forward() # saucedemo
time.sleep(10)
driver.refresh() # saucedemo

# Text vs get_attribute
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")

email = driver.find_element(By.XPATH, "(//input[@id='Email'])[1]")
email.clear()
email.send_keys("abc@gmail.com")
print("result of text: ", email.text)
print("result of get_attribute: ", email.get_attribute("value"))

button = driver.find_element(By.XPATH, "//button[normalize-space()='Log in']")
print("result of text: ", button.text)
print("result of get_attribute: ", button.get_attribute("value"))

time.sleep(10000)