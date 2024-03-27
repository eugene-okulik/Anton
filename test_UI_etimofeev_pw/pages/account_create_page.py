from playwright.sync_api import expect

from test_UI_etimofeev_pw.pages.base_page import BasePage
from test_UI_etimofeev_pw.pages.locators.locators import AccountCreateLocators as Loc


class AccountCreatePage(BasePage):
    page_url = "/customer/account/create/"

    def fill_personal_information(self, first_name, last_name):
        first_name_field = self.find(Loc.FIRST_NAME_FIELD)
        first_name_field.fill(first_name)

        last_name_field = self.find(Loc.LAST_NAME_FIELD)
        last_name_field.fill(last_name)

    def fill_sign_in_information(self, email, password):
        email_field = self.find(Loc.EMAIL_FIELD)
        email_field.fill(email)

        password_field = self.find(Loc.PASSWORD_FILED)
        password_field.hover()
        password_field.click()
        password_field.fill(password)

        confirm_password = self.find(Loc.CONFIRM_PASSWORD_FIELD)
        confirm_password.fill(password)

    def press_create_account_button(self):
        self.find(Loc.CREATE_ACCOUNT_BUTTON).click()

    def check_strength_password(self):
        expected_strength = "Strong"
        base_strength = "No Password"

        expect(self.find(Loc.STRENGTH_PASSWORD)).not_to_have_text(base_strength)

        current_strength = self.find(Loc.STRENGTH_PASSWORD)
        expect(current_strength, "Strength isn't matched").to_contain_text(
            expected_strength
        )

    def check_created_account_message(self):
        message = "Thank you for registering with Main Website Store."

        expect(self.find(Loc.SUCCESS_MESSAGE)).to_be_visible()

        actual_message = self.find(Loc.SUCCESS_MESSAGE)
        expect(actual_message, "Text isn't contained").to_contain_text(message)

    def check_names(self, first_name, last_name):
        current_data = self.find(Loc.CONTENT_ELEMENT).first

        expect(current_data, "First name isn't matched").to_contain_text(first_name)
        expect(current_data, "Last name isn't matched").to_contain_text(last_name)
