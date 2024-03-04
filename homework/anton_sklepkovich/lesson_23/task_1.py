import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.fixture()
def driver():
    options = Options()
    # options.add_argument('start-maximized')
    # options.add_argument('--window-size=19 20,1080')
    # options.add_experimental_option('detach', True)
    chrome_driver = webdriver.Chrome(options=options)
    # chrome_driver.maximize_window()
    # chrome_driver.set_window_size(1920, 1080)
    return chrome_driver


def test_input_data(driver):
    input_data = 'Selenium'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    input_text = driver.find_element(By.ID, 'id_text_string')
    input_text.send_keys(input_data)
    # input_text.submit()
    input_text.send_keys(Keys.ENTER)
    result_text = driver.find_element(By.ID, 'result-text')
    print(result_text.text)
