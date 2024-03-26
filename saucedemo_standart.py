from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://www.saucedemo.com/v1/index.html')

user_name = driver.find_element('xpath', '//*[@id="user-name"]')
user_name.send_keys('standard_user')
time.sleep(3)
password = driver.find_element('xpath', '//*[@id="password"]')
password.send_keys('secret_sauce')
time.sleep(3)
login = driver.find_element('xpath', '//*[@id="login-button"]')
login.click()
time.sleep(3)
assert driver.current_url == 'https://www.saucedemo.com/v1/inventory.html', 'Not this URL'

driver.get('https://www.saucedemo.com/v1/inventory.html')
time.sleep(5)
item1 = driver.find_element('xpath', '//*[@id="item_4_title_link"]')
item1.click()
time.sleep(3)
assert driver.current_url == 'https://www.saucedemo.com/v1/inventory-item.html?id=4', 'Not this URL'
driver.get('https://www.saucedemo.com/v1/inventory-item.html?id=4')
add_button = driver.find_element('xpath', '//*[@class="btn_primary btn_inventory"]')
add_button.click()
