---
title: "Great overview of Python profiling"
date: 2013-02-22
categories:
  - Programming articles
---

# Great overview of Python profiling
I'm very interested in [Python](http://python.org) optimization and profiling (see [Quick profiling in Python](http://codrspace.com/durden/quick-profiling-in-python/) and [Profiling Python code with cProfile and pstats](http://codrspace.com/durden/profiling-python-code-with-cprofile-and-pstats/)).  So I'm always on the look out for a good discussion on these topics.

Luckily I ran across [this article](http://www.huyng.com/posts/python-performance-analysis/) by [Huy Nguyen](http://www.huyng.com/).  It covers some great profiling tools I've discussed before such as [line_profiler](http://pythonhosted.org/line_profiler/) as well as some topics like [memory_profiler](https://github.com/fabianp/memory_profiler) which I have been meaning to discuss on this blog.

Also, the [tool for tracking down memory leaks](http://mg.pov.lt/objgraph/), objgraph, is something I've never seen before and will be investigating further.

The one key takeaway from this article is a little insight that's obvious but easily forgotten.  It's related to the [Unix](http://en.wikipedia.org/wiki/Unix) utility [time](http://en.wikipedia.org/wiki/Time_(Unix)) and the 3 'types' of 'time returned (emphasis is my own):

> - real - refers to the actual elasped time
> - user - refers to the amount of cpu time spent outside of kernel
> - sys -refers to the amount of cpu time spent inside kernel specific functions

>You can get a sense of how many cpu cycles your program used up regardless of other programs running on the system by adding together the sys and user times.

> **If the sum of sys and user times is much less than real time, then you can guess that most your program’s performance issues are most likely related to IO waits.**