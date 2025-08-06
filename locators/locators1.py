from selenium.webdriver.common.by import By
import pytest

class LocatorsCollector:
    button_header = (By.XPATH, "//p[contains(@class, 'header__linkText') and text()='Конструктор']")
    button_lenta_order = (By.XPATH, "//p[contains(@class, 'header__linkText') and text()='Лента Заказов']")
    button_ingridient = (By.CLASS_NAME, "counter_counter__ZNLkj")
    text_ingridient = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title') and text()='Детали ингредиента']")
    button_close_text_ingridient = (By.CLASS_NAME, "Modal_modal__close_modified__3V5XS ")
    konstruktor_bun = (By.CLASS_NAME, "Modal_modal__close_modified__3V5XS ")
    ingridient_number = (By.CLASS_NAME, 'counter_default__28sqi')

    

    orders_all_time = (By.CSS_SELECTOR, "p.OrderFeed_number__2MbrQ")
    orders_today = (By.CSS_SELECTOR, "p.OrderFeed_number__2MbrQ:nth-of-type(2)")
    number_order_look = (By.CLASS_NAME, "text_type_digits-default")
