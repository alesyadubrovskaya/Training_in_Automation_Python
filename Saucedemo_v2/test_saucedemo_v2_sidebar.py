import time
from data import *
from locators import *


def test_about(browser, auth_stand):
    browser.get(main_page_url)
    browser.find_element(*sidebar_button).click()
    browser.find_element(*about_button).click()
    assert browser.current_url == about_url


def test_logout(browser, auth_stand):
    browser.get(main_page_url)
    browser.find_element(*sidebar_button).click()
    browser.find_element(*logout_button).click()
    assert browser.current_url == url_auth


def test_mp(browser, auth_stand):
    browser.get(cart_url)
    assert browser.current_url == cart_url
    browser.find_element(*sidebar_button).click()
    browser.find_element(*allitems_button).click()
    assert browser.current_url == main_page_url


def test_reset_mp(browser, auth_stand, add_cart_mp):
    browser.get(main_page_url)
    browser.find_element(*sidebar_button).click()
    browser.find_element(*reset_button).click()
    assert browser.current_url == main_page_url


def test_reset_cp(browser, auth_stand, add_cart_all):
    browser.find_element(*cart_button_mp).click()
    browser.find_element(*sidebar_button).click()
    browser.find_element(*reset_button).click()
    assert browser.current_url == cart_url
    browser.refresh()


def test_reset_ip(browser, auth_stand, add_cart_ip):
    browser.find_element(*sidebar_button).click()
    browser.find_element(*reset_button).click()
    assert browser.current_url == item1_url
    browser.refresh()