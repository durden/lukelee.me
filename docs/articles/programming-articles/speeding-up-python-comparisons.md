---
title: "Speeding up python comparisons"
date: 2013-04-15
categories:
  - Programming articles
---

# Speeding up python comparisons
Did you know that the following would *even run* in Python?



```python
>>> x = 10
>>> y = 20
>>> z = 30
>>> z < x < y
```



Well, it turns out you can [combine comparisons arbitrarily](http://docs.python.org/2/reference/expressions.html#not-in) and skip evaluating a variable twice.  Not only does this work, but it's faster!



```python
>>> x = 10
>>> y = 20
>>> z = 30
>>> z < x < y
False
>>> if x > z or x < y: print 't'
t
>>> %timeit z < x < y
10000000 loops, best of 3: 59.7 ns per loop
>>> %timeit x > z or x < y
10000000 loops, best of 3: 131 ns per loop
```



Ok, so **71.3 ns** is not going to really change your application all that much.  However, this is a rare situation where the optimized version of the code is actually more **readable** as well.