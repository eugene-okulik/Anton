import pytest
import allure


@allure.feature('Test ui')
@allure.story('Test create account')
@allure.title('Test create new account with all correct fields')
def test_create_new_account_with_all_correct_fields(create_account, start_end):
    create_account.open_page()
    create_account.fill_all_form()
    create_account.check_alert_text('Thank you for registering with Main Website Store.')


@allure.feature('Test ui')
@allure.story('Test create account with old account')
@allure.title('Test create create account with old account')
@pytest.mark.regression
def test_create_account_with_old_account(create_account, create_new_account, start_end):
    old_data = create_new_account
    create_account.open_page(delete_cookies=True)
    create_account.fill_all_form(old_data)
    create_account.check_alert_text(
        'There is already an account with this email address. '
        'If you are sure that it is your email address, click here to get your password and access your account.'
    )


@allure.feature('Test ui')
@allure.story('Test create account with empty all fields')
@allure.title('Test create account with empty all fields')
@pytest.mark.smoke
def test_create_account_with_empty_all_fields(create_account, start_end):
    required_field = 'This is a required field.'
    create_account.open_page()
    create_account.click_button_create_account()
    create_account.check_error_message('first_name', required_field)
    create_account.check_error_message('last_name', required_field)
    create_account.check_error_message('email', required_field)
    create_account.check_error_message('password', required_field)
    create_account.check_error_message('confirm_password', required_field)
