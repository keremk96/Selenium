from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

# Alerts/Popups
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

alert = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']")
alert.click()

alertwindow = driver.switch_to.alert
print(alertwindow.text)

alertwindow.send_keys("welcome")
alertwindow.accept() # close alert windoow by using OK button
alertwindow.dismiss() # close alert window by using CANCEL button

# Authentication popups
driver.get("https://admin:admin@the-internet.herokuapp.com/digest_auth")

# Frame/Iframe
driver.get("AAAAAAA")
driver.maximize_window()

#driver.switch_to.frame(" name of the frame")
#driver.switch_to.frame(" id of the frame" )
#driver.switch_to.frame(" webelement")
#driver.switch_to.frame(" indedx (0) ")

driver.switch_to.frame("xxx")
driver.find_element(By.LINK_TEXT, "------").click()
driver.switch_to.default_content() # go back to main page

driver.switch_to.frame("aaaaa")
driver.find_element(By.LINK_TEXT, "pppppp").click
driver.switch_to.default_content()

driver.switch_to.frame("rrrrr")
driver.find_element(By.XPATH, "//------").click

# Inner Frame
driver.get("http://demo.automationtesting.in/Frames.html")
driver.maximize_window()

driver.find_element(By.XPATH, "/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[2]/a").click()

outerframe = driver.find_element(By.XPATH, "//*[@id='Multiple']/iframe")
driver.switch_to.frame(outerframe)

innerframe = driver.find_element(By.XPATH, "/html/body/section/div/div/iframe")
driver.switch_to.frame(innerframe)

driver.find_element(By.XPATH, "/html/body/section/div/div/div/input").send_keys("welcome")
driver.switch_to.parent_frame() # directlt switch to parent frame(outerframe)

# Browser Windows
# switch_to.window(WindowId)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

windowid = driver.current_window_handle # windowID changes every time
print(windowid) 

time.sleep(5)
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[3]/div[2]/p[2]/a").click()
windowIDs = driver.window_handles

parentWID = windowIDs[0]
childWID = windowIDs[1]
print(parentWID, childWID)

driver.switch_to.window(childWID)
print(driver.title)

driver.switch_to.window(parentWID)
print(driver.title)

######
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

time.sleep(5)
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[3]/div[2]/p[2]/a").click()
windowIDs = driver.window_handles

for winid in windowIDs:
    driver.switch_to.window(winid)
    print(driver.title)

# close specific browser window
for winid in windowIDs:
    driver.switch_to.window(winid)
    if driver.title == "OrangeHRM":
        driver.close()