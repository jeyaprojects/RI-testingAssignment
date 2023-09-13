from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
"""
login and logout
"""

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://facegenie-ams-school.web.app/")#launching the brower
driver.maximize_window()
#time.sleep(3)
print(driver.current_url)
#entering email address and password
driver.find_element(By.XPATH,"//input[@id='email']").send_keys("testbams@gmail.com")
#time.sleep(3)
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("facegenie")
#time.sleep(3)
driver.find_element(By.XPATH,"//button[normalize-space()='Log In']").click()
time.sleep(10)
time.sleep(10)
print(driver.current_url)
#logout
print("Logout")
driver.find_element(By.XPATH,"//span[normalize-space()='Log Out']").click()
driver.find_element(By.XPATH,"//button[normalize-space()='Ok']").click()
driver.close()
driver.quit()
