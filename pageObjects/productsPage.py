from pageObjects.basePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ProductsPage(BasePage):
    def select_3_products(self):
       men_section_btn = self.driver.find_element(By.CSS_SELECTOR,"div.header a[href='/men']")
       men_section_btn.click()
       time.sleep(2)
       # first product
       products_list_txt = self.driver.find_elements(By.CSS_SELECTOR,"div.listing-tem").__getitem__(0)
       products_list_txt.click()
       time.sleep(2)
       small_size_btn = self.driver.find_element(By.XPATH,"//a[contains(text(), 'X')]")
       small_size_btn.click()
       time.sleep(2)
       pink_color_btn = self.driver.find_element(By.XPATH,"//a[contains(text(), 'Green')]")
       pink_color_btn.click()
       time.sleep(2)            
       add_to_car_btn = self.driver.find_element(By.XPATH,"//span[contains(text(), 'ADD TO CART')]")
       add_to_car_btn.click()
       # back to category products
       men_section_btn = self.driver.find_element(By.CSS_SELECTOR,"div.header a[href='/men']")
       men_section_btn.click()
       # second product
       products_list_txt = self.driver.find_elements(By.CSS_SELECTOR,"div.listing-tem").__getitem__(1)
       products_list_txt.click()
       quantity_txt = self.driver.find_element(By.CSS_SELECTOR,"input[name='qty']")
       quantity_txt.clear()
       quantity_txt.send_keys("2")
       time.sleep(2)
       small_size_btn = self.driver.find_element(By.XPATH,"//a[contains(text(), 'S')]")
       small_size_btn.click()
       time.sleep(2)
       pink_color_btn = self.driver.find_element(By.XPATH,"//a[contains(text(), 'Black')]")
       pink_color_btn.click()
       time.sleep(2) 
       # Espera explícita de hasta 10 segundos para que el botón de la sección de hombres esté presente            
       add_to_car_btn = self.driver.find_element(By.XPATH,"//span[contains(text(), 'ADD TO CART')]")
       add_to_car_btn.click()
       # back to category products
       men_section_btn = self.driver.find_element(By.CSS_SELECTOR,"div.header a[href='/men']")
       men_section_btn.click()
       # third product
       products_list_txt = self.driver.find_elements(By.CSS_SELECTOR,"div.listing-tem").__getitem__(2)
       products_list_txt.click()
       quantity_txt = self.driver.find_element(By.CSS_SELECTOR,"input[name='qty']")
       quantity_txt.clear()
       quantity_txt.send_keys("3")
       time.sleep(2)
       small_size_btn = self.driver.find_element(By.XPATH,"//a[contains(text(), 'L')]")
       small_size_btn.click()
       time.sleep(2)
       pink_color_btn = self.driver.find_element(By.XPATH,"//a[contains(text(), 'Purple')]")
       pink_color_btn.click()
       time.sleep(2) 
       # Espera explícita de hasta 10 segundos para que el botón de la sección de hombres esté presente            
       add_to_car_btn = self.driver.find_element(By.XPATH,"//span[contains(text(), 'ADD TO CART')]")
       add_to_car_btn.click()
       # back to category products
       men_section_btn = self.driver.find_element(By.CSS_SELECTOR,"div.header a[href='/men']")
       men_section_btn.click()