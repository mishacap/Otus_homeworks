from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class AdministrationPage(BasePage):
    USER_NAME = By.CSS_SELECTOR, "#input-username"
    PASSWORD = By.CSS_SELECTOR, "#input-password"
    LOGIN_BUTTON = By.CSS_SELECTOR, "#form-login > div.text-end > button"
    LOGOUT_BUTTON = By.CSS_SELECTOR, "#nav-logout > a"

    def login(self, username, password):
        self.input_value(self.USER_NAME, username)
        self.input_value(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)
        return self

    def wait_logged_in(self):
        self.get_element(self.LOGOUT_BUTTON)
        return self
