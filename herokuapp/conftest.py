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
    # chrome_options.add_argument('--disable-cache')
    # chrome_options.add_argument('--incognito')

    browser = webdriver.Chrome(options=chrome_options)

    yield browser
    browser.quit()

