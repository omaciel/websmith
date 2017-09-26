'''Tests for finding web link elements.'''
from websmith.actions import (
    LinkByHREF,
    LinkByPartialHREF,
    LinkByPartialText,
    LinkByText,
    Go,
)
from websmith.ui import Session


def test_link_by_href(browser, page):
    '''Find web link elements by its href attribute.'''
    with Session(browser):
        Go(page)
        element = LinkByHREF('https://github.com/omaciel/websmith')
        assert element.tag_name == 'a'
        assert element.value == 'WebSmith'


def test_link_by_partial_href(browser, page):
    '''Find web link elements by its partial href attribute.'''
    with Session(browser):
        Go(page)
        element = LinkByPartialHREF('Bradbury')
        assert element.tag_name == 'a'
        assert element.value == 'Ray Bradbury'


def test_link_by_partial_text(browser, page):
    '''Find web link elements by its partial text value.'''
    with Session(browser):
        Go(page)
        element = LinkByPartialText('John')
        assert element.tag_name == 'a'
        assert element.value == 'John Steinbeck'


def test_link_by_text(browser, page):
    '''Find web link elements by its href attribute.'''
    with Session(browser):
        Go(page)
        element = LinkByText('WebSmith')
        assert element.tag_name == 'a'
        assert element.value == 'WebSmith'
