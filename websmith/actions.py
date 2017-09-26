"""Implements VERB-like objects that allow interction with DOM elements."""
import logging
import threading


logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)


class Action(object):
    '''Base class for all web actions.'''
    data = threading.local()

    def __init__(self):
        LOGGER.info('ACTION: {} on {}'.format(
            self.__class__.__name__,
            self.__dict__
        ))
        self._run()

    def _run(self):
        raise NotImplementedError()


def Check(name):
    '''Mark a checkbox as checked.

    Example:

    >>> Check('some-check-box')
    '''
    browser = Action.browser

    return browser.check(name)


def Choose(name, value):
    '''Mark a radiobox as checked.

    Borrowed from https://github.com/cobrateam/splinter

    Example:

    >>> Choose('some-radiobox-name', 'some-radiobutton-value')
    '''
    browser = Action.browser

    browser.choose(name, value)


def Click(element):
    '''Executes a 'click' on a web element.

    There is no real need to call this `Click` method, since most web elements
    returned by all other methods should already expose its own `click` method,
    but this is made available for more verbose, explicitly calls.

    Example:

    >>> Find(
    '''
    element.click()


def Fill(name, value):
    '''Fill a web element (by its name) with a value.

    Example:

    >>> Fill({'some-text-box': 'some value'})
    >>> Fill({'some-check-box': True})
    >>> Fill({'some-select-field': 'some-choice'})
    '''
    browser = Action.browser

    browser.fill(name, value)


def FillForm(field_values):
    '''Fill a web form.

    Fills a web form, filling each field with its corresponding value as
    provided by the dictionary `field_values`, where its `keys` provide the
    `name` for a field in the form, and its values are used to populate it.

    Example:

    >>> FillForm({
    ...    'some-text-box': 'some value',
    ...    'some-check-box': True,
    ...    'some-select-field': 'some-choice'})
    '''
    browser = Action.browser

    browser.fill_form(field_values)


def FindByCSS(css):
    '''Find a web element by using its CSS attribute.

    Example:

    >>> FindByCSS('h1')
    '''
    browser = Action.browser

    return browser.find_by_css(css)


def FindByXPATH(xpath):
    '''Find a web element by using its XPATH.

    Example:

    >>> FindByXPATH('//input')
    '''
    browser = Action.browser

    return browser.find_by_xpath(xpath)


def FindByTag(tag):
    '''Find a web element by using its tag.

    Example:

    >>> FindByTag('input')
    '''
    browser = Action.browser

    return browser.find_by_tag(tag)


def FindByName(name):
    '''Find a web element by using its name.

    Example:

    >>> FindByName('name')
    '''
    browser = Action.browser

    return browser.find_by_name(name)


def FindByText(text):
    '''Find a web element by using its text attribute.

    Example:

    >>> FindByText('John Steinbeck')
    '''
    browser = Action.browser

    return browser.find_by_text(text)


def FindByID(ID):
    '''Find a web element by using its ID.

    Example:

    >>> FindByID('first-column')
    '''
    browser = Action.browser

    return browser.find_by_id(ID)


def FindByValue(value):
    '''Find a web element by using its value.

    Example:

    >>> FindByValue('steinbeck')
    '''
    browser = Action.browser

    return browser.find_by_value(value)


def LinkByHREF(href):
    '''Find a link by using its HREF value.

    Example:

    >>> LinkByHREF('http://example.com')
    '''
    browser = Action.browser

    return browser.find_link_by_href(href)


def LinkByPartialHREF(href):
    '''Find a link by using its partial HREF value.

    Example:

    >>> LinkByPartialHREF('example')
    '''
    browser = Action.browser

    return browser.find_link_by_partial_href(href)


def LinkByPartialText(text):
    '''Find a link by using its partial text value.

    Example:

    >>> LinkByPartialText('example')
    '''
    browser = Action.browser

    return browser.find_link_by_partial_text(text)


def LinkByText(text):
    '''Find a link by using its text value.

    Example:

    >>> LinkByText('example')
    '''
    browser = Action.browser

    return browser.find_link_by_text(text)


def Go(URL):
    '''Load URL in the web browser.

    Example:

    >>> Go('https://www.google.com')
    '''
    browser = Action.browser

    browser.visit(URL)


def Hover(element):
    '''Move and hover the mouse focus to a web element.

    Example:

    >>> Hover(element)
    '''
    element.mouse_over()


def Select(name, value, by_text=False):
    '''Select a choice from a list of web elements.

    Example:

    >>> Select('some-dropdown', 'some-choice-value')
    >>> Select('some-dropdown','some-choice-text', True)
    '''
    browser = Action.browser

    if by_text is True:
        return browser.select_by_text(name, value)
    else:
        return browser.select(name, value)


def SendKeys(name, value, slowly=False):
    '''Send value to a web element that can receive text input.

    Example:

    >>> SendKeys('q', 'WebSmith')
    '''
    browser = Action.browser

    return browser.type(name, value, slowly)


def Uncheck(name):
    '''Mark a checkbox as checked.

    Example:

    >>> Uncheck('some-check-box')
    '''
    browser = Action.browser

    return browser.uncheck(name)
