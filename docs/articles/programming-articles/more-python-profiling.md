---
title: "More Python profiling"
date: 2012-05-30
categories:
  - Programming articles
---

# More Python profiling
I ran across another [good article](http://www.tracelytics.com/blog/profiling-python-performance-lineprof-statprof-cprofile/) that lines up with my recent [profiling post](http://codrspace.com/durden/profiling-python-code-with-cprofile-and-pstats/).

It's a good case study on starting to profile a small 'application' at a high-level and slowly drilling down the stack to see what is the bottleneck.  It also includes some nice information on something I didn't mention in my article, [statprof](http://pypi.python.org/pypi/statprof/).

I especially liked this quote from the article:

> Most performance problems aren’t complex; they’re just well-hidden. 