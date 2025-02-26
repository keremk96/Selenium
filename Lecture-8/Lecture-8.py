from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Notification Popups
# come from browser. we can not directly interact with it
ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=ops)

driver.get("https://whatmylocation.com/")
driver.maximize_window()

driver = webdriver.Chrome()
# WebTable

# html tag ==> <table>
# <tbody> ==> representing hole table
# <tr> ==> table row
# <th> ==> table header
# <td> ==> table data

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# 1) Counting number of rows and columns
Nrows = driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr")
Ncol = driver.find_elements(By.XPATH, "//table[@name='BookTable']//th")
print(len(Nrows))
print(len(Ncol))

# 2) Read specific row and column data
data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[5]/td[3]") # 5th row, 3rd column
print(data.text)

# 3) Read all rows and columns
Nrows = driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr")
Ncol = driver.find_elements(By.XPATH, "//table[@name='BookTable']//th")

for r in range(2,len(Nrows)+1):
    for c in range(1,len(Ncol)+1):
        data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]")
        print(data.text, end= '    ')
    print()

# Read data based on condition
Nrows = driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr")

for r in range(2,len(Nrows)+1):
    Name = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]")
    if Name.text == "Mukesh":
        Book = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" +str(r)+ "]/td[1]")
        print(Book.text)

# Dynamic Table
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"))
).send_keys("admin")
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123")
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
time.sleep(3)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a"))
).click()

time.sleep(3)

rows = driver.find_elements(By.XPATH, "//div[@role='table']/div[2]/div/div/div[5]/div")
print(len(rows))
count = 0
for r in range(1,len(rows)+1):
    status = driver.find_element(By.XPATH, "//div[@role='table']/div[2]/div["+str(r)+"]/div/div[5]/div").text
    if status == "Enabled":
        count = count+1

print("Total number of rows: ", len(rows))
print("Number of enabled users:  ", count)
print("Number of disabled users:  ", len(rows)-count)