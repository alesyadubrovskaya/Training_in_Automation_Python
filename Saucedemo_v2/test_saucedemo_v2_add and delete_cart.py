import time
from data import *
from locators import *


def test_add_to_cart_mp(browser, auth_stand):
    browser.get(main_page_url)
    browser.find_element(*add_button_mp).click()
    browser.find_element(*cart_button_mp).click()
    assert browser.current_url == cart_url
    item_cart = browser.find_element(*item_1_name)
    assert item_cart.text == item1_name
    item_cart_price = browser.find_element(*item_1_price)
    assert item_cart_price.text == item1_price


def test_add_to_cart_ip(browser, auth_stand):
    browser.get(main_page_url)
    browser.find_element(*item_1_link).click()
    browser.find_element(*add_button_ip).click()
    browser.find_element(*cart_button_mp).click()
    assert browser.current_url == cart_url
    item_cart = browser.find_element(*item_1_name)
    assert item_cart.text == item1_name
    item_cart_price = browser.find_element(*item_1_price)
    assert item_cart_price.text == item1_price


def test_delete_from_cart_ip(browser, auth_stand, add_cart_ip):
    item_cart = browser.find_element(*item_1_name)
    assert item_cart.text == item1_name
    item_cart_price = browser.find_element(*item_1_price)
    assert item_cart_price.text == item1_price
    browser.find_element(*remove_buttom_ip).click()
    browser.find_element(*cart_button_mp).click()
    assert browser.current_url == cart_url


def test_delete_from_cart_mp(browser, auth_stand, add_cart_mp):
    browser.find_element(*cart_button_mp).click()
    assert browser.current_url == cart_url
    browser.back()
    browser.find_element(*remove_button_mp).click()
    browser.find_element(*remove_button_mp_1).click()
    browser.find_element(*remove_button_mp_2).click()
    browser.find_element(*remove_button_mp_3).click()
    browser.find_element(*cart_button_mp).click()
    assert browser.current_url == cart_url


def test_delete_from_cart_cp(browser, auth_stand, add_cart_mp):
    browser.find_element(*cart_button_mp).click()
    assert browser.current_url == cart_url
    browser.find_element(*remove_button_mp).click()
    browser.find_element(*remove_button_mp_1).click()
    browser.find_element(*remove_button_mp_2).click()
    browser.find_element(*remove_button_mp_3).click()
    assert browser.current_url == cart_url

