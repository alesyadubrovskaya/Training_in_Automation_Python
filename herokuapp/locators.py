from selenium.webdriver.common.by import By

add_button = ('xpath', '//button[text() = "Add Element"]')
delete_button1 = ('xpath', '(//button[text() = "Delete"])[1]')
delete_button2 = ('xpath', '(//button[text() = "Delete"])[2]')
delete_button3 = ('xpath', '(//button[text() = "Delete"])[3]')


check_1 = ('xpath', '(//input[@type = "checkbox"])[1]')
check_2 = ('xpath', '(//input[@type = "checkbox"])[2]')

congrat_mess = ('xpath', '//p')
congrat_head = ('xpath', '//h3')

broken_img = (By.TAG_NAME, 'img')