from config.projects.google.info import *
from locators.web.google.locators import *

from config.projects.yandex.info import *
from locators.web.yandex.locators import *


class ProjectYandex:

    def __init__(self):
        self.project_config = Yandex().yandex_info
        self.project_test_locators = YandexTestLocators().yandex_locators


class ProjectGoogle:

    def __init__(self):
        self.project_config = Google().google_info
        self.project_test_locators = GoogleTestLocators().google_locators
