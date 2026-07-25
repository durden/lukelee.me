---
title: "Monkey-patching for good"
date: 2013-02-18
categories:
  - Programming articles
---

# Monkey-patching for good
[Monkey-patching](http://en.wikipedia.org/wiki/Monkey_patch) generally has a negative connotation in the [Python](http://python.org) community.  Luckily, the community [values](http://www.python.org/dev/peps/pep-0020/) code that is straight-forward and explicit, which is typically the opposite of [monkey-patching](http://en.wikipedia.org/wiki/Monkey_patch).

However, there is a time and a place for everything.  In fact, [Ned Batchelder](http://nedbatchelder.com) shows off a very clever use in his [excellent post](http://nedbatchelder.com/blog/201302/hunting_a_random_bug.html) about a recent bug chase.  He replaces the function `random.random` with `lambda: 1/0` which cleverly triggers an exception when someone later in the code tries to use `random.random`.  The real beauty of this 'solution' is the exception and automatic stack trace.  This can be very valuable when debugging code that you're very familiar with.

The [article](http://nedbatchelder.com/blog/201302/hunting_a_random_bug.html) is a great read so be sure to check it out.