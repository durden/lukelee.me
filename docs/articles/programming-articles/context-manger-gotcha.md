---
title: "Context Manger Gotcha"
date: 2012-05-24
categories:
  - Programming articles
---

# Context Manger Gotcha
Context managers are pretty useful when doing an action that involves something of the form:

    resource = get_resource()
    step1()
    step2()
    step3()
    release_resource(resource)

A few places come to mind:

1. Showing a progress dialog

2. Semaphores/mutex

3. Open/close file

4. Memory allocation/free

Granted some of these, namely #2 and #4, don't show up a lot in Python.  However, writing your own context manager can be useful.  I've used them several times for #1 above.

Writing a context manager is really easy.  Essentially just implement __enter__ and __exit__ to a class and use the 'with' keyword to implicitly invoke them. However, there is one caveat to keep in mind, the return value of __exit__.

There are three required arguments to __exit__ that are either all None or contain information about an exception that was raised inside the 'with' block. Your __exit__ method shouldn't re-raise this exception.  Instead, __exit__ should return ﻿True﻿ if you can handle the exception and do ﻿not﻿ wish to have it actually raised.  However, if you return False﻿ then the exception will get automatically raised once __exit__ is completed.

So make sure to always add a return value to your __exit__ methods!

Here's a small list of useful links on context managers:

 - [contextlib](http://www.doughellmann.com/PyMOTW/contextlib)

 - [Linuxtopia](http://www.linuxtopia.org/online_books/programming_books/python_programming/python_ch27s03.html)

 - [Python docs](http://docs.python.org/reference/datamodel.html#with-statement-context-managers)