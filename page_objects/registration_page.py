import allure
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage

class RegistrationPage(BasePage):
    FIRST_NAME_INPUT = By.CSS_SELECTOR, "#input-firstname"
    LAST_NAME_INPUT = By.CSS_SELECTOR, "#input-lastname"
    EMAIL_INPUT = By.CSS_SELECTOR, "#input-email"
    PASSWORD_INPUT = By.CSS_SELECTOR, "#input-password"
    CONTINUE_BUTTON = By.CSS_SELECTOR, "#form-register > div > button"
    PRIVACY_POLICY_SWITCHER = By.CSS_SELECTOR, "#form-register > div > div > input"
    ACCOUNT_HAS_BEEN_CREATED = By.CSS_SELECTOR, "#content > h1"

    @allure.step("Ожидаю все элементы на странице регистрации")
    def wait_registration_elements(self):
        self.get_element(self.FIRST_NAME_INPUT)
        self.get_element(self.LAST_NAME_INPUT)
        self.get_element(self.EMAIL_INPUT)
        self.get_element(self.PASSWORD_INPUT)
        self.get_element(self.CONTINUE_BUTTON)
        self.get_element(self.PRIVACY_POLICY_SWITCHER)
        return self


    @allure.step("Выполняю регистрацию нового клиента")
    def registration(self, firstname, lastname, email, password):
        self.logger.info("Registered user with FIRST NAME: %s, LAST NAME: %s, EMAIL: %s, PASSWORD: %s" %
                         (firstname, lastname, email, password))
        self.input_value(self.FIRST_NAME_INPUT, firstname)
        self.input_value(self.LAST_NAME_INPUT, lastname)
        self.input_value(self.EMAIL_INPUT, email)
        self.input_value(self.PASSWORD_INPUT, password)
        self.click(self.PRIVACY_POLICY_SWITCHER)
        self.click(self.CONTINUE_BUTTON)
        self.get_element(self.ACCOUNT_HAS_BEEN_CREATED)
        return self

