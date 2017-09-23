"""Implements VERB-like objects that allow interction with DOM elements."""
import logging
import threading


logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)


class Action(object):
    '''Base class for all web actions.'''
    data = threading.local()
    elements = []

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


def Find(finder, locator):
    '''Find a web element by using a finder type.

    The supported `finder` types are:
    * 'find_by_css'
    * 'find_by_xpath'
    * 'find_by_name'
    * 'find_by_tag'
    * 'find_by_value'
    * 'find_by_text'
    * 'find_by_id'

    Example:

    >>> Find('find_by_id', '')
    [<splinter.driver.webdriver.WebDriverElement at 0x1072b9a90>]
    '''
    browser = Action.browser

    func = getattr(browser, finder)
    return func(locator)


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


def SendKeys(value, slowly=False):
    '''Send value to a web element that can receive text input.

    Example:

    >>> SendKeys((By.ID, 'lst-ib'), 'WebSmith')
    '''
    browser = Action.browser

    return browser.type(value, slowly)


def Uncheck(name):
    '''Mark a checkbox as checked.

    Example:

    >>> Uncheck('some-check-box')
    '''
    browser = Action.browser

    return browser.uncheck(name)
