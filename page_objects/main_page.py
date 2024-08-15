from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage

class MainPage(BasePage):
    CART_BUTTON = By.CSS_SELECTOR, "#header-cart > div > button"
    SEARCH_INPUT = By.CSS_SELECTOR, "#search > input"
    SEARCH_BUTTON = By.CSS_SELECTOR, "#search > button"
    MAIN_ELEMENTS = By.CSS_SELECTOR, "#narbar-menu"
    SEARCH_ELEMENT = By.CSS_SELECTOR, "#product-search > ul > li:nth-child(2) > a"
    FEATURED_ONE = By.CSS_SELECTOR, "#content > div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4 > div:nth-child(1)"
    FEATURED_TWO = By.CSS_SELECTOR, "#content > div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4 > div:nth-child(2)"
    FEATURED_THREE = By.CSS_SELECTOR, "#content > div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4 > div:nth-child(3)"
    FEATURED_FOUR = By.CSS_SELECTOR, "#content > div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4 > div:nth-child(3)"
    FEATURED_PRODUCT_NAME = By.CSS_SELECTOR, "#content > div.row .product-thumb h4 a"


    def main_search(self, value):
        self.input_value(self.SEARCH_INPUT, value)
        self.click(self.SEARCH_BUTTON)
        self.get_element(self.SEARCH_ELEMENT)
        return self

    def wait_main_elements(self):
        self.get_element(self.CART_BUTTON)
        self.get_element(self.SEARCH_INPUT)
        self.get_element(self.SEARCH_BUTTON)
        self.get_element(self.MAIN_ELEMENTS)
        return self

    def wait_all_featured(self):
        self.get_element(self.FEATURED_ONE)
        self.get_element(self.FEATURED_TWO)
        self.get_element(self.FEATURED_THREE)
        self.get_element(self.FEATURED_FOUR)
        return self

    def get_featured_product_name(self, index=0):
        return self.get_elements(self.FEATURED_PRODUCT_NAME)[index].text

    def click_featured_product(self, index=0):
        if index == 0:
            self.click(self.FEATURED_PRODUCT_NAME)
        else:
            self.get_elements(self.FEATURED_PRODUCT_NAME)[index].click()

    def click_featured_product_2(self):
        self.get_element(self.FEATURED_ONE)
        self.click(self.FEATURED_ONE)
        return self


