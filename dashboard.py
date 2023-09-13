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
#going through all the top menus
#dsahboard
driver.find_element(By.XPATH,"//span[normalize-space()='Dashboard']").click()
time.sleep(3)
#attendance log
driver.find_element(By.XPATH,"//span[normalize-space()='Attendance Logs']").click()
time.sleep(2)
#Analytics and Report
driver.find_element(By.XPATH,"//span[normalize-space()='Analytics and Reports']").click()
time.sleep(2)
#manage student
driver.find_element(By.XPATH,"//span[normalize-space()='Manage Student']").click()
time.sleep(2)
#manage licence
driver.find_element(By.XPATH,"//span[normalize-space()='Manage Licenses']").click()
time.sleep(2)
#settings
driver.find_element(By.XPATH,"//span[normalize-space()='Setting']").click()
time.sleep(2)
print("FInished")
driver.close()
driver.quit()