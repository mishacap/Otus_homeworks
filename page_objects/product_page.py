from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage

class ProductPage(BasePage):
    PRODUCT_NAME = By.CSS_SELECTOR, "#content > div.row.mb-3 > div:nth-child(2) > h1"
    ADD_TO_CART = By.CSS_SELECTOR, "#button-cart"
    ADD_TO_WISH_LIST = By.CSS_SELECTOR, "#content > div.row.mb-3 > div:nth-child(2) > form > div > button:nth-child(1)"
    ADD_TO_COMPARE = By.CSS_SELECTOR, "#content > div.row.mb-3 > div:nth-child(2) > form > div > button:nth-child(2)"
    QTY_INPUT = By.CSS_SELECTOR, "#input-quantity"

    def wait_product_elements(self):
        self.get_element(self.PRODUCT_NAME)
        self.get_element(self.ADD_TO_CART)
        self.get_element(self.QTY_INPUT)
        return self


