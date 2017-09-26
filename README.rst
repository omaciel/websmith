Websmith
--------

A Domain Specific Language (DSL) for Web Testing.

How To Use It
+++++++++++++

Assuming that you have a `WebDriver` browser object, then::

  from websmith.actions import Go, SendKeys
  from websmith.ui import Session

  with Session(browser):
      Go('https://www.google.com')
      SendKeys('q', 'WebSmith')
