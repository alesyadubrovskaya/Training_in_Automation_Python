import time
from locators import *
from data import *

def test_order_ok(browser, auth_stand, add_cart_ip):
    browser.find_element(*cart_button_mp).click()
    assert browser.current_url == cart_url
    browser.find_element(*checkout_button).click()
    assert browser.current_url == order_form_url
    browser.find_element(*order_fname).send_keys(order_fname_ok)
    browser.find_element(*order_lname).send_keys(order_lname_ok)
    browser.find_element(*order_zipcode).send_keys(order_zipcode_ok)
    browser.find_element(*order_continue).click()
    assert browser.current_url == order_info_url
    browser.find_element(*order_confirm).click()
    assert browser.current_url == order_finish_url
    browser.find_element(*order_return_mp).click()
    assert browser.current_url == main_page_url


def test_order_wrong(browser, auth_stand, add_cart_mp):
    browser.find_element(*cart_button_mp).click()
    assert browser.current_url == cart_url
    browser.find_element(*checkout_button).click()
    assert browser.current_url == order_form_url
    browser.find_element(*order_fname).send_keys(order_fname_wrong)
    browser.find_element(*order_lname).send_keys(order_lname_wrong)
    browser.find_element(*order_zipcode).send_keys(order_zipcode_wrong)
    browser.find_element(*order_continue).click()
    assert browser.current_url == order_info_url
    browser.find_element(*order_confirm).click()
    assert browser.current_url == order_finish_url
    browser.find_element(*order_return_mp).click()
    assert browser.current_url == main_page_url


def test_order_empty(browser, auth_stand, add_cart_mp):
    browser.find_element(*cart_button_mp).click()
    assert browser.current_url == cart_url
    browser.find_element(*checkout_button).click()
    assert browser.current_url == order_form_url
    browser.find_element(*order_fname).send_keys('')
    browser.find_element(*order_lname).send_keys('')
    browser.find_element(*order_zipcode).send_keys('')
    browser.find_element(*order_continue).click()
    assert browser.current_url == order_form_url
    order_error = browser.find_element(*order_empty_error)
    assert order_error.text == order_error_message_1


def test_order_empty_first_name(browser, auth_stand, add_cart_mp):
    browser.find_element(*cart_button_mp).click()
    assert browser.current_url == cart_url
    browser.find_element(*checkout_button).click()
    assert browser.current_url == order_form_url
    browser.find_element(*order_fname).send_keys('')
    browser.find_element(*order_lname).send_keys(order_lname_ok)
    browser.find_element(*order_zipcode).send_keys(order_zipcode_wrong)
    browser.find_element(*order_continue).click()
    assert browser.current_url == order_form_url
    order_error = browser.find_element(*order_empty_error)
    assert order_error.text == order_error_message_1


def test_order_empty_lname(browser, auth_stand, add_cart_mp):
    browser.find_element(*cart_button_mp).click()
    assert browser.current_url == cart_url
    browser.find_element(*checkout_button).click()
    assert browser.current_url == order_form_url
    browser.find_element(*order_fname).send_keys(order_fname_wrong)
    browser.find_element(*order_lname).send_keys('')
    browser.find_element(*order_zipcode).send_keys(order_zipcode_ok)
    browser.find_element(*order_continue).click()
    assert browser.current_url == order_form_url
    order_error = browser.find_element(*order_empty_error)
    assert order_error.text == order_error_message_2


def test_order_emptyzipcode(browser, auth_stand, add_cart_mp):
    browser.find_element(*cart_button_mp).click()
    assert browser.current_url == cart_url
    browser.find_element(*checkout_button).click()
    assert browser.current_url == order_form_url
    browser.find_element(*order_fname).send_keys(order_fname_ok)
    browser.find_element(*order_lname).send_keys(order_lname_wrong)
    browser.find_element(*order_zipcode).send_keys('')
    browser.find_element(*order_continue).click()
    assert browser.current_url == order_form_url
    order_error = browser.find_element(*order_empty_error)
    assert order_error.text == order_error_message_3


def test_order_empty_cart(browser, auth_stand):
    browser.get(main_page_url)
    browser.find_element(*cart_button_mp).click()
    assert browser.current_url == cart_url
    browser.find_element(*checkout_button).click()
    assert browser.current_url == order_form_url
    browser.find_element(*order_fname).send_keys(order_fname_ok)
    browser.find_element(*order_lname).send_keys(order_lname_ok)
    browser.find_element(*order_zipcode).send_keys(order_zipcode_ok)
    browser.find_element(*order_continue).click()
    assert browser.current_url == order_info_url
    browser.find_element(*order_confirm).click()
    assert browser.current_url == order_finish_url
    browser.find_element(*order_return_mp).click()
    assert browser.current_url == main_page_url
