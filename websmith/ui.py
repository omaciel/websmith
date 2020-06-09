"""Browser and UI Elements."""
from splinter.driver.webdriver import BaseWebDriver, WebDriverElement
from splinter.driver.webdriver.cookie_manager import CookieManager

from websmith.actions import Action


class WebDriver(BaseWebDriver):
    """Wrapper for Splinter BaseWebDriver that accepts a real Selenium
    webdriver instance.
    """
    def __init__(self, browser, wait_time=2):
        self.driver = browser
        self.element_class = WebDriverElement
        self._cookie_manager = CookieManager(self.driver)
        super(WebDriver, self).__init__(wait_time)


class Session(object):
    """A convenient object for working with Web UI elements."""

    def __init__(self, browser):
        """Base client for handling web ui elements."""
        self.browser = WebDriver(browser)
        Action.browser = self.browser

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        delattr(Action, 'browser')
