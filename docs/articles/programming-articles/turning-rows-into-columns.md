---
title: "Turning rows into columns"
date: 2013-03-08
categories:
  - Programming articles
---

# Turning rows into columns
My mind was blown today while reading a [good article on Pandas performance](http://wesmckinney.com/blog/?p=278).  The built-in [zip function](http://docs.python.org/2/library/functions.html#zip) has magic powers I've never thought of before.

    >>> x = [(1,2,3), (4,5,6)]
    >>> zip(*x)
    [(1, 4), (2, 5), (3, 6)]

Turn a list of rows into a list of columns!  Of course, this can be done faster by using [Pandas](http://pandas.pydata.org/) but you'll have to read the above referenced article for those details.
