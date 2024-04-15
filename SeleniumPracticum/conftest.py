import pytest
from selenium import webdriver
from locators import *
from data import *
import time


@pytest.fixture(scope='function', autouse=True)
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--window-size=1200,1080')

    driver = webdriver.Chrome(options=options)

    yield driver
    driver.quit()


