from selenium import webdriver
from selenium.webdriver.common.by import By
import math

import time

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()


def funk(x):
    return math.log(math.fabs(12*math.sin(x)))


try:
    browser.get(link)
    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()

    x = int(browser.find_element(By.ID, 'input_value').text)
    result = funk(x)

    input_answer = browser.find_element(By.ID, 'answer')
    input_answer.send_keys(result)

    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    alert.accept()

    print(alert_text)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

