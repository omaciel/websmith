from selenium.webdriver.common.by import By

from websmith.actions import Go, SendKeys, Wait
from websmith.ui import Session


GOOGLE_SEARCH_BOX = (By.ID, 'lst-ib')


def searchEngine(url):
    Go(url)


def test_go_to_google(browser):
    with Session(browser) as session:  # noqa: F841
        searchEngine('https://www.google.com')
        assert browser.title == 'Google'
        element = Wait(GOOGLE_SEARCH_BOX)
        assert element is not None
        SendKeys(GOOGLE_SEARCH_BOX, 'Og Maciel')


def test_go_to_duckduckgo(browser):
    with Session(browser) as session:  # noqa: F841
        searchEngine('https://www.duckduckgo.com')
        assert browser.title == 'DuckDuckGo'
