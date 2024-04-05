import allure
import inspect
from playwright.sync_api import Page, expect, Dialog, Locator
from test_UI_asklepkovich_pw.pages.locators import create_account_locators as loc
from test_UI_asklepkovich_pw.pages.locators import eco_friendly_locators as loc_eco
from allure_commons.types import AttachmentType


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None
    title = None
    info = None
    more_icon = None

    def __init__(self, page: Page):
        self.page = page


    @staticmethod
    def assert_check(act_result, exp_result, message):
        stack = inspect.stack()
        name_function = stack[1].function
        print(f'Start checking: {name_function}')
        print(f'Actual result= {act_result}\n')
        print(f'Expected result= {exp_result}\n')
        assert act_result == exp_result, f'\n{message}\n' \
                                         f'Actual_result = {act_result}\n' \
                                         f'Expected_result = {exp_result}\n' \
                                         f'Done checking: {name_function}\n'
        print(f'Done checking: {name_function}\n')


    def wait_full_to_load(self):
        welcome = self.find(loc_eco.welcome).first
        return expect(welcome).not_to_be_empty()


    @allure.step('Open page for test ')
    def open_page(self, delete_cookies=None):
        if self.page_url:
            if delete_cookies:
                self.page.context.clear_cookies()
            self.page.goto(f'{self.base_url}{self.page_url}')
            self.wait_full_to_load()
            # self.screenshot()
        else:
            raise NotImplementedError('Page can not be opened for this page class')


    def find(self, locator: str) -> Locator:
        return self.page.locator(locator)


    @allure.step('Checking message in alert')
    def check_alert_text(self, text):
        self.wait_full_to_load()
        expect(self.find(loc.alert)).to_have_text(text)


    @allure.step('Checking error message for field')
    def check_error_message(self, field, exp_error):
        match field:
            case 'first_name':
                first_name_error = self.find(loc.first_name_error)
                self.assert_check(
                    first_name_error.text_content(), exp_error, f'Error check {field}'
                )
            case 'last_name':
                last_name_error = self.find(loc.last_name_error)
                self.assert_check(
                    last_name_error.text_content(), exp_error, f'Error check {field}'
                )
            case 'email':
                email_field_error = self.find(loc.email_error)
                self.assert_check(
                    email_field_error.text_content(), exp_error, f'Error check {field}'
                )
            case 'email':
                email_field_error = self.find(loc.email_error)
                self.assert_check(
                    email_field_error.text_content(), exp_error, f'Error check {field}'
                )
            case 'password_':
                password_field_error = self.find(loc.password_error)
                self.assert_check(
                    password_field_error.text_content(), exp_error, f'Error check {field}'
                )
            case 'confirm_password':
                confirm_password_field = self.find(loc.confirm_password_error)
                self.assert_check(
                    confirm_password_field.text_content(), exp_error, f'Error check {field}'
                )


    def check_title(self, exp_title):
        self.assert_check(self.title, exp_title, 'Error check title\n')


    def check_info(self, exp_info):
        self.assert_check(self.info, exp_info, 'Error check info\n')


    def check_more_icon(self, exp_more_icon):
        self.assert_check(self.more_icon, exp_more_icon, 'Error check more icon\n')


    @allure.step('Screenshot')
    def screenshot(self, file_name='screenshot.png'):
        allure.attach(self.page.screenshot(path=file_name), name=file_name, attachment_type=AttachmentType.PNG)