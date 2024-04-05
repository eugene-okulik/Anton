import allure
from test_UI_asklepkovich_pw.pages.base_page import BasePage
from test_UI_asklepkovich_pw.pages.locators import create_account_locators as loc
from test_UI_asklepkovich_pw.utils.generate_data import fake_data_for_account


class CreateAccount(BasePage):
    page_url = '/customer/account/create/'

    @allure.step('Fill all element on form create new account')
    def fill_all_form(self, data=fake_data_for_account):
        first_name = self.find(loc.first_name)
        last_name = self.find(loc.last_name)
        email_field = self.find(loc.email)
        password_field = self.find(loc.password)
        confirm_password_field = self.find(loc.confirm_password)
        btn_create_field = self.find(loc.btn_create_account)
        first_name.fill(data.get('first_name'))
        last_name.fill(data.get('last_name'))
        email_field.fill(data.get('email'))
        password_field.fill(data.get('password'))
        confirm_password_field.fill(data.get('password'))
        self.screenshot()
        btn_create_field.click()
        return fake_data_for_account

    @allure.step('Clik on button "Create an Account"')
    def click_button_create_account(self):
        btn_create_field = self.find(loc.btn_create_account)
        btn_create_field.click()
        self.screenshot()
