---
title: "Python can be evil"
date: 2012-12-14
categories:
  - Programming articles
---

# Python can be evil
## Disclaimer: This is just for fun, don't use this code!

I read an [article](http://pydev.blogspot.com/2012/12/python-tricks-making-sure-function-is.html) the other day about how to make sure a function is only called once.  I'm not entirely sure of a **real** use-case for this sort of thing.  However, it was an interesting brain teaser.

The comments of the article even suggested a funny trick to play, call a random function instead of the real one after 1 call.  So, I decided to implement something to do this just to test my [metaprogramming](http://en.wikipedia.org/wiki/Metaprogramming) skills:

[https://gist.github.com/durden/4285944](https://gist.github.com/durden/4285944)

Go checkout out the new [Github Gist](https://gist.github.com) interface and try it out!