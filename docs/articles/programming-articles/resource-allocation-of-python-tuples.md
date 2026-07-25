---
title: "Resource allocation of Python tuples"
date: 2014-06-13
categories:
  - Programming articles
---

# Resource allocation of Python tuples
I'm currently reading the early release of [High Performance Python](http://shop.oreilly.com/product/0636920028963.do).  The book is pretty rough around the edges since it's not even officially published.  However, I have high hopes for the final product.  There's already a lot of useful information in this early stage.

For example, did you know this about CPython tuples?

> Another benefit of the static nature
> of tuples is something python does in
> the back‐ ground: resource caching.
> Python is garbage collected, which
> means that when a vari‐ able isn’t
> used anymore python frees the use of
> the memory back to the operating
> system for use in other applications
> (or other variables).


> For tuples of sizes 1-20, when they
> are no longer used the space isn’t
> immediately given back to the system
> but rather saved for future use. This
> makes it so that when a new tuple of
> that size is needed in the future we
> don’t need to communicate with the
> operating system to find a region in
> memory to put the data since we have a
> reserve of free memory already.

That's neat, but the book didn't cite any proof.  So, I did my own research in the source of Python 2.7.7.  Sure enough, the book's authors were exactly right.  The proof is right [at the top of the tuple C implementation](http://hg.python.org/cpython/file/08a2b36f6287/Objects/tupleobject.c#l6), and you can read the source to see the full extent of the optimization.