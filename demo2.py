from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://testanild42testt111.freshcmdb.com/support/login")
time.sleep(5)
driver.find_element(By.LINK_TEXT, 'Forgot Password?').click()
# driver.find_element(By.XPATH, "//form/div[1]/input[@id='email']").send_keys('test12')
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(1) input[id='email']").send_keys('sandboxaccountd4223@yopmail.com')
driver.find_element(By.XPATH, "//button[text()='Request reset link']").click()
driver.close()