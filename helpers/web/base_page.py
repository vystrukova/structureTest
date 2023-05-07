import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:

    def __init__(self, browser, project, locator):
        self.browser = browser
        self.project = project
        self.locator = locator

    def return_url(self):
        return self.browser.current_url

    def is_visible(self, locator, timeout):
        """
        Проверяет что элемент visible
        """
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
            WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def wait_for_visible(self, locator, timeout):
        for _ in range(timeout):
            if self.is_visible(locator, timeout):
                return True
            time.sleep(0.5)
        return False
