---
title: "Decorating main"
date: 2012-06-04
categories:
  - Programming articles
---

# Decorating main
I've read a [few](http://sayspy.blogspot.com/2012/05/thoughts-on-using-function-signatures.html) [articles](http://www.blog.pythonlibrary.org/2012/05/31/python-201-decorating-the-main-function/) about decorating the main function in a [Python](http://python.org) script.

These are interesting ideas, but some of the article [comments](http://www.blog.pythonlibrary.org/2012/05/31/python-201-decorating-the-main-function/) point out several problems with the decorator approach.  The biggest problem to me is that the decorator executes the actual decorated function as soon as it's encountered.

I've always thought the
`if __name__ == "__main__":`
syntax was ugly.

I remember writing [Python](http://python.org) for years without every really knowing what it even meant.  To me it was just the [Python](http://python.org) way of 'int main()' in [C](http://en.wikipedia.org/wiki/C_(programming_language)) and a weird [Python](http://python.org) idiom.

I finally started to understand what was really happening behind the scenes of that weird idiom when I began playing around with [metaprogramming](http://en.wikipedia.org/wiki/Metaprogramming) [1].  However, I still think this is a strange syntax for beginners and subtly exposes them to an [introspection](http://www.ibm.com/developerworks/library/l-pyint/index.html) concept very early on.

This syntax is truly some of the worst [Python](http://python.org) has to offer and oddly enough it's one of the first that new developers see.

--------
[1] Great talk on [metaprogramming](http://pyvideo.org/video/884/python-metaprogramming-for-mad-scientists-and-evil)