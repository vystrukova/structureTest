import pytest

from project_test import *

supported_projects = {
    'yandex': ProjectYandex(),
    'google': ProjectGoogle()
}


def pytest_addoption(parser):
    parser.addoption('--project_name', action='store', default='yandex',
                     help='Choose project:')


@pytest.fixture(scope="session")
def project(request):
    project_name = request.config.getoption("project_name")

    if project_name == "yandex":
        print(f"\nstart yandex for test..")
        project = ProjectYandex()
    elif project_name == "google":
        print(f"\nstart google for test..")
        project = ProjectGoogle()
    else:
        raise pytest.UsageError(f"--project_name is invalid")

    yield project
