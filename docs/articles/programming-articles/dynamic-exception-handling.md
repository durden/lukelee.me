---
title: "Dynamic exception handling"
date: 2013-05-09
categories:
  - Programming articles
---

# Dynamic exception handling
I stumbled onto a [great lesson in Python exceptions](http://blog.codedstructure.net/2013/05/the-dynamics-of-catching-exceptions-in.html) today.

The article points out that exception handling in Python is very loose and dynamic.  It's a great read to understand what is possible with the dynamic nature of Exceptions.  For example, have you ever tried passing an Exception as an argument and then using that directly in your `except` statement?

<pre>
>>> def do_something():
...    blob
...
>>> def attempt(action, ignore_spec):
...     try:
...         action()
...     except ignore_spec:
...         pass
...
>>> attempt(do_something, ignore_spec=(NameError, TypeError))
>>> attempt(do_something, ignore_spec=TypeError)
Traceback (most recent call last):
  ...
NameError: global name 'blob' is not defined
</pre>

I don't know that I've ever tried that before, but it could be useful.