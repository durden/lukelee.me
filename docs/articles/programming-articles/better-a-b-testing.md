---
title: "Better A/B Testing"
date: 2012-05-30
categories:
  - Programming articles
---

# Better A/B Testing
I recently spent some time playing around with a [django](http://djangoproject.com) [project](https://github.com/durden/split_testing_playground) for [A/B split testing](http://en.wikipedia.org/wiki/A/B_testing).

I had not done any of this type of testing on any of my sites before.  So, I figured it would be a nice way to learn about the actual statistics behind it as well as how to implement it in a really simple manner.  One of the keys of split testing is to make sure to show the options an equal number of times.  This way your results don't get skewed.

In my understanding you 'run' a split testing for a specified amount of time, look at the results, then replace the options with the 'best' one once and for all (until your next test).  So, you bounce between options equally over a specified amount of time, pick a winner, and move on.  This seems pretty straight-forward, but you have to keep going back (or should) and continue testing new ideas to see what results in the best conversion rates.

What if your algorithm could just adapt over time and allow most visitors to see the 'best' option at any given time while still mixing in some new ideas every now and then?  This sounds like an even better plan.  Don't kid yourself, I didn't come up with this idea.  I read it in an [article](http://stevehanov.ca/blog/index.php?id=132) by [Steve Hanov](http://stevehanov.ca).

Go read it for yourself.  His explanation is much better than mine!

> Like many techniques in machine learning, the simplest strategy is hard to beat