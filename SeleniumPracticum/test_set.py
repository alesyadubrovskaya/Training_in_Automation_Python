from locators import *
from data import *
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_ok_time_sleep(driver):
    driver.get(base_url)
    head = driver.find_element(*header)
    assert head.text == head_er
    time.sleep(5)
    assert driver.find_element(*start_button).is_displayed() is True
    driver.find_element(*start_button).click()
    driver.find_element(*username_field).send_keys(username_ok)
    driver.find_element(*password_field).send_keys(password_ok)
    driver.find_element(*checkbox).click()
    assert driver.find_element(*checkbox).is_selected() is True
    driver.find_element(*login_button).click()
    wait = driver.find_element(*waiting_load)
    assert wait.is_displayed() is True
    time.sleep(5)
    mess = driver.find_element(*success_mess)
    assert mess.text == successMess


def test_login_ok_implicitly(driver):
    driver.implicitly_wait(10)
    driver.get(base_url)
    head = driver.find_element(*header)
    assert head.text == head_er
    time.sleep(5)
    assert driver.find_element(*start_button).is_displayed() is True
    driver.find_element(*start_button).click()
    driver.find_element(*username_field).send_keys(username_ok)
    driver.find_element(*password_field).send_keys(password_ok)
    driver.find_element(*checkbox).click()
    assert driver.find_element(*checkbox).is_selected() is True
    driver.find_element(*login_button).click()
    wait = driver.find_element(*waiting_load)
    assert wait.is_displayed() is True
    time.sleep(5)
    mess = driver.find_element(*success_mess)
    assert mess.text == successMess


def test_login_ok_explicitly(driver):
    wait = WebDriverWait(driver, 30, poll_frequency=1)
    driver.get(base_url)
    head = driver.find_element(*header)
    assert head.text == head_er
    wait.until(EC.visibility_of_element_located(start_button))
    assert driver.find_element(*start_button).is_displayed() is True
    driver.find_element(*start_button).click()
    driver.find_element(*username_field).send_keys(username_ok)
    driver.find_element(*password_field).send_keys(password_ok)
    driver.find_element(*checkbox).click()
    assert driver.find_element(*checkbox).is_selected() is True
    driver.find_element(*login_button).click()
    wait.until(EC.visibility_of_element_located(waiting_load))
    waiting = driver.find_element(*waiting_load)
    assert waiting.is_displayed() is True
    wait.until(EC.visibility_of_element_located(success_mess))
    mess = driver.find_element(*success_mess)
    assert mess.text == successMess
