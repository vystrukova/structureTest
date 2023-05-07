import pytest
from selenium import webdriver
from .base_page import BasePage


class OpenPage(BasePage):

    def __init__(self, browser, project, locator):
        self.browser = browser
        self.project = project
        self.locator = locator
        super().__init__(browser, project, locator)

    def open_page(self):
        base_url = self.project.BASE_URL
        self.browser.get(base_url)

    def find_logo(self, timeout):
        locator = self.locator.BASE_LOGO
        return self.wait_for_visible(locator, timeout)
