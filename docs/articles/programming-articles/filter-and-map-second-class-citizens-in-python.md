---
title: "Filter and Map: Second-class citizens in Python?"
date: 2012-08-09
categories:
  - Programming articles
---

# Filter and Map: Second-class citizens in Python?
I tend to use [Pylint](http://www.logilab.org/857/) quite a bit in my development process.  I recently stumbled on [Warning 141](http://pylint-messages.wikidot.com/messages:w0141), which complains about continued usage of the [filter](http://docs.python.org/library/functions.html#filter) function.

I thought this was a bit odd, but it [turns out](http://stackoverflow.com/a/3013722/1108031) that [Guido](http://www.python.org/~guido/) himself lobbied unsuccessfully to have [filter](http://docs.python.org/library/functions.html#filter) and [map](http://docs.python.org/library/functions.html#map) removed from [Python 3](http://docs.python.org/py3k/).

I realize you can easily replace the usage of both of these functions with [list comprehensions](http://docs.python.org/tutorial/datastructures.html#list-comprehensions).  However, I still prefer this syntax:



```python
filter(lambda x: x.attribute == value, my_list)
```



over



```python
my_list = [i for i in my_list if i.attribute == value]
```



This brings up an interesting thought.  The developer of [Pylint](http://www.logilab.org/857/) and [Guido](http://www.python.org/~guido/) obviously think [filter](http://docs.python.org/library/functions.html#filter) and [map](http://docs.python.org/library/functions.html#map) are second-class citizens.  Does this make them mean we shouldn't use them for future development?

[Not in my book](http://stackoverflow.com/questions/1247486/python-list-comprehension-vs-map).

This discussion reminds me of an old [Python](http://python.org) saying about '[consenting adults](http://mail.python.org/pipermail/tutor/2003-October/025932.html).'

So, for my development I'm going to stick with the old stand-by built-in [filter](http://docs.python.org/library/functions.html#filter) and [map](http://docs.python.org/library/functions.html#map) when I already have a function defined to use in the call.  Otherwise, I think the community seems to prefer using [list comprehensions](http://docs.python.org/tutorial/datastructures.html#list-comprehensions) for readability and possibly performance.

At this point, if you are like me you might want to [remove the pylint warning](https://github.com/durden/dotfiles/commit/e72a9749d6a24ef0be3cb940cab8cce4a947bb0d).  This will free you up to make your own decision based on the situation.