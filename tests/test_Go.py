from websmith.actions import Go
from websmith.ui import Session


def searchEngine(url):
    Go(url)


def test_go_to_google(browser):
    with Session(browser) as session:  # noqa: F841
        searchEngine('https://www.google.com')
        assert browser.title == 'Google'


def test_go_to_duckduckgo(browser):
    with Session(browser) as session:  # noqa: F841
        searchEngine('https://www.duckduckgo.com')
        assert browser.title == 'DuckDuckGo'
