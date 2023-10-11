from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def math_funk(x):
    return math.log(abs(12*math.sin(x)))


link = "https://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    x = int(browser.find_element(By.ID, 'input_value').text)
    final_x = math_funk(x)

    input_answer = browser.find_element(By.ID, 'answer')
    input_answer.send_keys(final_x)

    robot_Checkbox = browser.find_element(By.ID, 'robotCheckbox').click()
    browser.execute_script("window.scrollBy(0, 100);")
    robots_Rule = browser.find_element(By.ID, 'robotsRule').click()


    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

