---
title: "Speed up list searches"
date: 2013-03-01
categories:
  - Programming articles
---

# Speed up list searches
Need a way to speed up searching [Python](http://python.org) [lists](http://docs.python.org/2/library/stdtypes.html#sequence-types-str-unicode-list-tuple-bytearray-buffer-xrange), give [sets](http://docs.python.org/2/library/sets.html) a try.

<pre>
    >>> x = set(range(100))
    >>> y = range(100)
    >>> %timeit 100 in x
    10000000 loops, best of 3: 50 ns per loop
    >>> %timeit 100 in y
    1000000 loops, best of 3: 1.78 us per loop
</pre>
Why the dramatic speed up?  Remember [sets](http://docs.python.org/2/library/sets.html) are un-ordered and don't allow duplicates.  Thus, they are actually implemented using [dictionaries](http://docs.python.org/2/library/stdtypes.html#mapping-types-dict).

The [set documentation](http://docs.python.org/2/library/sets.html) explains this very well if you need a refresher:

> The set classes are implemented using
> dictionaries. Accordingly, the
> requirements for set elements are the
> same as those for dictionary keys;
> namely, that the element defines both
> __eq__() and __hash__(). As a result, sets cannot contain mutable elements
> such as lists or dictionaries.
> However, they can contain immutable
> collections such as tuples or
> instances of ImmutableSet. For
> convenience in implementing sets of
> sets, inner sets are automatically
> converted to immutable form, for
> example, Set([Set(['dog'])]) is
> transformed to
> Set([ImmutableSet(['dog'])]).

