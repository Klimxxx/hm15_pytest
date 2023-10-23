from selene import browser
from conftest import *


is_mobile = False

def test_web_sign_in(web_view):
    if is_mobile == True:
        pytest.skip(reason="пропускаем потому что не веб версия")
    else:
        browser.open('')
        browser.element('.HeaderMenu-link--sign-in').click()  # sign in


def test_web_sign_in_with_params(web_view, type_of_device):
    if type_of_device == "MOBILE":
        pytest.skip(reason="пропускаем потому что не веб версия")
    else:
        browser.open('')
        browser.element('.HeaderMenu-link--sign-in').click()



