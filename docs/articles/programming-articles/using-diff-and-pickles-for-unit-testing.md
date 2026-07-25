---
title: "Using diff and pickles for unit testing"
date: 2014-11-05
categories:
  - Programming articles
---

# Using diff and pickles for unit testing
I stressed using diff and [serialized numpy arrays](http://docs.scipy.org/doc/numpy/reference/generated/numpy.savetxt.html) in my [recent talk on testing](https://www.youtube.com/watch?v=Xjv8ZwZf-h4).  I was pleasantly surprised to read the authors of [High Performance Python](http://shop.oreilly.com/product/0636920028963.do) agree.

> Unit testing a complicated section of code that generates a large numerical output may be difficult. Do not be afraid to output a text file of results to run through diff or to use a pickled object. For numeric optimization problems, Ian likes to create long text files of floating-point numbers and use diff—minor rounding errors show up immediately, even if they’re rare in the output.

By the way, go and read [High Performance Python](http://shop.oreilly.com/product/0636920028963.do). It's excellent.