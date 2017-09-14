"""Foobar."""
from websmith.actions import Action


class Session(object):
    """A convenient object for working with Web UI elements."""

    def __init__(self, browser):
        """Base client for handling web ui elements."""
        self.browser = browser
        Action.browser = browser

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        delattr(Action, 'browser')
