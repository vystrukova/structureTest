import pytest

import config.projects.yandex.info
import config.projects.google.info

import locators.web.yandex.locators
import locators.web.google.locators

supported_projects = {
    'yandex': config.projects.yandex.info.YandexInfo,
    'google': config.projects.google.info.GoogleInfo
}

supported_locators = {
    'yandex': locators.web.yandex.locators.YandexLocators,
    'google': locators.web.google.locators.GoogleLocators
}


def pytest_addoption(parser):
    parser.addoption('--project_name', action='store', default='yandex',
                     help='Choose project:')
    parser.addoption('--locator_name', action='store', default='yandex',
                     help='Choose locators:')


@pytest.fixture(scope="session")
def project(request):
    project_name = request.config.getoption("project_name")

    if project_name == "yandex":
        print(f"\nstart yandex for test..")
        project = config.projects.yandex.info.YandexInfo
    elif project_name == "google":
        print(f"\nstart google for test..")
        project = config.projects.google.info.GoogleInfo
    else:
        raise pytest.UsageError(f"--project_name is invalid")

    yield project


@pytest.fixture(scope="session")
def locator(request):
    locator_name = request.config.getoption("locator_name")

    if locator_name == "yandex":
        print(f"\nstart yandex locators for test..")
        locator = locators.web.yandex.locators.YandexLocators
    elif locator_name == "google":
        print(f"\nstart google locators for test..")
        locator = locators.web.google.locators.GoogleLocators
    else:
        raise pytest.UsageError(f"--locator_name is invalid")

    yield locator

