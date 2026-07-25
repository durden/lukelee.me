---
title: "Python class attributes refresher"
date: 2014-03-07
categories:
  - Programming articles
---

# Python class attributes refresher
Here's a [great refresher on class attributes](http://www.toptal.com/python/python-class-attributes-an-overly-thorough-guide).

I didn't realize that `__dict__` on a class object returned a proxy that didn't allow deletion.  I'm not exactly sure why I'd ever want to delete things from a class object on the fly.  However, thinking about it lead me to create this interesting gist.

Deleting a method from a class object after instances have been created seems like a bad idea, but [we're all consenting adults here](https://mail.python.org/pipermail/tutor/2003-October/025932.html) so do as you see fit for your problem.

[https://gist.github.com/durden/9421967](https://gist.github.com/durden/9421967)
