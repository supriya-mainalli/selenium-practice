import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
time.sleep(2)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME, 'name').send_keys('Supriya')
time.sleep(2)

driver.close()