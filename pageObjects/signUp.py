from pageObjects.basePage import BasePage
from selenium.webdriver.common.by import By
from models.accountManager import AccountManager
import time

class SignUp(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.accountManager = AccountManager()

    def create_new_account(self):
        full_name, email, password = self.accountManager.get_account_details()
        create_account_btn = self.driver.find_element(By.CSS_SELECTOR,"a[href='/account/register']")
        create_account_btn.click()
        full_name_txt = self.driver.find_element(By.CSS_SELECTOR,"input[name='full_name']")
        full_name_txt.send_keys(full_name)
        email_txt = self.driver.find_element(By.CSS_SELECTOR,"input[name='email']")
        email_txt.send_keys(email)
        password_txt = self.driver.find_element(By.CSS_SELECTOR,"input[name='password']")
        password_txt.send_keys(password)
        register_account_btn = self.driver.find_element(By.CSS_SELECTOR,"button[type='submit']")
        register_account_btn.click()
        time.sleep(3)