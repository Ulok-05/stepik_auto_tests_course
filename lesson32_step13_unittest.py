from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
import tracemalloc

tracemalloc.start()


class TestTwoPage(unittest.TestCase):
    def test_for_page1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()

        try:
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            input1 = browser.find_element(By.XPATH,
                                          "//div[@class ='first_block']/div[@class ='form-group first_class']/input[@class ='form-control first']")
            input1.send_keys('Ivan')
            input2 = browser.find_element(By.XPATH,
                                          "//div[@ class ='first_block']/div[@class ='form-group second_class']/input[@class ='form-control second']")
            input2.send_keys('Ivanov')
            input3 = browser.find_element(By.XPATH,
                                          "//div[@ class ='first_block']/div[@class ='form-group third_class']/input[@class ='form-control third']")
            input3.send_keys('ivan-01@mail.ru')

            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()
            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)
            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text
            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'Should be absolute value of a number')

        finally:
            time.sleep(10)
            browser.quit()


    def test_for_page2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()

        try:
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            input1 = browser.find_element(By.XPATH,
                                          "//div[@class ='first_block']/div[@class ='form-group first_class']/input[@class ='form-control first']")
            input1.send_keys('Ivan')
            input2 = browser.find_element(By.XPATH,
                                          "//div[@ class ='first_block']/div[@class ='form-group second_class']/input[@class ='form-control second']")
            input2.send_keys('Ivanov')
            input3 = browser.find_element(By.XPATH,
                                          "//div[@ class ='first_block']/div[@class ='form-group third_class']/input[@class ='form-control third']")
            input3.send_keys('ivan-01@mail.ru')

            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()
            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)
            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text
            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'Should be absolute value of a number')

        finally:
            time.sleep(10)
            browser.quit()


if __name__ == "__main__":
    unittest.main()

