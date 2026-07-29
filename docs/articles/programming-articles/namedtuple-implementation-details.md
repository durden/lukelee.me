---
title: "Namedtuple implementation details"
date: 2013-08-08
categories:
  - Programming articles
---

# Namedtuple implementation details
I use [namedtuple](http://docs.python.org/2/library/collections.html#collections.namedtuple) in [Python](http://python.org) all the time.  The implementation is really interesting and unique, as this [excellent namedtuple post](http://jameso.be/2013/08/06/namedtuple.html) demonstrates.

The most interesting part to me was the discussion of namespaces and using [exec](http://docs.python.org/2/reference/simple_stmts.html#grammar-token-exec_stmt).  I'm not sure if I'd write code like this, but it's an interesting way to determine if something is a valid identifier:



```python
for name in (typename,) + field_names:
    try:
        exec ("%s = True" % name) in {}
    except (SyntaxError, NameError):
        raise ValueError('Invalid field name: %r' % name)
```



Interesting, now [go read the article](http://jameso.be/2013/08/06/namedtuple.html) and see if it's something you would write.