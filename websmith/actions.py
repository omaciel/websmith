"""Implements VERB-like objects that allow interction with DOM elements."""
import logging
import threading

from websmith.utils import (
    choose,
    fill_form,
    find_element,
    find_elements,
    perform_action_chain_move,
    select,
    wait_until_element_exists,
)

from selenium.webdriver.common.by import By


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


class Check(Action):
    '''Mark a checkbox as checked.

    Borrowed from https://github.com/cobrateam/splinter

    Example:
        >>> Check('some-check-box')
    '''

    def __init__(self, name):
        self.name = name

        super(Check, self).__init__()

    def _run(self):
        locator = (By.NAME, self.name)
        element = wait_until_element_exists(self.browser, locator)
        element.check()


class Choose(Action):
    '''Mark a radiobox as checked.

    Borrowed from https://github.com/cobrateam/splinter

    Example:
        >>> Choose('some-radiobox-name', 'some-radiobutton-value')
    '''

    def __init__(self, name, value):
        self.name = name
        self.value = value

        super(Choose, self).__init__()

    def _run(self):
        choose(self.browser, self.name, self.value)


class Click(Action):
    '''Click a web element.

    Example:
        >>> Click((By.NAME, 'commit'))
    '''
    def __init__(self, target):
        self.target = target

        super(Click, self).__init__()

    def _run(self):
        wait_until_element_exists(self.browser, self.target).click()


class Fill(Action):
    '''Fill a web element (by its name) with a value.

    Example:
        >>> Fill({'some-text-box': 'some value'})
        >>> Fill({'some-check-box': True})
        >>> Fill({'some-select-field': 'some-choice'})

    You can also fill out an entire form:
        >>> Fill({
                'name': 'John Steinbeck',
                'writer': True,
            })
    '''
    def __init__(self, field_values):
        self.field_values = field_values

        super(Fill, self).__init__()

    def _run(self):
        fill_form(self.browser, self.field_values)


class Find(Action):
    '''Find a web element.
    '''

    def __init__(self, locator):
        self.locator = locator

        super(Find, self).__init__()

    def _run(self):
        self.element = find_element(self.browser, self.locator)


class Hover(Action):
    '''Move and hover the mouse focus to a web element.

    Example:
        >>> Hover((By.ID, 'account_name'))
    '''
    def __init__(self, target):
        self.target = target

        super(Hover, self).__init__()

    def _run(self):
        perform_action_chain_move(self.browser, self.target)


class Go(Action):
    '''Load URL in the web browser.

    Example:
        >>> Go('https://www.google.com')
    '''
    def __init__(self, url):
        self.url = url

        super(Go, self).__init__()

    def _run(self):
        self.browser.get(self.url)


class Select(Action):
    '''Select a choice from a list of web elements.

    Borrowed from https://github.com/cobrateam/splinter

    Example:
        >>> Select('some-choice-list', 'some-choice-value')
        >>> Select('some-choice-list', 'some-choice-text', True)
    '''
    def __init__(self, name, value, by_text=False):
        self.name = name
        self.value = value
        self.by_text = by_text

        super(Select, self).__init__()

    def _run(self):
        select(self.browser, self.name, self.value, self.by_text)


class SendKeys(Action):
    '''Send value to a web element that can receive text input.

    Example:
        >>> SendKeys((By.ID, 'lst-ib'), 'WebSmith')
    '''
    def __init__(self, target, value):
        self.target = target
        self.value = value

        super(SendKeys, self).__init__()

    def _run(self):
        element = wait_until_element_exists(self.browser, self.target)
        element.send_keys(self.value)


class Uncheck(Action):
    '''Mark a checkbox as unchecked.

    Borrowed from https://github.com/cobrateam/splinter

    Example:
        >>> Uncheck('some-check-box')
    '''

    def __init__(self, name):
        self.name = name

        super(Uncheck, self).__init__()

    def _run(self):
        locator = (By.NAME, self.name)
        element = wait_until_element_exists(self.browser, locator)
        element.uncheck()


class Wait(Action):
    '''Wait for a web element to become available.

    Raise a TimeoutException is element is not found.

    Example:
        >>> Wait((By.ID, 'lst-ib'))
    '''
    def __init__(self, target):
        self.target = target

        super(Wait, self).__init__()

    def _run(self):
        self.element = wait_until_element_exists(self.browser, self.target)


class WaitAndClick(Action):
    '''Wait for a web element to become available and click it.

    Example:
        >>> WaitAndClick((By.NAME, 'commit'))
    '''
    def __init__(self, target):
        self.target = target

        super(WaitAndClick, self).__init__()

    def _run(self):
        wait_until_element_exists(self.browser, self.target).click()
