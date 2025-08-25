from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path='/Users/macsho/Programming/Python/Python_Selenium/WebDriver/Chrome/chromedriver')
driver = webdriver.Chrome(service=service)

# Open a website
driver.get("https://login.netsuite.com")
time.sleep(5)

# Find the search box element by its class name
input_element = driver.find_element(By.ID, "ui-id-1|input")                                     # Find the search box element
input_element.send_keys("your_account_id_varonis")                                              # Add you account id
time.sleep(5)

#Click the continue button
input_element = driver.find_element(By.XPATH, "//span[contains(text(),'Continue')]").click()   # Find the search box element
time.sleep(5)


# Login
driver.find_element(By.ID, "email").send_keys("your_email")                                     # Add you value of email
driver.find_element(By.ID, "password").send_keys("your_password")                               # Add the sales operation team member password
driver.find_element(By.ID, "login_button").click()

# Navigate to Credit Memo creation
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "create_credit_memo")))  # Wait for the create_credit_memo button to be present
driver.find_element(By.ID, "create_credit_memo").click()                                        # Click the create_credit_memo button

# Fill required fields
driver.find_element(By.ID, "credited_or_number").send_keys("OR-123456")                         # Add the credited order number

# Submit form
driver.find_element(By.ID, "submit_button").click()                                             # Click the submit button

# Assert state
state = driver.find_element(By.ID, "credit_approval_state").text                                # Get the credit approval state text
assert state == "TL Credit Review", "Credit memo did not enter expected state"                  # Assert the expected state when the Sales ops member is getting a message that a review message is required from TL

driver.quit()
