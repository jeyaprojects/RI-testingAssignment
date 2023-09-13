import unittest
import time
import HtmlTestRunner
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import sys
sys.path.append("..//sepassignment")
from pageObject.loginPage import LoginPage
class LoginTest(unittest.TestCase):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    baseURL="https://facegenie-ams-school.web.app/"
    username="testbams@gmail.com"
    password="facegenie"


    @classmethod
    def setUpClass(cls) -> None:
        cls.driver.get(cls.baseURL)
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
    def test_Login(self):
        lp=LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(10)
        time.sleep(10)
        lp.clickLout()
        time.sleep(2)
if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='..\\sepassignment\\reports'))

"""
to run in terminal to get htnal report
python -m testCases.LoginTest
"""