import time

import allure
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class AdministrationPage(BasePage):
    USER_NAME = By.CSS_SELECTOR, "#input-username"
    PASSWORD = By.CSS_SELECTOR, "#input-password"
    LOGIN_BUTTON = By.CSS_SELECTOR, "#form-login > div.text-end > button"
    LOGOUT_BUTTON = By.CSS_SELECTOR, "#nav-logout > a"

    CATALOG = By.CSS_SELECTOR, "#menu-catalog > a"
    PRODUCT = By.XPATH, '//*[@id="collapse-1"]/li[2]/a'

    ADD_BUTTON = By.CSS_SELECTOR, "#content > div.page-header > div > div > a"
    PDODUCT_NAME_INPUT = By.CSS_SELECTOR, "#input-name-1"
    META_TAG_TITLE = By.CSS_SELECTOR, "#input-meta-title-1"
    PRODUCT_DATA = By.CSS_SELECTOR, "#form-product > ul > li:nth-child(2) > a"
    PRODUCT_MODEL_INPUT = By.CSS_SELECTOR, "#input-model"
    PRODUCT_CEO = By.CSS_SELECTOR, "#form-product > ul > li:nth-child(11) > a"
    PRODUCT_CEO_INPUT = By.CSS_SELECTOR, "#input-keyword-0-1"
    PRODUCT_SAFE_BOTTON = By.CSS_SELECTOR, "#content > div.page-header > div > div > button"
    ALERT = By.CSS_SELECTOR, "#alert > div"
    BACK_BUTTON = By.CSS_SELECTOR, "#content > div.page-header > div > div > a"

    FILTER_INPUT = By.CSS_SELECTOR, "#input-name"
    FILTER_BUTTON = By.CSS_SELECTOR, "#button-filter"
    DATA_ELEMENT = By.CSS_SELECTOR, "#form-product > div.table-responsive > table > tbody > tr > td:nth-child(3)"

    PRODUCT_CECKBOX_FIRST = By.CSS_SELECTOR, "#form-product > div.table-responsive > table > tbody > tr:nth-child(1) > td:nth-child(1) > input"
    PRODUCT_COPY_BUTTON = By.CSS_SELECTOR, "#content > div.page-header > div > div > button:nth-child(3)"
    PRODUCT_CHECKBOX_SECOND = By.CSS_SELECTOR, "#form-product > div.table-responsive > table > tbody > tr:nth-child(2) > td:nth-child(1) > input"
    PRODUCT_DELETE_BOTTON = By.CSS_SELECTOR, "#content > div.page-header > div > div > button.btn.btn-danger"
    PRODUCT_STATUS = By.CSS_SELECTOR, "#form-product > div.table-responsive > table > tbody > tr:nth-child(2) > td:nth-child(3) > small"

    @allure.step("Выполняю вход в админку под кредами: {username}, {password}")
    def login(self, username, password):
        self.input_value(self.USER_NAME, username)
        self.input_value(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)
        return self

    def wait_logged_in(self):
        self.get_element(self.LOGOUT_BUTTON)
        return self

    @allure.step("Выполяю выход из админки")
    def logout(self):
        self.get_element(self.LOGOUT_BUTTON)
        self.click(self.LOGOUT_BUTTON)
        return self

    @allure.step("Открываю каталог")
    def open_catalog(self):
        self.get_element(self.CATALOG)
        self.click(self.CATALOG)
        self.get_element(self.PRODUCT)
        self.click(self.PRODUCT)
        return self

    @allure.step("Добавляю новый подукт: {product_name}, с тегом: {meta_tag_title}")
    def add_new_product(self, product_name, meta_tag_title):
        self.logger.info("Add new PRODUCT with NAME: %s, META TAG: %s" % (product_name, meta_tag_title))
        self.get_element(self.ADD_BUTTON)
        self.click(self.ADD_BUTTON)
        self.input_value(self.PDODUCT_NAME_INPUT, product_name)
        self.input_value(self.META_TAG_TITLE, meta_tag_title)
        self.click(self.PRODUCT_DATA)
        self.input_value(self.PRODUCT_MODEL_INPUT, product_name)
        self.click(self.PRODUCT_CEO)
        self.input_value(self.PRODUCT_CEO_INPUT, meta_tag_title)
        self.click(self.PRODUCT_SAFE_BOTTON)
        return self

    def wait_alert_and_back(self):
        self.get_element(self.ALERT)
        self.click(self.BACK_BUTTON)
        return self

    @allure.step("Ищу новый продукт: {name}")
    def find_new_product(self, name):
        self.logger.info("Execute SEARCH of %s", name)
        self.input_value(self.FILTER_INPUT, name)
        self.click(self.FILTER_BUTTON)
        return self

    def wait_filter_data(self):
        data_element = self.get_element(self.DATA_ELEMENT)
        return self

    @allure.step("Копирую продукт")
    def copy_product(self):
        self.get_element(self.PRODUCT_CECKBOX_FIRST)
        self.click(self.PRODUCT_CECKBOX_FIRST)
        self.get_element(self.PRODUCT_COPY_BUTTON)
        self.click(self.PRODUCT_COPY_BUTTON)
        return self

    @allure.step("Удаляю продукт")
    def delete_product(self):
        self.get_element(self.PRODUCT_CHECKBOX_SECOND)
        self.click(self.PRODUCT_CHECKBOX_SECOND)
        self.get_element(self.PRODUCT_DELETE_BOTTON)
        self.click(self.PRODUCT_DELETE_BOTTON)
        return self

    @allure.step("Проверяю статус")
    def cheсk_status(self):
        product_status = self.get_element(self.PRODUCT_STATUS)
        return product_status.text
