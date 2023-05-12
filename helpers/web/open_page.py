import pytest
from selenium import webdriver
from .base_page import BasePage


class OpenPage(BasePage):

    def __init__(self, browser, project):
        self.browser = browser
        self.project = project
        super().__init__(browser, project)

    def open_page(self):
        base_url = self.project.project_config.BASE_URL
        self.browser.get(base_url)

    def find_logo(self, timeout):
        locator = self.project.project_test_locators.BASE_LOGO
        return self.wait_for_visible(locator, timeout)
