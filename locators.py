from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\chromedriver_win32\\chromedriver.exe")

driver.get("https://www.rahulshettyacademy.com/angularpractice/")

driver.maximize_window()

driver.find_element_by_name("name").send_keys("Supriya")

driver.find_element_by_name("email").send_keys("abc@gmail.com")

driver.find_element_by_id("exampleInputPassword1").send_keys("1234")

checkbox = driver.find_element_by_id("exampleCheck1")
checkbox.click()

if not checkbox.is_selected():
    print("The checkbox is not selected")
    assert False

print("The checkbox is selected")

driver.find_element_by_xpath("//input[@type='submit']").click()

driver.close()
