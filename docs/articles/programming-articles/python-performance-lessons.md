---
title: "Python performance lessons"
date: 2012-07-24
categories:
  - Programming articles
---

# Python performance lessons
I ran across [this article](http://blog.explainmydata.com/2012/07/expensive-lessons-in-python-performance.html) on profiling python, etc.  I took away three things from it:

1. [Numpy's](http://numpy.scipy.org/) [take method](http://docs.scipy.org/doc/numpy/reference/generated/numpy.take.html) could speed up 'fancy' indexing.

2. [Pandas](http://pandas.pydata.org/pandas-docs/stable/index.html) has very fast/efficient [join]( http://pandas.pydata.org/pandas-docs/stable/merging.html) and [group by](http://pandas.pydata.org/pandas-docs/stable/groupby.html) by functionality.

3. Use named tuples more often when needing 'simple' objects that are not going to change.  They are essentially c-structs and thus are contiguous in memory.