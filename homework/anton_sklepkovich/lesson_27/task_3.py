from playwright.sync_api import Page, expect


def test_red_button(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    button = page.locator('#colorChange')
    expect(button).to_have_css('color', 'rgb(220, 53, 69)')
    button.click()
