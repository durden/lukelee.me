---
title: "Using __init__.py to enforce import order"
date: 2015-06-26
categories:
  - Programming articles
---

# Using __init__.py to enforce import order
Take a few minutes on your Friday to read this article on [simple rules for building great Python packages](http://axialcorps.com/2013/08/29/5-simple-rules-for-building-great-python-packages/).

It's never dawned on me the usefulness of using `__init__.py` to enforce the import order of submodules. You might be able to even use this tactic to avoid [circular dependencies](https://en.wikipedia.org/wiki/Circular_dependency) in a cleaner way than imports inside functions, etc.