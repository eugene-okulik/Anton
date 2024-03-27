import pytest
from playwright.sync_api import BrowserContext


@pytest.fixture()
def page(context: BrowserContext, playwright):
    playwright.selectors.set_test_id_attribute("id")
    page = context.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})
    return page
