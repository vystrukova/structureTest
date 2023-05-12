import config.projects.google.info
import locators.web.google.locators

import config.projects.yandex.info
import locators.web.yandex.locators


class ProjectGoogle:

    def __init__(self):
        self.google = config.projects.google.info.Google()
        self.google_test_locators = locators.web.google.GoogleTestLocators()


class ProjectYandex:

    def __init__(self):
        self.yandex = config.projects.yandex.info.Yandex()
        self.yanex_test_locators = locators.web.yandex.YandexTestLocators()
