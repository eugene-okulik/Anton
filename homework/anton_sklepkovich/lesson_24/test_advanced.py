import platform
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


os_type = platform.system()


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('headless')
    options.add_argument('start-maximized')
    options.add_argument('--log-level=3')
    chrome_driver = WebDriver(options=options)
    return chrome_driver


def test_add_item(driver):
    item_name = 'HTC One M9'
    driver.get('https://www.demoblaze.com/index.html')
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.LINK_TEXT, item_name))
    )
    new_tab = driver.find_element(By.LINK_TEXT, item_name)
    new_tab.send_keys(Keys.COMMAND + Keys.ENTER) if os_type == 'Darwin' else new_tab.send_keys(
        Keys.CONTROL + Keys.ENTER
    )
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.btn-success')))
    add_to_cart = driver.find_element(By.CSS_SELECTOR, 'a.btn-success')
    add_to_cart.click()
    WebDriverWait(driver, 5).until(EC.alert_is_present(), '')
    alert = driver.switch_to.alert
    alert.accept()
    driver.close()
    driver.switch_to.window(tabs[0])
    # driver.execute_script('window.scrollTo(0, 0);')
    cart = driver.find_element(By.ID, 'cartur')
    cart.click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.success')))
    item_in_cart = driver.find_element(By.CSS_SELECTOR, '.success')
    item = item_in_cart.find_elements(By.TAG_NAME, 'td')
    assert item[1].text == item_name


def test_first_item(driver):
    expected_item = 'Push It Messenger Bag'
    driver.get('https://magento.softwaretestingboard.com/gear/bags.html')
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'product-item-details')))
    find_item = driver.find_elements(By.CLASS_NAME, 'product-item-details')[0]
    add_to_compare = find_item.find_element(By.CSS_SELECTOR, '[title="Add to Compare"]')
    actions = ActionChains(driver)
    actions.move_to_element(find_item)
    actions.move_to_element(add_to_compare)
    actions.click()
    actions.perform()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'message-success')))
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'odd')))
    compare = driver.find_element(By.CLASS_NAME, 'odd')
    added_item = compare.find_element(By.CLASS_NAME, 'product-item-name')
    assert added_item.text == expected_item
