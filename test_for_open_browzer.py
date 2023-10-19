import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import math
from selenium.webdriver.chrome.options import Options




@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")



@pytest.mark.parametrize('number', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
def test_sign_in_on_stepic(browser, number):
    link = f'https://stepik.org/lesson/{number}/step/1'
    o = Options()
    o.add_experimental_option("detach", True)
    browser = webdriver.Chrome(o)
    browser.get(link)
    browser.implicitly_wait(15)
    browser.find_element(By.ID, 'ember33').click()
    browser.find_element(By.ID, 'id_login_email').send_keys('ulok-05@mail.ru')
    browser.find_element(By.ID, 'id_login_password').send_keys('Stepic526266')
    browser.find_element(By.XPATH, '//*[@id="login_form"]/button').click()


    #жмем "попробовать снова"
    # WebDriverWait(browser, 30).until(
    #       EC.element_to_be_clickable((By.CLASS_NAME, "again-btn"))
    # ).click()

    #сравниваем
    # assert "Correct!" == feed_back




