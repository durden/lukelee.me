---
title: "Python code quality"
date: 2012-04-10
categories:
  - Programming articles
---

# Python code quality
Here is a great read on [python code quality](http://css.dzone.com/articles/python-code-quality).

> One more quick disclaimer here - why do we care about code quality? Let's face it - there are two reasons that we need to improve the quality of our code. The first reason is that I suck. It's true! Sometimes I write really poor code; usually, even. There are lots of reasons; excuses really - maybe I'm exploring the problem space. Maybe I thought it would be a one-off script. Maybe I'm new to the language or the library. Maybe I'm under time pressure so I just want it to work. Maybe I just don't care.

> The second reason is that you suck too. In fact the only code worse than my code is other people's code - and I'm confident that you all could make that statement yourselves.

I couldn't agree more.  I've always really liked using [pylint](http://www.logilab.org/857) and [pep8](https://github.com/jcrocholl/pep8) to try and cleanup/standardize code.  However, the above article mentions a few more tools I can't wait to try in some automated fashion to find code smells and refactoring opportunities:

- [clonedigger](http://clonedigger.sourceforge.net/)

- [pygenie](http://traceback.org/2008/03/31/measuring-cyclomatic-complexity-of-python-code/)