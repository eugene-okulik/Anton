from playwright.sync_api import Page


def test_login(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    search_field = page.get_by_role('link', name='Form Authentication')
    search_field.click()
    input_login = page.get_by_role('textbox', name='Username')
    input_password = page.get_by_role('textbox', name='Password')
    button = page.get_by_role('button', name='Login')
    input_login.fill('login')
    input_password.fill('password')
    button.click()
