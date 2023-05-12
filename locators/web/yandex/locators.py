from selenium.webdriver.common.by import By


class YandexTestLocators:
    def __init__(self):
        self.yandex_locators = YandexLocators()


class YandexLocators:
    BASE_LOGO = (By.XPATH, "//input[@class='search3__input mini-suggest__input']")
