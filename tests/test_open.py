from helpers.web.open_page import OpenPage


class TestOpenPage:

    def test_open_page(self, browser, project):
        open_page = OpenPage(browser, project)
        open_page.open_page()
        assert browser.current_url == project.project_config.BASE_URL
        logo_element = open_page.find_logo(timeout=3)
        assert logo_element == True
