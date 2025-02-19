from selenium import webdriver
from selenium.common import ElementNotSelectableException, ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

# Wait Commands

# implicit wait

driver.get("https://www.google.com.tr/")
driver.implicitly_wait(10)

# explicit wait

from selenium.common import ElementNotSelectableException, ElementNotVisibleException, NoSuchElementException
mywait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
                                                                         ElementNotVisibleException,
                                                                         ElementNotSelectableException,
                                                                         Exception])

searchbox = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//textarea[@id='APjFqb']"))
)

#searchbox = driver.find_element(By.XPATH, "//textarea[@id='APjFqb']")
searchbox.send_keys("Selenium")
searchbox.submit()

sel = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//h3[normalize-space()='Selenium']"))
)

#sel = driver.find_element(By.XPATH, "//h3[normalize-space()='Selenium']")
sel.click()







