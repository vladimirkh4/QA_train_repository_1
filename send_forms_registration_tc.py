from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# Данные для заполнения форм при регистации на сайте
data_list = ['Vlad', 'Petrov', 'vld_ptr@mail.ru']
# Номера полей обязательных при регистрации на сайте
fields = ['first', 'second', 'third']

# в цикле проходим по всем сайтам, на которых нужно заполнить форму регистрации
for i in range(1, 3):
    url = f'https://suninjuly.github.io/registration{i}.html'

    with webdriver.Chrome() as browser:
        # открываем сайт в браузере
        browser.get(url)

        try:
            # в цикле проходим по всем полям обязательным для регистрации
            for index in range(3):
                # находим поле
                form = browser.find_element(
                    By.CSS_SELECTOR, f'.first_block input.{fields[index]}')
                # заполняем поле
                form.send_keys(data_list[index])

            # находим и нажимаем кнопку "Submit"
            button = browser.find_element(By.XPATH, '//button[@type="submit"]')
            button.click()

            # ожидаем пока загрузится страница
            sleep(1)

            # находим текст об успешной регистрации
            welcome_text = browser.find_element(By.TAG_NAME, "h1").text

            # проверяем текст
            assert "Congratulations! You have successfully registered!" == welcome_text

            # если всё хорошо печатаем сообщение об успешной регистрации
            print(f'''Регистрация на сайте по адресу:
suninjuly.github.io/registration{i}.html
прошла успешно!!!
''')
            sleep(5)

        # если в процессе регистрации произошла ошибка печатем об этом сообщение
        # с указанием ошибки
        except Exception as err:
            print(f'''Регистрация на сайте по адресу:
suninjuly.github.io/registration{i}.html
завершилась ошибкой:
{err}''')







