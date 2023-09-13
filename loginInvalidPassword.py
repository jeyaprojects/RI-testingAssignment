from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://facegenie-ams-school.web.app/")#launching the brower
driver.maximize_window()
time.sleep(3)
#entering email address and password
driver.find_element(By.XPATH,"//input[@id='email']").send_keys("testbams@gmail.com")
time.sleep(3)
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("facegenie1")
time.sleep(3)
driver.find_element(By.XPATH,"//button[normalize-space()='Log In']").click()
time.sleep(2)
msg=driver.find_element(By.XPATH,"//div[@class='MuiAlert-message css-1xsto0d']").text
print(msg)
print("Test Completed")
driver.close()
driver.quit()
