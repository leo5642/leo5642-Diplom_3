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
from selenium.webdriver import ActionChains

class HomePage(BasePage):
    @allure.step('Метот нажимает на кнопку Конструктор')
    def click_button_kom(self):
        self.click(LocatorsCollector.button_header)
    
    @allure.step('Метот нажимает на Лента заказов')
    def click_button_order(self):
        self.click(LocatorsCollector.button_lenta_order)
    
    @allure.step('Метот нажимает на ингридиент')
    def click_button_bun(self):
        self.click(LocatorsCollector.button_ingridient)
    
    @allure.step('Метот возвращает текст активного ингридиента')
    def get_text_activ(self):
        return self.get_text(LocatorsCollector.text_ingridient)
    
    @allure.step('Метот нажимает на крестик раскрытого ингридиента')
    def click_button_close_bun(self):
        self.click(LocatorsCollector.button_close_text_ingridient)
    
    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step("перенос элемента в конструктор")
    def drag_and_drop_in_konst(self):
        ingredient = self.find_element(LocatorsCollector.button_ingridient)
        target = self.find_element(LocatorsCollector.konstruktor_bun)
        self.drag_and_drop(ingredient, target)

    @allure.step("получение количества ингридиента")
    def text_number(self):
        return self.get_text(LocatorsCollector.ingridient_number)
    