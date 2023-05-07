import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

import config.projects.yandex.info
import config.projects.google.info

from config.projects.google.info import Info
# from config.projects.yandex.info import Info

supported_projects = {
    'yandex': config.projects.yandex.info.Info,
    'google': config.projects.google.info.Info
}


def pytest_addoption(parser):
    parser.addoption('--project_name', action='store', default='yandex',
                     help='Choose project:')


@pytest.fixture(scope="session")
def project(request):
    project_name = request.config.getoption("project_name")

    if project_name == "yandex":
        print(f"\nstart yandex for test..")
        project = config.projects.yandex.info.Info
    elif project_name == "google":
        print(f"\nstart google for test..")
        project = config.projects.google.info.Info
    else:
        raise pytest.UsageError(f"--project_name is invalid")

    yield project
