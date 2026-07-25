---
title: "Numpy testing"
date: 2012-04-05
categories:
  - Programming articles
---

# Numpy testing
Testing for array equality is very common when writing unit tests for code that heavily utilizes [numpy](http://numpy.scipy.org/).  So, to further expand on my recent call to use [smart python asserts](http://codrspace.com/durden/smart-python-asserts/) here are a few [great asserts](http://docs.scipy.org/doc/numpy/reference/routines.testing.html) customized just for numpy.

<pre>
import numpy
experiment = numpy.arange(10, 20)
year = numpy.arange(1990, 2000)
numpy.testing.assert_array_equal(experiment, year)

AssertionError: Arrays are not equal

(mismatch 100.0%)
 x: array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
 y: array([1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999])
</pre>

This is so much more informative and easy than the naive assert method I used before:
<pre>
import numpy
experiment = numpy.arange(10, 20)
year = numpy.arange(1990, 2000)

equal = year == experiment
self.assertTrue(equal.all(), "Mismatched arrays")

self.assertTrue(equal.all(), "Mismatched arrays")
AssertionError: Invalid return value
</pre>