---
title: "Another detailed explanation of Python decorators"
date: 2013-01-04
categories:
  - Programming articles
---

# Another detailed explanation of Python decorators
There are a ton of guides on decorators out there and [ebooks](http://www.amazon.com/Guide-Learning-Python-Decorators-ebook/dp/B006ZHJSIM) that go into great depth.  Just [google it](https://www.google.com/search?q=python+decorators) for a huge listing of results, or skip to the what seems to be the [canonical reference](http://stackoverflow.com/questions/739654/understanding-python-decorators) on the topic.

I've read a lot of these over the years, but I recently read a newer [article](http://www.brianholdefehr.com/decorators-and-functional-python) that had a good tidbit on [closures](http://en.wikipedia.org/wiki/Closure_(computer_science)) and how these work in [Python](http://python.org):
> In Python, a closure provides full
> read access to any variable in the
> function's scope chain, but only
> provides write access to mutable
> objects (lists, dictionaries, etc.).

Remember, decorators can be a useful way to extend a method or functions use without modifying the function directly.  In fact, I've written about decorators and some common uses a few times:

 - [Decorating main](http://codrspace.com/durden/decorating-main/)
 - [Python can be evil](http://codrspace.com/durden/python-can-be-evil/)
 - [Profiling](http://codrspace.com/durden/quick-profiling-in-python/)