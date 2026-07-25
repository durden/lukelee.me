---
title: "Partial Function Application in Python"
date: 2013-12-04
categories:
  - Programming articles
---

# Partial Function Application in Python
Spend a few minutes and read this great article on [partial function application in Python](http://tech.pro/tutorial/1520/partial-function-application-in-python).

I've used `partial` quite a bit in the past when dealing with `map` as the author discusses.  In addition, I've used `partial` in situations where it leads to more readable function calls, especially with calls that have lots of optional arguments.  Here's a good example from my own usage of [matplotlib](http://matplotlib.org) and the [subtitle method](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.suptitle):

[https://gist.github.com/durden/7788315](https://gist.github.com/durden/7788315)

It's much more readable to call `set_title` all over a module than the cumbersome and error-prone `suptitle` method with its' myriad of optional arguments.  You can also decrease duplicated code and lock-down arguments by using partial functions in this way.

Finally, here's something about partial functions that [Christian Schramm](http://tech.pro/chms) taught me in his [excellent article](http://tech.pro/tutorial/1520/partial-function-application-in-python):

> So there we have one very practical
> advantage of using the partial
> function [from] functools over our own
> wrapper: We avoid constructing (and
> destructing) another stack frame,
> which is a costly thing to do if done
> very often (read: It's slow). Now we
> all know about how “premature
> optimization is the root of all evil”,
> but using the partial function is
> typically not much an effort, really.
> If the partial version is no more
> complicated than a wrapper, we might
> as well use it.