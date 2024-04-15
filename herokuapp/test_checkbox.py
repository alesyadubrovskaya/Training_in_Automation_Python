from locators import *
from data import *
import time


def test_checkboxes(browser):
    browser.get(checkbox_url)
    browser.find_element(*check_1).click()
    assert browser.find_element(*check_1).is_selected()
    browser.find_element(*check_2).click()
    assert browser.find_element(*check_2).is_selected() is False
    browser.find_element(*check_1).click()
    assert browser.find_element(*check_1).is_selected() is False
    browser.find_element(*check_2).click()
    assert browser.find_element(*check_2).is_selected()