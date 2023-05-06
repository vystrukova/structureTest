

class OpenPage:

    def __init__(self, browser, project):
        self.browser = browser
        self.project = project

    def open_page(self, browser):
        base_url = self.project.BASE_URL
        browser.get(base_url)
        return browser
