import time

from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class UIError(Exception):
    """Indicates that a UI action could not be done."""


class UINoSuchElementError(UIError):
    """Indicates that UI Element is not found."""


def ajax_complete(browser):
    """Checks whether an ajax call is completed."""

    jquery_active = False
    angular_active = False

    try:
        jquery_active = browser.execute_script('return jQuery.active') > 0
    except WebDriverException:
        pass

    try:
        angular_active = browser.execute_script(
            'return angular.element(document).injector().get("$http")'
            '.pendingRequests.length') > 0
    except WebDriverException:
        pass

    return not (jquery_active or angular_active)


def choose(browser, name, value):
    '''Select a radio button by value.

    Example:
        >>> choose('author', 'steinbeck')
    '''
    locator = (
        By.XPATH,
        '//input[contains(@type, "radio") and contains(@name, "{}")]'.format(
            name))
    elements = find_elements(browser, locator)
    for element in elements:
        if element.get_attribute('value') == value:
            element.click()


def fill_form(browser, field_values):
    '''Fill out a web form with values.

    Borrowed from https://github.com/cobrateam/splinter

    Example:

        >>> fill_form({'q': 'websmoth'})
        >>> fill_form({
                'name': 'John Steinbeck',
                'writer': True,
            })
    '''
    for name, value in field_values.items():
        locator = (By.NAME, name)
        element = wait_until_element_exists(browser, locator)
        if (
                element.get_attribute('type') in ['text', 'password'] or
                element.get_attribute('tag_name') == 'textarea'):
            element.send_keys(value)
        elif element.get_attribute('type') == 'checkbox':
            if value:
                element.check()
            else:
                element.uncheck()
        elif element.get_attribute('type') == 'radio':
            choose(browser, name, value)
        elif element.get_attribute('tag_name') == 'select':
            element.select(value)
        else:
            element.value = value


def find_element(browser, locator):
    '''Locate a web element.

    Example:
        >>> find_element((By.ID, 'lst-ib'))
    '''
    return browser.find_element(*locator)
    #  return wait_for_element(browser, locator)


def find_elements(browser, locator):
    '''Locate a web element.

    Example:
        >>> find_elements((By.TAG_NAME, 'select'))
    '''
    return browser.find_elements(*locator)


def perform_action_chain_move(browser, locator):
    """Moving the mouse to the middle of an element specified by locator
    parameter
    :param locator: The locator that describes the element.
    :raise: UINoSuchElementError if the element could not be found.
    """
    element = wait_until_element(browser, locator)
    if element is None:
        raise UINoSuchElementError(
            'Cannot move cursor to element with locator {}'
            .format(locator)
        )
    scroll_into_view(browser, element)
    ActionChains(browser).move_to_element(element).perform()
    wait_for_ajax(browser)


def select(browser, name, value, by_text=False):
    '''Select a radio button by value.

    Example:
        >>> select('author', 'steinbeck')
    '''
    locator = (
        By.XPATH,
        '//select[contains(@name, "{}")]/option[{}]'.format(
            name,
            ('text()="{}"'.format(value)
             if by_text
             else 'contains(@value, "{}")'.format(value)),
        ))
    find_element(browser, locator).click()


def scroll_page(browser):
    """Scroll web page up."""
    browser.execute_script('scroll(350, 0);')


def scroll_right_pane(browser):
    """Scroll right pane down to find the save/submit button."""
    browser.execute_script(
        "$('#panel_main').data('jsp').scrollBy(0, 100);")


def scroll_into_view(browser, element):
    """ Scrolls current element into visible area of the browser window."""
    # Here aligntoTop=False option is set.
    browser.execute_script(
        'arguments[0].scrollIntoView(false);',
        element,
    )


def wait_for_ajax(browser, timeout=30, poll_frequency=0.5):
    """Waits for an ajax call to complete until timeout."""
    WebDriverWait(
        browser, timeout, poll_frequency
    ).until(
        ajax_complete, 'Timeout waiting for page to load'
    )


def wait_for_element(browser, locator, timeout=12, poll_frequency=0.5):
    '''
    '''
    try:
        element = WebDriverWait(
            browser, timeout, poll_frequency).until(
                expected_conditions.presence_of_element_located(locator),
                message='Element {} could not be found.'.format(locator[1]))
        wait_for_ajax(browser, poll_frequency=poll_frequency)
        return element
    except TimeoutException as err:
        print(
            '{}: Waiting for element "{}" to display. {}'.format(
                type(err).__name__,
                locator[1],
                err
            ))
        return None


def wait_until_element(browser, locator, timeout=12, poll_frequency=0.5):
    """Wrapper around Selenium's WebDriver that allows you to pause your
    test until an element in the web page is present and visible.
    """
    try:
        element = WebDriverWait(
            browser, timeout, poll_frequency
        ).until(
            expected_conditions.visibility_of_element_located(locator),
            message='Element {} is not visible.'.format(locator[1])
        )
        wait_for_ajax(browser, poll_frequency=poll_frequency)
        return element
    except TimeoutException as err:
        print(
            '{}: Waiting for element "{}" to display. {}'.format(
                type(err).__name__,
                locator[1],
                err
            ))
        return None


def wait_until_element_exists(
        browser,
        locator,
        timeout=12,
        poll_frequency=0.5):
    """Wrapper around Selenium's WebDriver that allows you to pause your
    test until an element in the web page is present.
    """
    try:
        element = WebDriverWait(
            browser, timeout, poll_frequency
        ).until(
            expected_conditions.presence_of_element_located(locator),
            message='Element {} is not present'.format(locator[1])
        )
        wait_for_ajax(browser, poll_frequency=poll_frequency)
        return element
    except TimeoutException as err:
        print(
            '{}: Waiting for element "{}" to become visible. {}'.format(
                type(err).__name__,
                locator[1],
                err
            ))
        return None
