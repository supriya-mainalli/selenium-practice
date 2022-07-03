from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:\\chromedriver_win32\\chromedriver.exe")

driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

print(driver.find_element(By.XPATH, "//div[@id='radio-btn-example']/fieldset/legend").text)

radio_buttons = driver.find_elements(By.XPATH, "//input[@name='radioButton']")

for radio_button in radio_buttons:
    radio_button.click()
    print(radio_button.is_enabled())

driver.close()