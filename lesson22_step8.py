from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import os


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    input_f_name = browser.find_element(By.NAME, 'firstname')
    input_f_name.send_keys('Galiulina')
    input_l_name = browser.find_element(By.NAME, 'lastname')
    input_l_name.send_keys('Julia')
    input_email = browser.find_element(By.NAME, 'email')
    input_email.send_keys('ulok-05@mail.ru')

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'fail.txt')           # добавляем к этому пути имя файла

    input_file = browser.find_element(By.ID, 'file')
    input_file.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

