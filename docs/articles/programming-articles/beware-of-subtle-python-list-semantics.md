---
title: "Beware of subtle python list semantics"
date: 2012-08-03
categories:
  - Programming articles
---

# Beware of subtle python list semantics
Here's a quiz:



```python
x = [1]
y = [2]
print id(x)

x += y
print x, id(x)

x = [1]
y = [2]
print id(x)

x = x + y
print id(x)
```



Do += or + create a new object or update the existing one in place?  Seems a bit ambiguous and the answer was somewhat unexpected, at least for me.

Keep in mind [+= is a shorthand for x.extend(y)](http://stackoverflow.com/a/2347272/1108031).

I would be curious to know why the Python language was designed with this little 'trick.'  It seems like this blatantly violates the '**There should be one-- and preferably only one --obvious way to do it.**' mantra from [The Zen of Python](http://www.python.org/dev/peps/pep-0020/).

There is a lot of good information associated with [this question](http://stackoverflow.com/questions/2347265/what-does-plus-equals-do-in-python) so make sure to scan through the whole thread.  [This answer](http://stackoverflow.com/a/2347423/1108031) has some nice insight into the special method implementation and design.

The design makes sense but this is definitely something to keep in mind when using the += operator.