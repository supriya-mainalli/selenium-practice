from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome(executable_path="D:\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com/angularpractice/")

driver.maximize_window()

#TD, xpath, CSS, name, LinkText, class name
driver.find_element(By.NAME, 'name').send_keys('supriya')

driver.find_element(By.NAME,'email').send_keys('abc@gmail.com')

driver.find_element(By.ID, 'exampleInputPassword1').send_keys('1234')

checkbox = driver.find_element(By.ID, 'exampleCheck1')
checkbox.click()

# if not checkbox.is_selected():
#     print("The checkbox is not selected")
#     assert False
#
# print("The checkbox is selected")

driver.find_element(By.XPATH,"//input[@type='submit']").click()

driver.close()