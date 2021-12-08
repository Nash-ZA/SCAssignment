from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
import sys

s = Service('C:\Drivers\ChromeDriver\chromedriver.exe')
img_path = 'C:\\Selenium\\img.jpg'
driver = webdriver.Chrome(service=s)

# Open demoga Web Page
driver.get("https://demoqa.com/")

title = driver.title
action = ActionChains(driver)

print(title)

if title == "ToolsQA":
    print("Page Loaded successfully")
else:
    driver.close()
    sys.exit("Script Ended due to incorrect page loaded")

driver.maximize_window()

time.sleep(1)

# Click on Forms Card
driver.find_element(By.XPATH, "//*[@class='card-body']//H5[text() = 'Interactions']").click()
print("")
print("Interactions Display Card Clicked")

# Click on Practice Form List Selection
driver.find_element(By.XPATH, "//*[contains(text(), 'Droppable')]").click()
print("")
print("Practice Form List Selection Clicked")

# Find Draggable Object and Drag Target

DragObj = driver.find_element(By.XPATH, "//*[@id='draggable']")
DragDestination = driver.find_element(By.XPATH, "//*[@id='droppable']")

# Perform Drag and Drop
action.drag_and_drop(DragObj, DragDestination).perform()
print("")
print("Drag and Drop Performed")

# Validate Drag and Drop was successful
driver.find_element(By.XPATH, "//*[@id='droppable']/p[text()='Dropped!']")
print("")
print("Drag and Drop Validated")

# Navigate to Second Tab (Accept Tab)
driver.find_element(By.XPATH, "//*[@id='droppableExample-tab-accept']").click()
DragAcceptable = driver.find_element(By.XPATH, "//*[@id='acceptable']")
DragNotAcceptable = driver.find_element(By.XPATH, "//*[@id='notAcceptable']")
DragDestination1 = driver.find_element(By.XPATH, "//*[@id='droppable' and @class='drop-box ui-droppable']")

action.drag_and_drop(DragNotAcceptable, DragDestination1).perform()
state = DragDestination1.get_attribute("class")

if 'ui-state-highlight' in state:
    print("Validation Failed. Drag and Drop accepted for Not Acceptable Object")
    driver.close()
    sys.exit("Script Ended due to drag and Drop accepted for Not Acceptable Object")

action.drag_and_drop(DragAcceptable, DragDestination1).perform()

action.drag_and_drop(DragNotAcceptable, DragDestination1).perform()
state = DragDestination1.get_attribute("class")

if 'ui-state-highlight' in state:
    print("Validation Successful. Drag and Drop accepted")
else:
    driver.close()
    sys.exit("Script Ended due to drag and Drop not accepted for Acceptable Object")

driver.find_element(By.XPATH, "//*[@id='droppableExample-tab-preventPropogation']").click()

DragMe = driver.find_element(By.XPATH, "//*[@id='dragBox']")
OuterNGreedy = driver.find_element(By.XPATH, "//*[@id='notGreedyDropBox']")
InnerNGreedy = driver.find_element(By.XPATH, "//*[@id='notGreedyInnerDropBox']")
OuterGreedy = driver.find_element(By.XPATH, "//*[@id='greedyDropBox']")
InnerGreedy = driver.find_element(By.XPATH, "//*[@id='greedyDropBoxInner']")

action.click_and_hold(DragMe).move_to_element(OuterNGreedy).pause(1).move_by_offset(0, -100).release().perform()
time.sleep(1)

print("")
print("Move DragMe to Outer Greedy Box")
state = InnerNGreedy.get_attribute("class")

if 'ui-state-highlight' in state:
    print("Validation Failed. Inner Greedy box should be highlighted but not triggered")
    driver.close()
    sys.exit("Script Ended due to Inner Greedy box should be highlighted but not triggered")
else:
    print("Validation Successful. Inner Greedy box is highlighted but not triggered")

print("")
print("Move DragMe to Inner Greedy Box")
action.drag_and_drop(DragMe, InnerNGreedy).perform()

state = InnerNGreedy.get_attribute("class")

if 'ui-state-highlight' in state:
    print("")
    print("Validation Successful. Inner Greedy box is highlighted and triggered")
else:
    print("Validation Failed. Inner Greedy box should be highlighted and triggered")
    driver.close()
    sys.exit("Script Ended due to Inner Greedy box should be highlighted and triggered")

print("")
print("Move DragMe to Inner Not Greedy Box")
action.drag_and_drop(DragMe, InnerGreedy).perform()

state = OuterGreedy.get_attribute("class")

if 'ui-state-highlight' in state:
    print("Validation Failed. Outer Greedy box should not be highlighted")
    driver.close()
    sys.exit("Script Ended due to Outer Greedy box should not be highlighted")
else:
    print("")
    print("Validation Successful. Outer Greedy box is not highlighted")

print("")
print("Move DragMe to Outer Not Greedy Box")
action.click_and_hold(DragMe).move_to_element(OuterGreedy).pause(1).move_by_offset(0, -100).release().perform()

state = InnerGreedy.get_attribute("class")

if 'ui-state-highlight' in state:
    print("")
    print("Validation Successful. Outer Greedy trigger validated")
else:
    driver.close()
    sys.exit("Script Ended due to drag and Drop not accepted for Inner Greedy Object")

    print("")
    print("Execution Completed")
driver.close()
