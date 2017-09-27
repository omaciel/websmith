Websmith
--------

A Domain Specific Language (DSL) for Web UI Testing.

How To Use It
+++++++++++++

Assuming that you have a `WebDriver` browser object, then::

  from websmith.actions import Go, FindByValue, SendKeys
  from websmith.ui import Session

  with Session(browser):
      Go('https://www.google.com')
      SendKeys('q', 'WebSmith')
      FindByValue('Google Search').click()
