---
title: "Adding braces to Python"
date: 2014-03-09
categories:
  - Programming articles
---

# Adding braces to Python
Ever wonder what it would take to add braces to Python?  Enter [Python with braces](http://www.pythonb.org/).

The [main diff](https://github.com/eshirazi/python-with-braces/commit/9c9c0079e4ac5b2ccec1056ac90c94daf89165a6#diff-cb0b9d6312c0d67f6d4aa1966766ceddR34) modifies the Python grammar and related parsing functionality.  If you're still interested, the following little snippets kickstart the magic:

 - [Change a simple statement to require semi-colons](https://github.com/eshirazi/python-with-braces/commit/9c9c0079e4ac5b2ccec1056ac90c94daf89165a6#diff-cb0b9d6312c0d67f6d4aa1966766ceddR34)
 - [Change a suite of statements to use braces and semicolons instead of indentation](https://github.com/eshirazi/python-with-braces/commit/9c9c0079e4ac5b2ccec1056ac90c94daf89165a6#diff-cb0b9d6312c0d67f6d4aa1966766ceddR78)

I don't think this will fork will catch on at all even though I'd consider myself the target audience for this type of thing.  I'm a Python convert from a long history in [C](http://en.wikipedia.org/wiki/C_(programming_language)) and wouldn't want to use this.  I love the indentation requirement.

However, this project illustrates how open sourcing a language can open up all sorts of possibilities and allow smaller communities to form around their own preferences.  Maybe this type of project opens Python up to all the people who would love the language if they could just get past the whitespace requirement.

Again, using a fork like this is probably not advisable for production, in my opinion, but you have to admit the diff is relatively small.

Finally, it's great that Python has a single [grammar file](https://github.com/eshirazi/python-with-braces/blob/master/Grammar/Grammar) and even a published [guide to changing Python's grammar](http://legacy.python.org/dev/peps/pep-0306/) for people interested in syntax design and parsing.