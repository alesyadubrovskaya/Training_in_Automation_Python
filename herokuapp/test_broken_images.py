import requests

from locators import *
from data import *
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_find_broken_images(browser):
    browser.get(img_url)
    images = browser.find_elements(*broken_img)
    broken_images = []
    for image in images:
        src = image.get_attribute('src')
        if src:
            response = requests.get(src)
            if response.status_code != 200:
                broken_images.append(src)
                print(f'Broken images found')
    if broken_images:
        print('List of broken images: ')
        for broken_image in broken_images:
            print(broken_image)
    else:
        print('Not found')