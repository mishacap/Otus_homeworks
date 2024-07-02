from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def test_one(browser):
    browser.get("https://google.com")
    assert browser.title == "Google"

def test_two(browser):
    browser.get("http://192.168.31.66:8081")
    assert browser.title == "Your Store"