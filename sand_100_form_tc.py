from time import sleep
from random import choice
from selenium import webdriver
from selenium.webdriver.common.by import By

names = ['Rahim', 'Tony', 'Sterling', 'Cross', 'Madrid', 'London', 'Real', 'Chelsea']
url = 'https://suninjuly.github.io/huge_form.html'

with webdriver.Chrome() as browser:
    browser.get(url)
    sleep(1)

    forms = browser.find_elements(By.CSS_SELECTOR, '.first_block input')

    for form in forms:
        form.send_keys(choice(names))

    browser.find_element(By.TAG_NAME, 'button').click()

    sleep(5)

    alert = browser.switch_to.alert
    print(alert.text)



