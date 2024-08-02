from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

def verify_connection():
    try:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://demo.evershop.io/")
        driver.implicitly_wait(10)
        login_link = driver.find_element(By.CSS_SELECTOR, "a[href='/account/login']")
        login_link.click()
        create_account = driver.find_element(By.CSS_SELECTOR,"a[href='/account/register']")
        create_account.click()       


    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    verify_connection()
