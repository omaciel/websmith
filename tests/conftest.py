import os

import pytest

from selenium import webdriver


@pytest.yield_fixture(scope='function')
def browser(request):
    """Fixture to create a web browser."""
    browser = webdriver.Chrome()

    def close_browser():
        """Handle closing browser object."""
        browser.quit()
    request.addfinalizer(close_browser)

    return browser


@pytest.fixture(scope='session')
def page(request):
    '''Fixture to provide a testable web page.'''
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return '{}{}{}'.format('file://', dir_path, '/data/page.html')
