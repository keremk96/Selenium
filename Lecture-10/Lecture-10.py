from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()

# Mouse Operations

# Mouse Hover
driver.get("https://omayo.blogspot.com/")

blog = driver.find_element(By.XPATH, "//a[@href='#']")
sel = driver.find_element(By.XPATH, "//*[@id='cssmenu']/ul/li[2]/ul/li[1]/a")

act = ActionChains(driver)
act.move_to_element(blog).move_to_element(sel).click().perform()

# Right Click
driver.get("https://demo.guru99.com/test/simple_context_menu.html")

button = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")

act = ActionChains(driver)
act.context_click(button).perform() # right click

# Double Click
driver.get("https://demo.guru99.com/test/simple_context_menu.html")

double = driver.find_element(By.XPATH, "//button[normalize-space()='Double-Click Me To See Alert']")

act = ActionChains(driver)
act.double_click(double).perform() # double click

# Drag and Drop
driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

source_ele = driver.find_element(By.ID, "box6")
target_ele = driver.find_element(By.ID, "box106")

act = ActionChains(driver)
act.drag_and_drop(source_ele,target_ele).perform() # drag and drop operation

# Slider
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")

min_slider = driver.find_element(By.XPATH, "//*[@id='slider-range']/span[1]")
max_slider = driver.find_element(By.XPATH, "//*[@id='slider-range']/span[2]")

print("Location of slider Before moving ..........")
print(min_slider.location) # {'x': 59, 'y': 294}
print(max_slider.location) # {'x': 485, 'y': 294}

act = ActionChains(driver)
act.drag_and_drop_by_offset(min_slider,100,0).perform()
act.drag_and_drop_by_offset(max_slider,-39,0).perform()

print("Location of slider After moving ..........")
print(min_slider.location) # {'x': 59, 'y': 294}
print(max_slider.location) # {'x': 485, 'y': 294}

# Scrolling page
driver.get("https://www.worldometers.info/geography/flags-of-the-world/")

# 1) scroll down page by pixel
driver.execute_script("window.scrollBy(0,3000)", "")
value = driver.execute_script("return window.pageYOffset;")

print("Number of pixels moved: ", value)

# 2) Scroll down page till the element is visible
driver.get("https://www.worldometers.info/geography/flags-of-the-world/")

flag = driver.find_element(By.XPATH, "//img[@src='/img/flags/small/tn_tu-flag.gif']")

driver.execute_script("arguments[0].scrollIntoView();", flag)
value = driver.execute_script("return window.pageYOffset;")

print("Number of pixels moved: ", value)


# 3) Scroll down page till end
driver.get("https://www.worldometers.info/geography/flags-of-the-world/")

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)", "")

value = driver.execute_script("return window.pageYOffset;")

print("Number of pixels moved: ", value)

# Scroll up starting position

time.sleep(3)
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)", "")

value = driver.execute_script("return window.pageYOffset;")

print("Number of pixels moved: ", value)