---
title: "Performance of different Python error handling"
date: 2012-12-20
categories:
  - Programming articles
---

# Performance of different Python error handling
Most programmers are familiar with the two common ways of dealing with errors:

 1. [Look before you leap](http://docs.python.org/2/glossary.html#term-lbyl)
 2. [Easier to ask forgiveness than permission](http://docs.python.org/2/glossary.html#term-eafp)

Ever wonder which is *faster*?

I often catch myself thinking about the performance of these two strategies in my everyday Python coding.  Of course, the performance of these is dependent on a number of things, namely the ratio of times you expect something to fail.

This is probably not a foreign concept to any experienced developer, but I stumbled on a [great Stackoverflow answer](http://stackoverflow.com/questions/5589532/try-catch-or-validation-for-speed/) that summarized this quite well.  Give it a quick read, it's worth a refresher.