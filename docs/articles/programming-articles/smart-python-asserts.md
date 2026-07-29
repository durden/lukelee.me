---
title: "Smart Python asserts"
date: 2012-04-04
categories:
  - Programming articles
---

# Smart Python asserts
The [unittest](http://docs.python.org/library/unittest.html) module in Python is fully-featured and included in the standard library.  I would hesitate using anything else when testing my Python projects.  However, I've been doing it wrong.

There are a ton of useful [assert variants](http://docs.python.org/library/unittest.html#assert-methods).  At first glance it might seem like overkill.  I mean all you really need is assertTrue() right? I guess you could really kick it up a notch and use assertFalse too just for fun.  Well if your like me your unit tests are littered with statements like this:



```python
self.assertTrue('entityname' in col_names)
```



Nothing about either of these is *wrong* until you see the messages you get for a failing test.



```python
AssertionError: False is not true
```



**False is not True!**

Of course it's not, but this isn't terribly useful.  However, after a little research into the [assert variants](http://docs.python.org/library/unittest.html#assert-methods) we can come up with the following:


```python
self.assertIn('entityname', col_names)
AssertionError: 'entityname' not found in ['entity_name', 'Time', 'Qo', 'Co', 'Qg', 'Cg']
```



**Much better**.  We didn't even have to write our own custom error message, which all the assert* methods take as an optional argument.  Of course, writing your own custom message can be really helpful, but all of these built-in asserts are meant to keep you from having to do this.

The authors of the unittest module thought carefully about providing sensible defaults when designing the assert methods.  So next time you are writing your unit tests think carefully about what assert method you use.  It could save you some time when looking at and writing failure messages.

Here's another great example of something that should be avoided:


```python
self.assertTrue(val >= 1979.0)
AssertionError: False is not true

self.assertGreaterEqual(val, 1979.0)
AssertionError: 1978.0 not greater than or equal to 1979.0
```

