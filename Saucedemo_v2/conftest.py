import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from locators import *
from data import *


@pytest.fixture(scope='function', autouse=True)
def browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.page_load_strategy = 'normal'

    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--windows-size=1200,800')

    browser = webdriver.Chrome(options=chrome_options)
    browser.implicitly_wait(10)

    yield browser
    browser.quit()


@pytest.fixture()
def auth_stand(browser):
    browser.get(url_auth)
    browser.find_element(*username_input).send_keys(username_ok)
    browser.find_element(*password_input).send_keys(password_ok)
    browser.find_element(*login_button).click()


@pytest.fixture()
def add_cart_mp(browser, auth_stand):
    browser.get(main_page_url)
    browser.find_element(*add_button_mp).click()
    browser.find_element(*add_button_mp_1).click()
    browser.find_element(*add_button_mp_2).click()
    browser.find_element(*add_button_mp_3).click()


@pytest.fixture()
def add_cart_all(browser, auth_stand):
    browser.get(main_page_url)
    browser.find_element(*add_button_mp).click()
    browser.find_element(*add_button_mp_1).click()
    browser.find_element(*add_button_mp_2).click()
    browser.find_element(*add_button_mp_3).click()
    browser.find_element(*add_button_mp_4).click()
    browser.find_element(*add_button_mp_5).click()


@pytest.fixture()
def add_cart_ip(browser, auth_stand):
    browser.get(main_page_url)
    browser.find_element(*item_1_link).click()
    browser.find_element(*add_button_ip).click()

