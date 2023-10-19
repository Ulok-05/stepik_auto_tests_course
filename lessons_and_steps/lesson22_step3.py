from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


link = "https://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    num1 = int(browser.find_element(By.ID, 'num1').text)
    num2 = int(browser.find_element(By.ID, 'num2').text)

    sum_nums = num1 + num2

    select = Select(browser.find_element(By.ID, 'dropdown'))
    select.select_by_value(str(sum_nums))

    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()