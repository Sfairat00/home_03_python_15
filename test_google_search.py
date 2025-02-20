import pytest
from selene import browser, be, have


@pytest.fixture(scope="session")
def browser_context():
    browser.config.window_height = 500
    browser.config.window_width = 500

@pytest.fixture(autouse=True)
def operation_browser():
    browser.open('https://google.com')
    yield
    browser.quit()

def test_valid_result():
    browser.element('[name="q"]').should(be.blank).type('yashka/selene').press_enter()
    browser.element('html').should(have.text('Об этой странице'))

def test_invalid_result():
    browser.element('[name="q"]').should(be.blank).type('ererrerrerer').press_enter()
    browser.element('html').should(have.no.text('ничего не найдено'))