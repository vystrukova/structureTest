import pytest
from open_page import OpenPage


class TestOpenPage:

    def test_open_page(self, browser, project):
        open_page = OpenPage(browser, project)
        browser = open_page.open_page(browser)
        assert browser.current_url == project.BASE_URL
