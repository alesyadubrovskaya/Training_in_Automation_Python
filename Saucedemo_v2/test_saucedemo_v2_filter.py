import time
from data import *
from locators import *

def test_filter_za(browser, auth_stand):
    browser.get(main_page_url)
    assert browser.current_url == main_page_url, 'Wrong url'
    browser.find_element(*filter).click()
    browser.find_element(*za).click()
    item1 = browser.find_element(*first_item)
    item6 = browser.find_element(*last_item)
    assert item1.text == first_it_za, 'Wrong item'
    assert item6.text == last_it_za, 'Wrong item'


def test_filter_lh(browser, auth_stand):
    browser.find_element(*filter).click()
    browser.find_element(*lh).click()
    item1 = browser.find_element(*first_item_price)
    item6 = browser.find_element(*last_item_price)
    assert item1.text == first_it_lh, 'Wrong price'
    assert item6.text == last_it_lh, 'Wrong price'


def test_filter_hl(browser, auth_stand):
    browser.find_element(*filter).click()
    browser.find_element(*hl).click()
    item1 = browser.find_element(*first_item_price)
    item6 = browser.find_element(*last_item_price)
    assert item1.text == first_it_hl, 'Wrong price'
    assert item6.text == last_it_hl, 'Wrong price'


def test_filter_az(browser, auth_stand):
    browser.find_element(*filter).click()
    browser.find_element(*az).click()
    item1 = browser.find_element(*first_item)
    item6 = browser.find_element(*last_item)
    assert item1.text == first_it_az, 'Wrong item'
    assert item6.text == last_it_az, 'Wrong item'