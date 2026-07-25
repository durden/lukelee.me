---
title: "Profiling Python code with cProfile and pstats"
date: 2012-05-18
categories:
  - Programming articles
---

# Profiling Python code with cProfile and pstats
I've been trying to profile some [pytables](http://www.pytables.org) code lately and been doing a lot of reading on [cProfile](http://docs.python.org/library/profile.html#module-cProfile) and [pstats](http://docs.python.org/library/profile.html#module-pstats).

In short, do this to see how it works:

`python -m cProfile -o stats <my_awesome_code>.py`

`python -m pstats stats`

The [pstats](http://docs.python.org/library/profile.html#module-pstats) module even provides a command line interface to sort and list your profiling results!  The downside is this seems to be relatively undocumented except for the in-command documentation (type 'help' at the prompt).

I found this [article](http://stefaanlippens.net/python_profiling_with_pstats_interactive_mode) pretty useful.

It's pretty great that Python comes bundled with all of this be default, but be careful on Ubuntu apparently (from article):

> Although the cProfile and pstats modules are listed on the Python Standard Library page, they were not installed by default on my setup (Ubuntu). A simple install of the python-profiler package did the trick.
