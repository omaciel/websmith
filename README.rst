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

What if you speak a language other than English?
Let's inspect the `Google Search` button::

  <input class="gNO89b" value="Google Search" name="btnK" type="submit" ...>

We can find the button by the attribute `name` with ``FindByName('btnK')`` or
by the CSS `class` with ``FindByCSS('input.gNO89b')``.

How To Get A WebDriver Object?
++++++++++++++++++++++++++++++

Say you want to control Firefox::

  from selenium import webdriver
  browser = webdriver.Firefox()
