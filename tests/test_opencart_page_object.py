import time


from conftest import browser, base_url

from page_objects.administration_page import AdministrationPage
from page_objects.main_page import MainPage
from page_objects.product_page import ProductPage
from page_objects.registration_page import RegistrationPage
from page_objects.alert import Alert
from helpers import get_fake_product, get_random_index, get_user_data, get_product_data


def test_main_elements(browser, base_url):
    browser.get(f"{base_url}:8081/")
    main_page = MainPage(browser)
    main_page.wait_main_elements()

def test_main_search(browser, base_url):
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
    main_page.click_featured_product_2()
    product_page = ProductPage(browser)
    product_page.wait_product_elements()

def test_registration_elements(browser, base_url):
    browser.get(f"{base_url}:8081/index.php?route=account/register")
    registration_page = RegistrationPage(browser)
    registration_page.wait_registration_elements()

def test_registration_new_user(browser, base_url):
    browser.get(f"{base_url}:8081/index.php?route=account/register")
    registration_page = RegistrationPage(browser)
    user_data = get_user_data()
    registration_page.registration(*user_data)

def test_administration_login(browser, base_url):
    browser.get(f"{base_url}:8081/administration/")
    admin_page = AdministrationPage(browser)
    admin_page.login(username="user", password="bitnami")
    admin_page.wait_logged_in()
    admin_page.logout()

def test_change_currency_euro(browser, base_url):
    browser.get(f"{base_url}:8081/")
    main_page = MainPage(browser)
    main_page.change_currency_euro()
    currency = main_page.check_currency()
    assert "€" in currency
    currency_cart = main_page.check_currency_cart()
    assert "€" in currency_cart
    currency_featured = main_page.check_currency_featured()
    assert "€" in currency_featured



def test_change_currency_pound(browser, base_url):
    browser.get(f"{base_url}:8081/")
    main_page = MainPage(browser)
    main_page.change_currency_pound()
    currency = main_page.check_currency()
    assert "£" in currency
    currency_cart = main_page.check_currency_cart()
    assert "£" in currency_cart
    currency_featured = main_page.check_currency_featured()
    assert "£" in currency_featured

def test_change_currency_dollar(browser, base_url):
    browser.get(f"{base_url}:8081/")
    main_page = MainPage(browser)
    main_page.change_currency_dollar()
    currency = main_page.check_currency()
    assert "$" in currency
    currency_cart = main_page.check_currency_cart()
    assert "$" in currency_cart
    currency_featured = main_page.check_currency_featured()
    assert "$" in currency_featured

def test_add_new_product(browser, base_url):
    browser.get(f"{base_url}:8081/administration/")
    admin_page = AdministrationPage(browser)
    admin_page.login(username="user", password="bitnami")
    admin_page.open_catalog()
    product_data = get_product_data()
    admin_page.add_new_product(*product_data)
    admin_page.wait_alert_and_back()
    admin_page.find_new_product(product_data[0])
    admin_page.wait_filter_data()

def test_delete_product(browser, base_url):
    browser.get(f"{base_url}:8081/administration/")
    admin_page = AdministrationPage(browser)
    admin_page.login(username="user", password="bitnami")
    admin_page.open_catalog()
    admin_page.copy_product()
    status = admin_page.chek_status()
    assert "Disabled" in status
    admin_page.delete_product()
    alert = browser.switch_to.alert
    alert.accept()

