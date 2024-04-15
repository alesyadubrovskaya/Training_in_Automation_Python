from locators import *
from data import *
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_delete(browser):
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    browser.get(element_url)
    wait.until(EC.element_to_be_clickable(add_button)).click()
    assert browser.find_element(*delete_button1).is_displayed()
    wait.until(EC.element_to_be_clickable(delete_button1)).click()
    assert wait.until(EC.invisibility_of_element(delete_button1))


def test_add_delete_some(browser):
    wait = WebDriverWait(browser, 30, poll_frequency=1)
    browser.get(element_url)
    wait.until(EC.element_to_be_clickable(add_button)).click()
    assert browser.find_element(*delete_button1).is_displayed()
    browser.find_element(*add_button).click()
    assert browser.find_element(*delete_button2).is_displayed()
    browser.find_element(*add_button).click()
    assert browser.find_element(*delete_button3).is_displayed()
    wait.until(EC.element_to_be_clickable(delete_button3)).click()
    assert wait.until(EC.invisibility_of_element(delete_button3))
    wait.until(EC.element_to_be_clickable(delete_button2)).click()
    assert wait.until(EC.invisibility_of_element(delete_button2))
    wait.until(EC.element_to_be_clickable(delete_button1)).click()
    assert wait.until(EC.invisibility_of_element(delete_button1))