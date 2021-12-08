from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import sys

s = Service('C:\Drivers\ChromeDriver\chromedriver.exe')
img_path = 'C:\\Selenium\\img.jpg'

options = Options()
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--headless");
options.add_argument("window-size=1920,1080");
driver = webdriver.Chrome(options=options, service=s)


# Open demoga Web Page
driver.get("https://demoqa.com/")

title = driver.title

print(title)

if title == "ToolsQA":
    print("Page Loaded successfully")
else:
    driver.close()
    sys.exit("Script Ended due to incorrect page loaded")

time.sleep(1)

# Click on Forms Card
driver.find_element(By.XPATH, "//*[@class='card-body']//H5[text() = 'Elements']").click()
print("Elements Display Card Clicked")

# Click on Practice Form List Selection
driver.find_element(By.XPATH, "//*[contains(text(), 'Web Tables')]").click()
print("Web Tables List Selection Clicked")

# Map Table
# ---------------

table_length = driver.find_elements(By.XPATH,
                                    "//*[@class='rt-tr-group']/div[contains(@class,'rt-tr')]/div[contains(@class,'rt-td')]/div[@class='action-buttons']")
print("Number of Rows in table:")
print(len(table_length))
driver.find_element(By.XPATH, "//*[@id='addNewRecordButton']").click()

FirstName = 'Kevin'
LastName = 'Test'
Email = 'test123@test.com'
Age = '68'
Salary = '3800'
Department = 'That One'


txt_FirstName = driver.find_element(By.XPATH, "//*[@id='firstName']")
txt_LastName = driver.find_element(By.XPATH, "//*[@id='lastName']")
txt_Email = driver.find_element(By.XPATH, "//*[@id='userEmail']")
txt_Age = driver.find_element(By.XPATH, "//*[@id='age']")
txt_Salary = driver.find_element(By.XPATH, "//*[@id='salary']")
txt_Department = driver.find_element(By.XPATH, "//*[@id='department']")
# Begin inputting details for new record
txt_FirstName.send_keys(FirstName)
txt_LastName.send_keys(LastName)
txt_Email.send_keys(Email)
txt_Age.send_keys(Age)
txt_Salary.send_keys('enough')
txt_Department.send_keys(Department)
# Submit
driver.find_element(By.XPATH, '//*[@id="submit"]').click()
# Validate Error
time.sleep(2)

color = txt_Salary.value_of_css_property("border-color")

print(color)

if color != "rgb(220, 53, 69)":
    print("Validation Failed")
    sys.exit("Script Ended due incorrect error color code")

print("Error validation Successful")

txt_Salary.send_keys(Keys.CONTROL + 'a')
txt_Salary.send_keys(Salary)
driver.find_element(By.XPATH, "//*[@id='submit']").click()
time.sleep(2)

# Validate data entered correctly

driver.find_element(By.XPATH, "//*[@class='rt-tr-group']/div[contains(@class,'rt-tr')]/div[contains(@class,'rt-td') and text() = '" +FirstName+ "']")
driver.find_element(By.XPATH, "//*[@class='rt-tr-group']/div[contains(@class,'rt-tr')]/div[contains(@class,'rt-td') and text() = '" +LastName+ "']")
driver.find_element(By.XPATH, "//*[@class='rt-tr-group']/div[contains(@class,'rt-tr')]/div[contains(@class,'rt-td') and text() = '" +Email+ "']")
driver.find_element(By.XPATH, "//*[@class='rt-tr-group']/div[contains(@class,'rt-tr')]/div[contains(@class,'rt-td') and text() = '" +Age+ "']")
driver.find_element(By.XPATH, "//*[@class='rt-tr-group']/div[contains(@class,'rt-tr')]/div[contains(@class,'rt-td') and text() = '" +Salary+ "']")
driver.find_element(By.XPATH, "//*[@class='rt-tr-group']/div[contains(@class,'rt-tr')]/div[contains(@class,'rt-td') and text() = '" +Department+ "']")

newTable_length = driver.find_elements(By.XPATH,
                                    "//*[@class='rt-tr-group']/div[contains(@class,'rt-tr')]/div[contains(@class,'rt-td')]/div[@class='action-buttons']")

if len(newTable_length) == len(table_length):
    print("New Data wasn't added to the table successfully")
    sys.exit("Script failed due to table data not being added correctly")

print("New Number of Rows in table:")
print(len(newTable_length))

# Edit new data

driver.find_element(By.XPATH, "//DIV[@class='rt-td' and text() = '" +FirstName+ "']//following-sibling::DIV[@class ='rt-td']//*[@class='action-buttons']//*[contains(@id, 'edit-record') and @title='Edit']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='lastName']").send_keys(Keys.CONTROL + 'a')
driver.find_element(By.XPATH, "//*[@id='lastName']").send_keys('ChangeTest')
driver.find_element(By.XPATH, "//*[@id='submit']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@class='rt-tr-group']/div[contains(@class,'rt-tr')]/div[contains(@class,'rt-td') and text() = 'ChangeTest']")

# Delete new data

driver.find_element(By.XPATH, "//DIV[@class='rt-td' and text() = '" +FirstName+ "']//following-sibling::DIV[@class ='rt-td']//*[@class='action-buttons']//*[contains(@id, 'delete-record') and @title='Delete']").click()


newTable_length = driver.find_elements(By.XPATH,
                                    "//*[@class='rt-tr-group']/div[contains(@class,'rt-tr')]/div[contains(@class,'rt-td')]/div[@class='action-buttons']")

if len(newTable_length) == len(table_length):
    print("New data deleted successfully")
else:
    print("Delete was unsuccessful")
    sys.exit("Script closed due to data not being deleted from table")

    driver.close()