from pageObjects.basePage import BasePage
from pageObjects.homePage import HomePage
from pageObjects.loginPage import LoginPage
from pageObjects.signUp import SignUp
from pageObjects.productsPage import ProductsPage
from pageObjects.cartPage import CartPage
from pageObjects.checkoutPage import CheckoutPage

def teste_suite():
    try: 
        basePage = BasePage()
        homePage = HomePage(driver=basePage.driver)
        loginPage = LoginPage(driver=basePage.driver)
        signUp = SignUp(driver=basePage.driver)
        homePage.open_home_page()
        loginPage.click_login()
        signUp.create_new_account()
        loginPage.logout_new_account_recently_created()
        loginPage.click_login()
        account_details = signUp.accountManager.get_account_details()
        name, email, password = account_details[0], account_details[1], account_details[2]
        loginPage.login_new_account(email,password)
        productsPage = ProductsPage(driver=basePage.driver)
        productsPage.select_3_products()
        cartPage = CartPage(driver=basePage.driver)
        cartPage.checkout_cart()
        cartPage.pay_product()
        checkoutPage = CheckoutPage(driver=basePage.driver)
        checkoutPage.verify_detail_bill(name,email)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        basePage.quit()

if __name__ == "__main__":
    teste_suite()