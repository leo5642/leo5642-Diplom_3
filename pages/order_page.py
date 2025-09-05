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

class OrderPage:
    def __init__(self, browser):
        self.browser = browser

    def generate_random_string(self, length=10):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    @allure.step('Регистрация нового пользователя')
    def register_new_user(self):
        email = self.generate_random_string(10) + '@test.ru'
        password = self.generate_random_string(10)
        name = self.generate_random_string(10)
        
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        requests.post(UrlCollector.url_register, data=payload)
        return email, password

    @allure.step('Авторизация пользователя')
    def login_user(self, email, password):
        payload = {
            "email": email,
            "password": password
        }
        response = requests.post(UrlCollector.url_login, data=payload)
        return response.json()["accessToken"]

    @allure.step('Создание нового заказа')
    def create_new_order(self, token):
        headers = {"Authorization": f"{token}"}
        response = requests.post(
            UrlCollector.url_order,
            data=AuthData.my_order.copy(),
            headers=headers
        )
        return response.json()["order"]["number"]

    @allure.step('Полный процесс создания заказа')
    def register_order(self):
        email, password = self.register_new_user()
        token = self.login_user(email, password)
        return self.create_new_order(token)