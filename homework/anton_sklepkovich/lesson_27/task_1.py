from playwright.sync_api import Page, expect


def test_find_select(page: Page):
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    page.on('dialog', lambda dialog: dialog.accept())
    page.locator('.a-button').click()
    result = page.locator('#result-text')
    expect(result).to_have_text('Ok')
