import pytest
from selene import browser, be, have


@pytest.fixture(scope="session")
def browser_context():
    browser.config.window_height = 900
    browser.config.window_width = 900


@pytest.fixture(autouse=True)
def operation_browser():
    browser.open('https://google.com')
    yield
    browser.quit()


def test_valid_result(browser_context):
    browser.element('[name="q"]').should(be.blank).type('yashka/selene').press_enter()
    browser.element('html').should(have.text('Об этой странице'))


def test_invalid_result(browser_context):
    browser.element('[name="q"]').should(be.blank).type('ererrerrererенкенепвап').press_enter()
    browser.element('html').should(have.text('По запросу ererrerrererенкенепвап ничего не найдено.'))
