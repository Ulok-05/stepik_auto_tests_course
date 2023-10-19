from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


def funk(x):
    return math.log(math.fabs(12 * math.sin(x)))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:
    # говорим Selenium проверять в течение 13 секунд, пока стоимость не станет 100
    price = WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    browser.find_element(By.ID, 'book').click()

    x = int(browser.find_element(By.ID, 'input_value').text)
    x_result = funk(x)

    input_answer = browser.find_element(By.ID, 'answer')
    input_answer.send_keys(x_result)

    browser.find_element(By.ID, 'solve').click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    alert.accept()

    print(alert_text)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
