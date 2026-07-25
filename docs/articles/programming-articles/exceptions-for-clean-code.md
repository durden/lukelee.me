---
title: "Exceptions for clean code"
date: 2013-02-11
categories:
  - Programming articles
---

# Exceptions for clean code
I found this [great article on Python exceptions](http://www.jeffknupp.com/blog/2013/02/06/write-cleaner-python-use-exceptions/).  The article spends a good amount of time discussing performance, but the most important part to me was the realization that [Python](http://python.org) uses exceptions in a variety of [atypical places](http://docs.python.org/2/library/exceptions.html#exceptions.StopIteration).

> Many programmers have had it drilled
> into their head that exceptions, in
> any language, should only be used in
> truly exceptional cases. They're
> wrong. The Python community's approach
> to exceptions leads to cleaner code
> that's easier to read.