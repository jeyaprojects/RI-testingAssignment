'''
Here we use PageObjectModel(POM) and generate HTML reports using UnitTest Framework for Homepage Loging


'''

from selenium.webdriver.common.by import By
class LoginPage():
    #locators for all wb element
    textbox_email_xpath = "//input[@id='email']"
    textbox_password_xpath = "//input[@id='password']"
    button_login_xpath = "//button[normalize-space()='Log In']"
    alert_box_invalid_username="//div[@class='MuiAlert-message css-1xsto0d']"
    alert_box_invalid_passwprd="//div[@class='MuiAlert-message css-1xsto0d']"
    button_logout_xpath = "//span[normalize-space()='Log Out']"
    button_logout_confirm_xpath="//button[normalize-space()='Ok']"

    # create contructor and initate the driver
    def __init__(self,driver):
        self.driver=driver
    #create action method for each element
    def setUserName(self, username):
        self.driver.find_element(By.XPATH,self.textbox_email_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_email_xpath).send_keys(username)
    def setPassword(self,password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)
    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()
    def check_invalid_username(self):
        msg=self.driver.find_element(By.XPATH,self.alert_box_invalid_username).text
        return msg
    def check_invalid_password(self):
        msg=self.driver.find_element(By.XPATH,self.alert_box_invalid_passwprd).text
        return msg

    def clickLout(self):
        self.driver.find_element(By.XPATH, self.button_logout_xpath).click()
        self.driver.find_element(By.XPATH, self.button_logout_confirm_xpath).click()
