from pageObjects.basePage import BasePage
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert

class CartPage(BasePage):
    def checkout_cart(self):
        cart_btn = self.driver.find_element(By.CSS_SELECTOR,"a[href='/cart']")
        cart_btn.click()
        time.sleep(5)        
        checkout_btn = self.driver.find_element(By.CSS_SELECTOR,"a[href='/checkout']")
        checkout_btn.click()
        fullName_txt = self.driver.find_element(By.CSS_SELECTOR,"input[name='address[full_name]']")
        fullName_txt.send_keys("Eduardo Victorio")
        telephone_txt = self.driver.find_element(By.CSS_SELECTOR,"input[name='address[telephone]']")
        telephone_txt.send_keys("933424954")
        address_txt = self.driver.find_element(By.CSS_SELECTOR,"input[name='address[address_1]']")
        address_txt.send_keys("Street Kennedy 124")
        city_txt = self.driver.find_element(By.CSS_SELECTOR,"input[name='address[city]']")
        city_txt.send_keys("San Diego")
        country_select_first = Select(self.driver.find_element(By.ID,"address[country]"))
        country_select_first.select_by_visible_text("United States")
        province_select = Select(self.driver.find_element(By.ID,"address[province]"))
        province_select.select_by_visible_text("California")
        zipCode_txt = self.driver.find_element(By.CSS_SELECTOR,"input[name='address[postcode]']")
        zipCode_txt.send_keys("00038")
        time.sleep(3)
        paymentMode_rdo = self.driver.find_elements(By.CSS_SELECTOR,"span.radio-unchecked").__getitem__(0)
        paymentMode_rdo.click()
        continuePayment = self.driver.find_element(By.XPATH,"//span[contains(text(), 'Continue to payment')]")
        continuePayment.click()
        time.sleep(2)
        

    def pay_product(self):
        checkout_form = self.driver.find_element(By.CSS_SELECTOR,"form#checkoutPaymentForm")
        visaMode_rdo = checkout_form.find_element(By.CSS_SELECTOR,"svg[class='feather feather-circle']")
        visaMode_rdo.click()
        iframe = self.driver.find_element(By.CSS_SELECTOR, "iframe[allow='payment *']")
        self.driver.switch_to.frame(iframe)
        cardNumber_txt = self.driver.find_elements(By.CSS_SELECTOR,"input.InputElement.is-empty.Input.Input--empty").__getitem__(0)
        cardNumber_txt.send_keys("4242 4242 4242 4242 0932")
        cvv_txt = self.driver.find_element(By.CSS_SELECTOR,"input[aria-label='Credit or debit card CVC/CVV']")
        cvv_txt.send_keys("777")
        self.driver.switch_to.default_content()
        placeOrder_btn = checkout_form.find_element(By.XPATH,"//span[contains(text(), 'Place Order')]")
        placeOrder_btn.click()