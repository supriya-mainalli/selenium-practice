import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# from selenium.webdriver.common.By import By

driver = webdriver.Chrome()
driver.get("https://testanild42testt111.freshcmdb.com/support/login")
driver.maximize_window()
print(f"The title of the page is : {driver.title}")
print(f"The currentl url is: {driver.current_url}")
time.sleep(7)
driver.find_element(By.ID, 'username').send_keys('sandboxaccountd4223@yopmail.com')
driver.find_element(By.NAME, 'password').send_keys('test1234')
driver.find_element(By.XPATH, "//button[@data-testid='login-button']").click()
time.sleep(5)
