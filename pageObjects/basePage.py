from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class BasePage:
    def __init__(self, driver=None):
        if driver is None:
            chrome_options = Options()
            chrome_options.add_argument("start-maximized")
            chrome_options.add_argument("test-type")
            chrome_options.add_argument("disable-notifications")
            
            # Configuraciones para deshabilitar el autocompletado
            prefs = {
                "profile.default_content_setting_values.notifications": 2,
                "profile.default_content_setting_values.popups": 0,
                "profile.password_manager_enabled": False,
                "credentials_enable_service": False,
                "autofill.profile_enabled": False,
                "autofill.credit_card_enabled": False,
                "autofill.enabled": False
            }
            chrome_options.add_experimental_option("prefs", prefs)
            
            self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
            self.driver.implicitly_wait(5)
        else:
            self.driver = driver

    def quit(self):
        self.driver.quit()
