from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome(executable_path="D:\\chromedriver_win32\\chromedriver.exe")

driver.get("https://www.rahulshettyacademy.com/angularpractice/")

driver.maximize_window()

drop_down = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))

# there ways to select
drop_down.select_by_value("Male")
drop_down.select_by_index(1)
drop_down.select_by_value("student")
# dropdown.select_by_visible_text ()

driver.quit()
