from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import requests

driver = webdriver.Chrome()
driver.get("https://omayo.blogspot.com/")
driver.maximize_window()

# CheckBox

# 1) Selecting speciffx checkhbox
cbox = driver.find_element(By.XPATH, "//div[@id='HTML33']//input[1]")
cbox.click()

# 2) Selecting all checkboxes
mbox = driver.find_elements(By.XPATH, "//input[@type='checkbox' and @name='accessories']")
for i in range(len(mbox)):
    mbox[i].click()

# 3) Seleckting multiple checkboxes by choice
mbox = driver.find_elements(By.XPATH, "//input[@type='checkbox' and @name='accessories']")
for i in range(len(mbox)):
    item = mbox[i].get_attribute("value")
    if item == "Pen" or item == "Bag":
        mbox[i].click()

# 4) Clearing all checkboxes
cbox =  driver.find_elements(By.XPATH, "//input[@type='checkbox' and @name='accessories']")
for box in cbox:
    if box.is_selected():
        box.click()

# Link
driver.get("https://www.nopcommerce.com/en/demo")
driver.maximize_window()
# href ==> hyperlink reference (html)
link = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.LINK_TEXT, "Features"))
)
link.click()

# Find number of links in a page
#links = driver.find_elements(By.TAG_NAME, "a")
links = driver.find_elements(By.XPATH, "//a")
print("total number of links: ", len(links))
for n in links:
    print(n.text)

# Broken links
driver.get("http://www.deadlinkcity.com/")
all_links = driver.find_elements(By.TAG_NAME, "a")

count = 0
for link in all_links:
    url = link.get_attribute("href")
    try:
        res = requests.head(url)
    except:
        None

    if res.status_code>=400:
        print(url, " is broken link")
        count+=1
    else:
        print(url, " is valid link")
print("Total numbber of broken links: ", count)

# Dropdown
driver.get("https://practice.expandtesting.com/dropdown")
drp = driver.find_element(By.XPATH, "//select[@id='country']")
drpcountry = Select(drp)

# select option from dropdown
drpcountry.select_by_visible_text("Turkey")
drpcountry.select_by_value("abc")
drpcountry.select_by_index(12)

# capture all options from dropdown
alloptions = drpcountry.options
print("Total number of options: ", len(alloptions))

for opt in alloptions:
    print(opt.text)

# select option from dropdown without using built-in method
for opt in alloptions:
    if opt.text=="Turkey":
        opt.click()
        break