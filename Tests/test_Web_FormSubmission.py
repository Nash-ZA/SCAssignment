from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import sys



s = Service(r'C:\Drivers\ChromeDriver\chromedriver.exe')
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

driver.maximize_window()

time.sleep(1)

# Click on Forms Card
driver.find_element(By.XPATH, "//*[@class='card-body']//H5[text() = 'Forms']").click()
print("Forms Display Card Clicked")

# Click on Practice Form List Selection
driver.find_element(By.XPATH, "//*[contains(text(), 'Practice Form')]").click()
print("Practice Form List Selection Clicked")

gender = 'Other'
hobby = 'Reading'

# Map Form fields
# ---------------
txt_FirstName = driver.find_element(By.XPATH, "//*[@id='firstName']")
txt_LastName = driver.find_element(By.XPATH, "//*[@id='lastName']")
txt_Email = driver.find_element(By.XPATH, "//*[@id='userEmail']")
rdb_GenderMale = driver.find_element(By.XPATH,
                                     "//*[contains(@class, 'custom-control custom-radio') and input[@value='"+gender+"']]")
txt_Phone = driver.find_element(By.XPATH, "//*[@id='userNumber']")
DateSelect = driver.find_element(By.XPATH, "//*[@id='dateOfBirthInput']")
cmb_Subject = driver.find_element(By.XPATH, "//*[@id='subjectsInput']")
# chk_Hobbies = driver.find_element(By.XPATH, "//*[contains(@for, 'hobbies-checkbox') and /*[text() = '"+hobby+"']]")
chk_Hobbies = driver.find_element(By.XPATH, "//*[text() = '"+hobby+"']//ancestor::*[contains(@for, 'hobbies-checkbox')]")
btn_ChooseFile = driver.find_element(By.XPATH, "//*[@id='uploadPicture']")
txt_CurrentAddress = driver.find_element(By.XPATH, "//*[@id='currentAddress']")
cmb_State = driver.find_element(By.XPATH, "//*[contains(@id, 'react-select-3') and @type='text']")
cmb_City = driver.find_element(By.XPATH, "//*[contains(@id, 'react-select-4') and @type='text']")
btn_Submit = driver.find_element(By.XPATH, "//*[@id='submit' and @type='submit']")



# Start Form Field Actions
# ------------------------
txt_FirstName.send_keys('Kevin')  # input First Name
txt_LastName.send_keys('Naude')  # input Last Name
txt_Email.send_keys('knaude130@gmail.com')  # input Email
# Select Gender
rdb_GenderMale.click()
txt_Phone.send_keys('0736694435')  # Input Phone Number
# Select Date
DateSelect.send_keys(Keys.CONTROL + 'a')
DateSelect.send_keys('22 Dec 1993')
DateSelect.send_keys(Keys.ENTER)
cmb_Subject.send_keys('Computer Science')
cmb_Subject.send_keys(Keys.ARROW_DOWN)
cmb_Subject.send_keys(Keys.TAB)
time.sleep(3)
chk_Hobbies.click()
chk_Hobbies.get_attribute('checked')
print("Hobby Checkbox selected and validated successfully")
btn_ChooseFile.send_keys(img_path)
print("Image Uploaded successfully")
txt_CurrentAddress.send_keys('123 Test Street,' +Keys.ENTER+ 'Test Town,' +Keys.ENTER+ 'Amstertest,' +Keys.ENTER+ '669855')
cmb_State.send_keys('NCR')
cmb_State.send_keys(Keys.TAB)
cmb_City.send_keys('Noida')
cmb_City.send_keys(Keys.TAB)
btn_Submit.click()
print("Form Submitted Successfully")

time.sleep(3)
btn_Close = driver.find_element(By.XPATH, "//*[@id='closeLargeModal' and @type='button']")
btn_Close.click()


driver.close()
