import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    return chrome_driver


def test_select_python(driver):
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#id_choose_language')))
    chose_select = driver.find_element(By.CSS_SELECTOR, '#id_choose_language')
    chose_select = Select(chose_select)
    chose_select.select_by_value('1')
    submit = driver.find_element(By.CSS_SELECTOR, '#submit-id-submit')
    submit.submit()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#result')))
    result = driver.find_element(By.CSS_SELECTOR, '#result')
    result_text = result.text.split()[-1]
    assert result_text == 'Python'


def test_start_hello_world(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#start')))
    start = driver.find_element(By.CSS_SELECTOR, '#start button')
    start.click()
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#finish')))
    hello_world = driver.find_element(By.CSS_SELECTOR, '#finish')
    assert hello_world.text == 'Hello World!'
