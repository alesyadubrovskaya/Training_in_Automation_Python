import time
from data import *
from locators import *

def test_select_item_by_name(browser, auth_stand):
    browser.get(main_page_url)
    browser.find_element(*item_1_link).click()
    assert browser.current_url == item1_url
    i1name = browser.find_element(*item_1_name)
    assert i1name.text == item1_name
    i1desc = browser.find_element(*item_1_descr)
    assert i1desc.text == item1_desc
    i1price = browser.find_element(*item_1_price)
    assert i1price.text == item1_price
    i1img = browser.find_element(*item_1_img)
    assert i1img.get_dom_attribute('src') == item1_img


def test_select_item_by_image(browser, auth_stand):
    browser.get(main_page_url)
    browser.find_element(*item_1_imglink).click()
    assert browser.current_url == item1_url
    i1name = browser.find_element(*item_1_name)
    assert i1name.text == item1_name
    i1desc = browser.find_element(*item_1_descr)
    assert i1desc.text == item1_desc
    i1price = browser.find_element(*item_1_price)
    assert i1price.text == item1_price
    i1img = browser.find_element(*item_1_img)
    assert i1img.get_dom_attribute('src') == item1_img

