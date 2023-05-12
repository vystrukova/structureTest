from selenium.webdriver.common.by import By


class GoogleTestLocators:
    def __init__(self):
        self.google_locators = GoogleLocators()


class GoogleLocators:
    BASE_LOGO = (By.XPATH, "//img[@alt='Google']")
