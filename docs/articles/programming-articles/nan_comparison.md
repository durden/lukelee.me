---
title: "NaN comparison and dictionaries"
date: 2017-11-14
categories:
  - Programming articles
---

# NaN comparison and dictionaries

Is it possible for two dictionaries to compare equally if all the keys are not
equal?  Surely not, right?

<pre>
    import numpy

    y = {'a': numpy.nan, 'c': 'test', 'b': numpy.nan}
    x = {'a': numpy.nan, 'c': 'test', 'b': numpy.nan}

    print 'x == y', x == y
    print 'x["a"] == y["a"]', x['a'] == y['a']
</pre>

The first print line prints `True` but the second print line prints `False`.

That's a bit unexpected, so lets dive into why.

The key concepts are equality vs. identity, nan equality and dictionary comparison is implemented.

### 1. Equality

Equality is usually what you're looking with the `==` operator. The following usage of the `==` operator behaves as expected:

<pre>
    x = 4000
    y = 4000

    print x == y
</pre>

Remember everything in Python is an object, even integers. Each object has a memory location that can be determined by using the `id()` function:

<pre>
    print id(x)
    print id(y)
</pre>

The numbers printed above aren't important and vary across systems, but the numbers are different.  Therefore, x and y are different objects, but comparison with `==` is successful.

### 2. Identity

The `is` operator compares identity, i.e. that two objects exactly the same object.

<pre>
    x = 4000
    y = x

    print id(x)
    print id(y)
</pre>

Now both the x and y object point to the same memory location meaning their identity is equal. You can verify this with the `is` operator:

<pre>
    print x is y
</pre>

### 3. nan equality

The numpy.nan variable refers to a specific value inside the numpy package.  So, using numpy.nan will always return the same object.  This means it will always compare successfully with the `is` operator.

By definition two nan objects will always compare as unequal.  This may seem strange, but it's defined by the IEEE standards committee.  You can read more about the rationale behind that [here](https://stackoverflow.com/questions/1565164/what-is-the-rationale-for-all-comparisons-returning-false-for-ieee754-nan-values).

Keep in mind that all the values in your dictionary are instances of the same object, numpy.nan.  So they compare successfully for identity, but not equality.

### 4. Dictionary comparison

Python dictionaries are considered to be equal if both dictionaries have the same keys and the keys refer to the same object **or** if the are equal.  The [generic Python comparison function](https://github.com/python/cpython/blob/2.7/Objects/object.c#L997) assumes identity always implies equality, but as we've seen above that's not the case with nan.

So, we have a clash of two ideas, IEEE dictates that two nan values are not equal, but Python assumes identity implies equality.  In fact [Python's guidelines for creating custom objects](https://docs.python.org/2/reference/expressions.html#value-comparisons) explicitly mention that 'Equality comparison should be reflexive. In other words, identical objects should compare equal.'

Since Python dictionary comparison first checks for identity, not equality, you get the strange result.
