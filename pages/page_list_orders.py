from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from locators.locators1 import LocatorsCollector
import allure
from pages.base_page import BasePage
from locators.url import UrlCollector

class PageOrder(BasePage):
    
    @allure.step("Метот заполняет поле имя")
    def get_open_url(self, url, locator):
        self.driver.get(url)
        self.find_element(locator)

    @allure.step('Получает текст элемента')
    def get_text(self, locator):
        element = self.find_visible_element(locator)
        return element.text

    @allure.step('Получает текст элемента всех заказов')
    def get_text_order_all(self):
        element = self.find_visible_element(LocatorsCollector.orders_all_time)
        return element.text
    
    @allure.step('Получает текст элемента всех заказов')
    def get_open_url_orders_list(self):
        self.get_open_url(UrlCollector.url_list_order, LocatorsCollector.orders_all_time)
    
    @allure.step('Получает текст элемента за сегодня заказов')
    def get_text_order_today(self):
        element = self.find_visible_element(LocatorsCollector.orders_today)
        return element.text
    
    @allure.step('Получает текст первого элемента из ленты заказов')
    def get_text_order_list(self):
        element = self.find_visible_element(LocatorsCollector.number_order_look)
        return element.text