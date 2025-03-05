from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium. webdriver import ActionChains, Keys
import time

driver = webdriver.Chrome()

driver.get("https://text-compare.com/")
driver.maximize_window()

# Actions

input1 = driver.find_element(By.XPATH, "//textarea[@id='inputText1']")
input2 = driver.find_element(By.XPATH, "//textarea[@id='inputText2']")

input1.send_keys("welcome to selenium")

act = ActionChains(driver)

# Ctrl+A
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
# Ctrl+C
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
# Press Tab
act.send_keys(Keys.TAB).perform()
# Ctrl+V
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

# Download File
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
driver.maximize_window()
driver.find_element(By.XPATH, "//tbody/tr[1]/td[5]/a[1]").click()

# Download PDF
preferences = {"plugins.always_open_pdf_externally":True}
ops = webdriver.ChromeOptions()
ops.add_experimental_option("prefs",preferences)
driver = webdriver.Chrome(options=ops)

driver.get("https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/")
driver.maximize_window()
driver.find_element(By.XPATH, "//tbody/tr[1]/td[5]/a[1]").click()