from pageObjects.basePage import BasePage
from selenium.webdriver.common.by import By
import time

class LoginPage(BasePage):
    def click_login(self):
        login_btn = self.driver.find_element(By.CSS_SELECTOR, "a[href='/account/login']")
        login_btn.click()

    def login_new_account(self, email, password):
        user_txt = self.driver.find_element(By.CSS_SELECTOR,"input[type='text']")
        user_txt.send_keys(email)
        psw_text = self.driver.find_element(By.CSS_SELECTOR,"input[type='password']")
        psw_text.send_keys(password)
        signIn_btn = self.driver.find_element(By.CSS_SELECTOR,"button[type='submit']")
        signIn_btn.click()
        time.sleep(5)

    def logout_new_account_recently_created(self):
        login_btn = self.driver.find_element(By.CSS_SELECTOR, "a[href='/account']")
        login_btn.click()
        logout_btn = self.driver.find_element(By.XPATH,"//a[contains(text(), 'Logout')]")
        logout_btn.click()
        time.sleep(2)