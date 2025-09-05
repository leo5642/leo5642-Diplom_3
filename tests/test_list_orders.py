from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from pages.page_home import HomePage
from locators.locators1 import LocatorsCollector
from locators.url import UrlCollector
from pages.page_list_orders import PageOrder
import allure

class Testbookscollector2:
    @allure.title("Проверка увелечения счетчика общего заказов при добавлении заказа")
    def test_sum_order_plus_one(self, browser, request):
        order_bage = PageOrder(browser)
        self.driver = browser
        order_bage.get_open_url_orders_list()
        orders_all = order_bage.get_text_order_all()
       
        order = request.getfixturevalue("number_order")
        assert len(str(order)) == 6
        orders_all1 = order_bage.get_text_order_all()
        
        assert int(orders_all) + 1 == int(orders_all1)

    @allure.title("Проверка увелечения счетчика сегодня заказов при добавлении заказа")
    def test_sum_today_order_plus_one(self, browser, request):
        order_bage = PageOrder(browser)
        self.driver = browser
        order_bage.get_open_url_orders_list()
        orders_all = order_bage.get_text_order_today()
       
        order = request.getfixturevalue("number_order")
        assert len(str(order)) == 6
        orders_all1 = order_bage.get_text_order_today()
        
        assert int(orders_all) + 1 == int(orders_all1)

    @allure.title("Проверка появления номера заказа в списке ленты заказов")
    def test_number_order_in_list_orters(self, browser, request):
        order_bage = PageOrder(browser)
        self.driver = browser
        order_bage.get_open_url_orders_list()
       
        order = request.getfixturevalue("number_order")
        assert len(str(order)) == 6
        orders_all = order_bage.get_text_order_list()
        
        assert '#0' + str(order) == orders_all


