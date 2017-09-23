from websmith.actions import (
    Choose,
    FillForm,
    Find,
    Go,
    Select,
)
from websmith.ui import Session


def test_go_to_page(browser, page):
    with Session(browser):
        Go(page)
        assert browser.title == 'WebSmith'


def test_fill_form(browser, page):
    '''Fill out form with values.'''
    with Session(browser):
        Go(page)
        FillForm({'firstname': 'John', 'lastname': 'Steinbeck'})

        assert Find('find_by_name', 'firstname').value == 'John'
        assert Find('find_by_name', 'lastname').value == 'Steinbeck'


def test_select_first_radio_button(browser, page):
    '''Select the "John Steinbeck" radio button'''
    with Session(browser):
        Go(page)
        Choose('writers', 'steinbeck')
        element = Find(
            'find_by_xpath',
            ('//input[contains(@type, "radio")'
             'and contains(@value, "steinbeck")]'))
        assert element.checked
        assert element.value == 'steinbeck'


def test_select_from_dropdown_by_value(browser, page):
    '''Select individual item from a web dropdown by its value.'''
    with Session(browser):
        Go(page)
        Select('writers', 'bradbury')
        assert Find(
            'find_by_xpath',
            '//option[contains(@value, "bradbury")]').checked


def test_select_from_dropdown_by_text(browser, page):
    '''Select individual item from a web dropdown by its text.'''
    with Session(browser):
        Go(page)
        Select('writers', 'John Steinbeck', True)
        assert Find(
            'find_by_xpath',
            '//option[contains(@value, "steinbeck")]').checked
