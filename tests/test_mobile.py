from selene import browser
from conftest import *


is_mobile = True

def test_mob_sign_in(mobile_view):
    if mobile_view is False:
        pytest.skip(reason="пропускаем потому что не мобильная версия")
    else:
        browser.open('')
        browser.element('.flex-1 a.flex-order-1').click()  # sign in

def test_mob_sign_in_with_params(mobile_view, type_of_device):
    if type_of_device == "WEB":
        pytest.skip(reason="пропускаем потому что не мобильная версия")
    else:
        browser.open('')
        browser.element('.flex-1 a.flex-order-1').click()  # sign in



