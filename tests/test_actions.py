from selenium.webdriver.common.by import By

from websmith.actions import Choose, Find, Fill, Go
from websmith.ui import Session


def test_go_to_page(browser, page):
    with Session(browser) as session:  # noqa: F841
        Go(page)
        assert browser.title == 'WebSmith'


def test_fill_form(browser, page):
    '''Foo'''
    with Session(browser) as session:  # noqa: F841
        Go(page)
        Fill({'firstname': 'John', 'lastname': 'Steinbeck'})


def test_select_first_radio_button(browser, page):
    '''Foo'''
    with Session(browser) as session:  # noqa: F841
        Go(page)
        Choose('author', 'steinbeck')
        element = Find((
            By.XPATH,
            '//input[contains(@value, "steinbeck")]'
        )).element
        element.click()
        assert element.is_selected()
        assert element.get_attribute('value') == 'steinbeck'
