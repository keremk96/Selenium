# Importing Module
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Creating object for Chrome class
driver = webdriver.Chrome()
# Opening URL
driver.get("https://opensource-demo.orangehrmlive.com/")
# Entering username
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.NAME, "username")))

username = driver.find_element(By.NAME, "username")
username.send_keys("Admin")
# Entering password
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.NAME, "password")))

password = driver.find_element(By.NAME, "password")
password.send_keys("admin123")
# Clicking login button
login = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")
login.click()

# Capturing title of webpage
act_title = driver.title
exp_title = "OrangeHRM"
# Verifying title of webpage
if act_title == exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")

driver.quit()