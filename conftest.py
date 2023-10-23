import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://github.com/'
    browser.config.driver_name = 'chrome'

    yield

    browser.quit()


@pytest.fixture
def web_view():
    browser.config.window_width = 1200
    browser.config.window_height = 1200
    is_mobile = False
    yield


@pytest.fixture
def mobile_view():
    browser.config.window_width = 400
    browser.config.window_height = 800
    is_mobile = True
    yield


@pytest.fixture(params=["WEB", "MOBILE"])
def type_of_device(request):
    return request.param

@pytest.mark.parametrize('type_of_device', ["WEB", "MOBILE"], indirect=True)
def test_dynamic_fixture(type_of_device):
    assert type_of_device in ["WEB", "MOBILE"]

@pytest.fixture(params=["WEB", "MOBILE"])
def param_value(request):
    return request.param