import time

from selenium.webdriver.common.by import By
from conftest import browser, base_url

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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


def test_currency(browser, base_url):
    browser.get(f"{base_url}:8081")
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#form-currency > div > a > span"))).click()
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#form-currency > div > ul > li:nth-child(1) > a")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#form-currency > div > ul > li:nth-child(2) > a")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#form-currency > div > ul > li:nth-child(3) > a"))).click()









