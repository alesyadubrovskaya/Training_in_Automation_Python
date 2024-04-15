from selenium.common import NoAlertPresentException, TimeoutException

from locators import *
from data import *
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_auth_if_alert(browser):
    wait = WebDriverWait(browser, 5, poll_frequency=1)
    browser.get(auth_url)
    try:
        wait.until(EC.alert_is_present())
        browser.switch_to.alert
    except (NoAlertPresentException, TimeoutException):
        pass
    else:
        print('No alert')


def test_auth_alert_ok(browser):
    browser.get(auth_url_ok)
    assert browser.find_element(*congrat_head).text == header
    assert browser.find_element(*congrat_mess).text == congratulate