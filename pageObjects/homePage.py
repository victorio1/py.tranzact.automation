from pageObjects.basePage import BasePage

class HomePage(BasePage):
    def open_home_page(self):
        self.driver.get("https://demo.evershop.io/")
        self.driver.maximize_window()