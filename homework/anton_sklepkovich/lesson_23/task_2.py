import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import platform


os_type = platform.system()


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('start-maximized')
    chrome_driver = webdriver.Chrome(options=options)
    return chrome_driver


def test_fill_form(driver):
    driver.get('https://demoqa.com/automation-practice-form')
    css_first_name = (By.CSS_SELECTOR, '#firstName')
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(css_first_name))
    input_text_first = driver.find_element(By.CSS_SELECTOR, '#firstName')
    input_text_first.send_keys('Ivan')
    input_text_last = driver.find_element(By.CSS_SELECTOR, '#lastName')
    input_text_last.send_keys('Smirnov')
    input_text_email = driver.find_element(By.CSS_SELECTOR, '#userEmail')
    input_text_email.send_keys('name@example.com')
    gender = driver.find_elements(By.CSS_SELECTOR, '.custom-radio')[0]
    driver.execute_script("arguments[0].scrollIntoView(true);", gender)
    gender.click()
    input_text_phone = driver.find_element(By.CSS_SELECTOR, '#userNumber')
    input_text_phone.send_keys('1234567890')
    input_subject = driver.find_element(By.CSS_SELECTOR, '#subjectsContainer')
    input_subject.click()
    input_subject = driver.find_element(By.CSS_SELECTOR, '#subjectsInput')
    input_subject.send_keys('English')
    input_subject.send_keys(Keys.ENTER)
    input_text_birth = driver.find_element(By.CSS_SELECTOR, '#dateOfBirthInput')
    input_text_birth.click()
    match os_type:
        case 'Windows':
            action = ActionChains(driver)
            action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
        case _:
            action = ActionChains(driver)
            action.key_down(Keys.COMMAND).send_keys('a').key_up(Keys.COMMAND).perform()
    input_text_birth.send_keys('01 Feb 2000')
    input_text_birth.send_keys(Keys.ENTER)
    hobby = driver.find_elements(By.CSS_SELECTOR, '.custom-checkbox')
    hobby[0].click()
    hobby[2].click()
    input_address = driver.find_element(By.CSS_SELECTOR, '#currentAddress')
    input_address.send_keys('Address 123')
    select_state = driver.find_element(By.CSS_SELECTOR, '#state')
    driver.execute_script('arguments[0].scrollIntoView(true)', select_state)
    select_state.click()
    select_state = driver.find_element(By.CSS_SELECTOR, '#react-select-3-input')
    select_state.send_keys('Haryana')
    select_state.send_keys(Keys.ENTER)
    select_city = driver.find_element(By.CSS_SELECTOR, '#city')
    select_city.click()
    select_city = driver.find_element(By.CSS_SELECTOR, '#react-select-4-input')
    select_city.send_keys('Karnal')
    select_city.send_keys(Keys.ENTER)
    submit = driver.find_element(By.CSS_SELECTOR, '#submit')
    submit.submit()
    all_text = driver.find_element(By.CSS_SELECTOR, '.table-responsive')
    print(all_text.text)
