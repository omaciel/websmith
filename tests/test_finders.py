'''Tests for finding web elements.'''
from websmith.actions import (
    FindByCSS,
    FindByID,
    FindByName,
    FindByTag,
    FindByText,
    FindByValue,
    FindByXPATH,
    Go,
)
from websmith.ui import Session


def test_find_by_css(browser, page):
    '''Find web elements by its css attribute.'''
    with Session(browser):
        Go(page)
        elements = FindByCSS('li')

        for element in elements:
            assert element.tag_name == 'li'


def test_find_by_id(browser, page):
    '''Find web elements by its id.'''
    with Session(browser):
        Go(page)
        assert FindByID('login').tag_name == 'form'


def test_find_by_name(browser, page):
    '''Find web elements by its name.'''
    with Session(browser):
        Go(page)
        assert FindByName('firstname').tag_name == 'input'


def test_find_by_tag(browser, page):
    '''Find web elements by its tag.'''
    with Session(browser):
        Go(page)
        elements = FindByTag('li')

        for element in elements:
            assert element.tag_name == 'li'


def test_find_by_text(browser, page):
    '''Find web elements by its text.'''
    with Session(browser):
        Go(page)
        elements = FindByText('John Steinbeck')

        for element in elements:
            assert element.text == 'John Steinbeck'


def test_find_by_value(browser, page):
    '''Find web elements by its value.'''
    with Session(browser):
        Go(page)
        elements = FindByValue('steinbeck')

        for element in elements:
            assert element.value == 'steinbeck'


def test_find_by_xpath(browser, page):
    '''Find web element by its XPATH.'''
    with Session(browser):
        Go(page)
        element = FindByXPATH(
            ('//input[contains(@type, "radio")'
             'and contains(@value, "steinbeck")]'))
        assert element.checked is not True
        assert element.value == 'steinbeck'
