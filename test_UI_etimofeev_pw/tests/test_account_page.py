from faker import Faker

from test_UI_etimofeev_pw.pages.account_create_page import AccountCreatePage


def test_button(page):
    fake = Faker()
    email = fake.email()
    first_name = fake.first_name()
    last_name = fake.last_name()
    password = "1234QQqqqq"

    account_page = AccountCreatePage(page)
    account_page.open()
    account_page.fill_personal_information(first_name=first_name, last_name=last_name)
    account_page.fill_sign_in_information(email=email, password=password)
    account_page.check_strength_password()
    account_page.press_create_account_button()
    account_page.check_created_account_message()
    account_page.check_names(first_name=first_name, last_name=last_name)
