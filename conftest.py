from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from pages.page_home import HomePage
from pages.base_page import BasePage
from locators.locators1 import LocatorsCollector
from pages.page_list_orders import PageOrder
from locators.url import UrlCollector
import allure
from locators.data import AuthData
import string 
import random 
import json
import requests
from pages.order_page import OrderPage

def pytest_generate_tests(metafunc):
    if "browser" in metafunc.fixturenames:
        metafunc.parametrize("browser", ["chrome"], indirect=True)

@pytest.fixture(scope="function")
def browser(request):
    base_page = BasePage(browser)

    if request.param == "chrome":
        driver = base_page.get_driver_chrome()
    elif request.param == "firefox":
        driver = base_page.get_driver_firefox()
    driver.maximize_window()
    driver.get(UrlCollector.url_home)
    yield driver
    
    driver.quit()

@pytest.fixture(scope="function", autouse=False)
def number_order(browser):
    order_page = OrderPage(browser)
    return order_page.register_order()