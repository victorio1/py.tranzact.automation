from pageObjects.basePage import BasePage
from selenium.webdriver.common.by import By
import time

class CheckoutPage(BasePage):
    def verify_detail_bill(self,name,email):
        # verify username & email
        name_txt = self.driver.find_elements(By.CSS_SELECTOR,"div.mb-2 div.text-textSubdued")
        email_txt = self.driver.find_elements(By.CSS_SELECTOR,"div.mb-2 div.text-textSubdued")
        
        assert name in name_txt[0].text, f"expected name is not contains '{name}'. current text: {name_txt[0].text} '"
        assert email in email_txt[1].text, f"expected name is not contains '{name}'. current text: {email_txt[1].text} '"

        # verify payment method
        paymentMethod_txt = self.driver.find_elements(By.CSS_SELECTOR,"div.mb-2 div.text-textSubdued")
        expectedPayMentMethod = "Credit Card"
        assert expectedPayMentMethod in paymentMethod_txt[3].text, f"expected text is not contains '{expectedPayMentMethod}'. current text: '{paymentMethod_txt[3].text}'" 
        
        # verify shipping_address details
        name_shipping_address = self.driver.find_elements(By.CSS_SELECTOR,"div.address__summary div.full-name")
        street_shipping_address = self.driver.find_elements(By.CSS_SELECTOR,"div.address__summary div.address-one")        
        city_province_postcode_shipping_address = self.driver.find_elements(By.CSS_SELECTOR,"div.address__summary div.city-province-postcode")
        telephone_shipping_address = self.driver.find_elements(By.CSS_SELECTOR,"div.address__summary div.telephone")
        
        expected_name_s = "Eduardo Victorio"
        street_s = "Street Kennedy 124"
        country_s = "00038, San Diego California, United States"
        phone_s = "933424954"
        assert expected_name_s in name_shipping_address[1].text, f"expected text is not contains '{expected_name_s}'. current text: '{name_shipping_address[1].text}'" 
        assert street_s in street_shipping_address[1].text, f"expected text is not contains '{street_s}'. current text: '{street_shipping_address[1].text}'" 
        actual_country_s = city_province_postcode_shipping_address[1].text
        actual_countr_s_normalized = actual_country_s.replace("\n"," ")
        assert country_s in actual_countr_s_normalized, f"expected text is not contains '{country_s}'. current text: '{actual_countr_s_normalized}'" 
        assert phone_s in telephone_shipping_address[1].text, f"expected text is not contains '{phone_s}'. current text: '{telephone_shipping_address[1].text}'" 
        
        # verify billing_address details
        name_billing_address = self.driver.find_elements(By.CSS_SELECTOR,"div.address__summary div.full-name")
        street_billing_address  = self.driver.find_elements(By.CSS_SELECTOR,"div.address__summary div.address-one")
        city_province_postcode_billing_address  = self.driver.find_elements(By.CSS_SELECTOR,"div.address__summary div.city-province-postcode")
        telephone_billing_address  = self.driver.find_elements(By.CSS_SELECTOR,"div.address__summary div.telephone")
        
        expected_name_b = "Eduardo Victorio"
        street_b = "Street Kennedy 124"
        country_b = "00038, San Diego California, United States"
        phone_b = "933424954"
        assert expected_name_b in name_billing_address[1].text, f"expected text is not contains '{expected_name_b}'. current text: '{name_billing_address[1].text}'" 
        assert street_b in street_billing_address[1].text, f"expected text is not contains '{street_b}'. current text: '{street_billing_address[1].text}'" 
        actual_country_b = city_province_postcode_billing_address[1].text
        actual_country_b_normalized = actual_country_b.replace("\n", " ")
        assert country_b in actual_country_b_normalized, f"expected text is not contains '{country_b}'. current text: '{actual_country_b_normalized}'" 
        assert phone_b in telephone_billing_address[1].text, f"expected text is not contains '{phone_b}'. current text: '{telephone_billing_address[1].text}'" 
        
        # verify price details
        # verify contains with $
        listPrice_products = self.driver.find_elements(By.XPATH,"//span[contains(text(), '$')]")
        actualListPrice = [element.text for element in listPrice_products]
        expectedPrices = ["$1,791.90","$1,579.60","$789.80"]
        actual_prices_sorted = sorted(actualListPrice)
        expected_prices_sorted = sorted(expectedPrices)
        assert actual_prices_sorted == expected_prices_sorted, (
           f" the list price expected was {expected_prices_sorted},"
           f" we got this prices {actual_prices_sorted}"     
        )
        # verify contains
        listPrice_products = self.driver.find_elements(By.XPATH, "//span[contains(text(), '$')]")
        actualListPrice = [element.text for element in listPrice_products]
        expectedPrices = ["1,791.90", "1,579.60", "789.80"]
        for expected_price in expectedPrices:
            match_found = any(expected_price in actual_price for actual_price in actualListPrice)
            assert match_found, f"Price expected '{expected_price}' it was not found in the current price: {actualListPrice}"

        finalPrice_product = self.driver.find_elements(By.XPATH,"//div[contains(text(), '$')]")
        expectedTotalPrice = "4,166.30"
        assert expectedTotalPrice in finalPrice_product[3].text, f"expected price is not contains '{expectedTotalPrice}'. current text: '{finalPrice_product[3].text}'" 
        time.sleep(2)

