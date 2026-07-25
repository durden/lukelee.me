---
title: "Numpy performance tricks"
date: 2014-03-24
categories:
  - Programming articles
---

# Numpy performance tricks
Here's a [short and to the point article on numpy performance tricks](http://cyrille.rossant.net/numpy-performance-tricks/).

I'd suggest a quick glance through your code even if you think you know better.  I found a few places in my code where I used Python's `max()` function instead of the built-in method on a numpy array.  These are easy to spot and quick to fix.