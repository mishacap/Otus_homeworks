import time
import random

from selenium.webdriver.common.by import By
from conftest import browser, base_url

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from helpers import create_random_user
from page_objects.main_page import MainPage
from page_objects.user_page import UserPage
from page_objects.product_page import ProductPage
from page_objects.cart_page import CartPage
from page_objects.checkout_page import CheckoutPage
from page_objects.comparison_page import ComparisonPage
from page_objects.wishlist_page import WishListPage
from page_objects.alert_element import AlertSuccessElement



def test_top_elements(browser, base_url):
    browser.get(f"{base_url}:8081")
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#top > div > div.nav.float-start")))
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#search > button")))
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#search > input")))
    WebDriverWait(browser, 3).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#category")))
    WebDriverWait(browser, 2 ).until(
        method=EC.title_is("Your Store"),
        message="Не дождался корректного тайтла страницы"
    )


def test_administration_elements(browser, base_url):
    browser.get(f"{base_url}:8081/administration/")
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#input-username")))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#input-password")))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#form-login > div.text-end > button")))


def test_registration_elements(browser, base_url):
    browser.get(f"{base_url}:8081/index.php?route=account/register")
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#input-firstname")))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#input-email")))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#input-password")))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#input-newsletter")))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#form-register > div > button")))


def test_product_elements(browser, base_url):
    browser.get(f"{base_url}:8081/en-gb/product/apple-cinema")
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#content > div.row.mb-3 > div:nth-child(1) > div > a > img")))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#content > div.row.mb-3 > div:nth-child(1) > div")))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#content > div.row.mb-3 > div:nth-child(2) > form > div > button:nth-child(1)")))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#content > div.row.mb-3 > div:nth-child(2) > form > div > button:nth-child(2)")))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#button-cart")))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR,
         "#content > div.row.mb-3 > div:nth-child(2) > ul:nth-child(3) > li:nth-child(2) > h2 > span")))
    WebDriverWait(browser, 2 ).until(
        method=EC.title_is("Apple Cinema 30"),
        message="Не дождался корректного тайтла страницы"
    )


def test_catalog_elements(browser, base_url):
    browser.get(f"{base_url}:8081/en-gb/catalog/")
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#column-left > div.list-group.mb-3 > a:nth-child(1)")))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#column-left > div.list-group.mb-3 > a:nth-child(2)")))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#column-left > div.list-group.mb-3 > a:nth-child(3)")))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#column-left > div.list-group.mb-3 > a:nth-child(4)")))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#column-left > div.list-group.mb-3 > a:nth-child(5)")))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#column-left > div.list-group.mb-3 > a:nth-child(6)")))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#column-left > div.list-group.mb-3 > a:nth-child(7)")))
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#column-left > div.list-group.mb-3 > a:nth-child(8)")))


def test_login_logout_administration(browser, base_url):
    browser.get(f"{base_url}:8081/administration/")
    input_username = browser.find_element(By.ID, "input-username")
    input_username.send_keys("user")
    input_password = browser.find_element(By.ID, "input-password")
    input_password.send_keys("bitnami")
    browser.find_element(By.CSS_SELECTOR, "#form-login > div.text-end > button").click()
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#nav-profile > a > span")))
    browser.find_element(By.CSS_SELECTOR, "#nav-logout > a > span").click()


def test_check_prices(browser, base_url):
    browser.get(f"{base_url}:8081")
    WebDriverWait(browser, 2).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#form-currency"))
    ).click()
    euro = browser.find_element(By.CSS_SELECTOR, "a[href='EUR']")
    euro.click()
    price_element = WebDriverWait(browser, 3).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".price"))
    )
    price_text = price_element.text
    assert "€" in price_text


def test_add_to_cart_top(browser, base_url):
    browser.get(f"{base_url}:8081")
    selectors = [
        "#content > div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4 > div:nth-child(1) > div > div.content > form > div > button:nth-child(1)",
        "#content > div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4 > div:nth-child(2) > div > div.content > form > div > button:nth-child(1)"
    ]
    random_selector = random.choice(selectors)
    add_to_cart = browser.find_element(By.CSS_SELECTOR, random_selector)
    ActionChains(browser).move_to_element(add_to_cart).perform()
    WebDriverWait(browser, 10).until(
        EC.all_of(EC.visibility_of_element_located((By.CSS_SELECTOR, random_selector)),
                  EC.element_to_be_clickable((By.CSS_SELECTOR, random_selector)))
    )
    browser.find_element(By.CSS_SELECTOR, random_selector).click()

    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#alert > div"))
    )
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#alert > div > button"))
    ).click()

    cart = browser.find_element(By.CSS_SELECTOR, "#header-cart .btn.btn-lg.btn-inverse")
    ActionChains(browser).move_to_element(cart).perform()
    cart.click()

    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "img.img-thumbnail"))
    )
