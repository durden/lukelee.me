---
title: "Python import best-practices"
date: 2014-06-23
categories:
  - Programming articles
---

# Python import best-practices
Ever been confused by Python imports or wanted to see a strong argument on how to do them *right*?  If so, go read this [great article on packaging python projects](http://blog.habnab.it/blog/2013/07/21/python-packages-and-you/).

I've never read a better or more concise discussion of implicit relative imports,
explicit relative imports, and absolute imports.  I've read
[PEP 328](http://www.python.org/dev/peps/pep-0328/) numerous times over the
years, but the [packaging article](http://blog.habnab.it/blog/2013/07/21/python-packages-and-you/)  explains more with much less confusion.

I disagree with the author's ultimate guidance on *always* using the
fully-qualified module name in imports.  I've been on several projects where the
top-level module has a name change or has an annoying, long name.  So, I
sometimes prefer to use explicit relative imports with the 'dotted'
notation.  However, as the author suggests, this choice is primarily an issue
of style.

There is a strong case **for** using the fully-qualified module name.  It's nice
that all your imports are identical, including your test imports.  In fact,
your tests import the package **exactly** like 'real users' of your library. That's pretty powerful.