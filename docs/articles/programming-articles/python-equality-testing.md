---
title: "Python equality testing"
date: 2012-04-18
categories:
  - Programming articles
---

# Python equality testing
I ran into this [great article](http://me.veekun.com/blog/2012/03/24/python-faq-equality/) on python equality.

I think the discussion on how Python handles [interning](http://docs.python.org/library/functions.html#intern) especially useful.

From the [article](http://me.veekun.com/blog/2012/03/24/python-faq-equality/):

> 

- Most of the time, you want ==.

- Use arg is None when you have a function with an argument defaulting to None. That’s okay, because there’s only one None.

- For testing whether two classes, functions, or modules are the same object, is is okay. Stylistic choice.

- Never use is with str, int, float, complex, or any other core immutable value type! Interning makes the response worthless!

- Other valid uses of is are fairly rare and obscure, for example:

    - If I have a large tree structure and want to find the location of a subtree, == will recursively compare values (potentially very slow) but is will tell me if I’ve found the exact same node.
    
    - A caching mechanism may want to treat all objects as distinct, without having to care about or rely on how they implement ==. is can be appropriate here.

    - Demonstrating to newbies that interning exists is only possible with is :)

