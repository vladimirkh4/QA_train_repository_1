import math
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


url = 'https://suninjuly.github.io/execute_script.html'

with webdriver.Chrome() as browser:
    browser.get(url)

    num = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.ID, 'answer').send_keys(calc(num))

    browser.find_element(By.ID, 'robotCheckbox').click()

    robot = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot)
    robot.click()

    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    alert = browser.switch_to.alert.text
    print(alert)



