'''Tests for Radio Buttons and DropDown boxes.'''
from websmith.actions import (
    Choose,
    FillForm,
    FindByName,
    FindByXPATH,
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

        assert FindByName('firstname').value == 'John'
        assert FindByName('lastname').value == 'Steinbeck'


def test_select_radio_button(browser, page):
    '''Select the "John Steinbeck" radio button'''
    with Session(browser):
        Go(page)
        Choose('writers', 'steinbeck')
        element = FindByXPATH(
            ('//input[contains(@type, "radio")'
             'and contains(@value, "steinbeck")]'))
        element.click()
        assert element.checked
        assert element.value == 'steinbeck'


def test_select_from_dropdown_by_value(browser, page):
    '''Select individual item from a web dropdown by its value.'''
    with Session(browser):
        Go(page)
        Select('writers', 'bradbury')
        assert FindByXPATH(
            '//option[contains(@value, "bradbury")]').checked


def test_select_from_dropdown_by_text(browser, page):
    '''Select individual item from a web dropdown by its text.'''
    with Session(browser):
        Go(page)
        Select('writers', 'John Steinbeck', True)
        assert FindByXPATH(
            '//option[contains(@value, "steinbeck")]').checked
