import time

from selenium.webdriver.common.by import By
from conftest import browser, base_url
from faker import Faker

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from page_objects.administration_login_page import AdministrationPage
from page_objects.main_page import MainPage
from page_objects.product_page import ProductPage
from page_objects.registration_page import RegistrationPage
from helpers import get_fake_product, get_random_index, get_user_data


def test_administration_login(browser, base_url):
    browser.get(f"{base_url}:8081/administration/")
    admin_page = AdministrationPage(browser)
    admin_page.login(username="user", password="bitnami")
    admin_page.wait_logged_in()

def test_main_elements(browser, base_url):
    browser.get(f"{base_url}:8081/")
    main_page = MainPage(browser)
    main_page.wait_main_elements()

def test_main_searh(browser, base_url):
    browser.get(f"{base_url}:8081/")
    main_page = MainPage(browser)
    main_page.main_search(get_fake_product())

def test_featured_elements(browser, base_url):
    browser.get(f"{base_url}:8081/")
    main_page = MainPage(browser)
    main_page.wait_all_featured()

def test_featured_click(browser, base_url):
    browser.get(f"{base_url}:8081/")
    main_page = MainPage(browser)
    main_page.click_featured_product(3)
    product_page = ProductPage(browser)
    product_page.wait_product_elements()

def test_registration_elements(browser, base_url):
    browser.get(f"{base_url}:8081/index.php?route=account/register")
    registration_page = RegistrationPage(browser)
    registration_page.wait_registration_elements()

def test_registarion_new_user(browser, base_url):
    browser.get(f"{base_url}:8081/index.php?route=account/register")
    registration_page = RegistrationPage(browser)
    user_data = get_user_data()
    registration_page.registration(*user_data)












