from data import *
from locators import *
import time



def test_auth_ok(browser, auth_stand):
    assert browser.current_url == main_page_url


def test_auth_wrong(browser):
    browser.get(url_auth)
    assert browser.current_url == url_auth
    browser.find_element(*username_input).send_keys(username_wrong)
    browser.find_element(*password_input).send_keys(password_wrong)
    browser.find_element(*login_button).click()
    assert browser.current_url == url_auth
    error_mess = browser.find_element(*login_error1)
    assert error_mess.text == auth_err_1, 'Ok'


def test_auth_empty(browser):
    browser.get(url_auth)
    assert browser.current_url == url_auth
    browser.find_element(*username_input).send_keys('')
    browser.find_element(*password_input).send_keys('')
    browser.find_element(*login_button).click()
    assert browser.current_url == url_auth
    error_mess = browser.find_element(*login_error1)
    assert error_mess.text == auth_err_2, 'Ok'


def test_auth_wrongname(browser):
    browser.get(url_auth)
    assert browser.current_url == url_auth
    browser.find_element(*username_input).send_keys(username_wrong)
    browser.find_element(*password_input).send_keys(password_ok)
    browser.find_element(*login_button).click()
    assert browser.current_url == url_auth
    error_mess = browser.find_element(*login_error1)
    assert error_mess.text == auth_err_1, 'Ok'


def test_auth_wrongpass(browser):
    browser.get(url_auth)
    assert browser.current_url == url_auth
    browser.find_element(*username_input).send_keys(username_ok)
    browser.find_element(*password_input).send_keys(password_wrong)
    browser.find_element(*login_button).click()
    assert browser.current_url == url_auth
    error_mess = browser.find_element(*login_error1)
    assert error_mess.text == auth_err_1, 'Ok'


def test_auth_emptyname(browser):
    browser.get(url_auth)
    assert browser.current_url == url_auth
    browser.find_element(*username_input).send_keys('')
    browser.find_element(*password_input).send_keys(password_wrong)
    browser.find_element(*login_button).click()
    assert browser.current_url == url_auth
    error_mess = browser.find_element(*login_error1)
    assert error_mess.text == auth_err_2, 'Ok'


def test_auth_emptypass(browser):
    browser.get(url_auth)
    assert browser.current_url == url_auth
    browser.find_element(*username_input).send_keys(username_wrong)
    browser.find_element(*password_input).send_keys('')
    browser.find_element(*login_button).click()
    assert browser.current_url == url_auth
    error_mess = browser.find_element(*login_error1)
    assert error_mess.text == auth_err_3, 'Ok'


