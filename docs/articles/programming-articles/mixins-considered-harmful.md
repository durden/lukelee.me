---
title: "Considering mixins"
date: 2014-04-08
categories:
  - Programming articles
---

# Considering mixins
I've recently been testing out the idea of using [Mixins](http://en.wikipedia.org/wiki/Mixin) for an upcoming project.  I resist because the [mixin](http://en.wikipedia.org/wiki/Mixin) pattern uses multiple inheritance, which usually screams complexity and trouble.  [Mixins](http://en.wikipedia.org/wiki/Mixin) are typically supposed to circumvent the [diamond problem](http://en.wikipedia.org/wiki/Multiple_inheritance#The_diamond_problem) by attempting to not have any clashing method names.

However, as projects grow, as all good ones do, keeping this namespace pollution problem in check becomes cumbersome.  Even if you now the [method resolution order in Python](http://python-history.blogspot.com/2010/06/method-resolution-order.html) like a pro it wastes time on bugs that most likely could have been avoided using a different pattern.

On the other hand, the mixin pattern is very useful for [separating concerns](http://en.wikipedia.org/wiki/Separation_of_concerns).  It's just too bad that the end user of an object using mixins cannot see that separation.

I haven not been able to articulate my objections to the mixin pattern, but luckily for me this [mixins considered harmful](https://www.artima.com/weblogs/viewpost.jsp?thread=246483) series of articles provides a lot of examples and detailed discussion.

The author does a great job of arguing for generic functions over mixins:

> The advantage of generic functions is
> that they are clearly defined outside
> classes, whereas the mixin approach is
> kind of schizophrenic: the
> functionality is actually defined
> externally, but that fact is made
> invisible to the final user.

I've always felt that using modules for namespacing is useful, and I often push off writing classes until they are clearly needed.  I often see a lot of Python code with unnecessary classes everywhere, and until never understood why this style was so popular.  This quote from the [mixin article series](https://www.artima.com/weblogs/viewpost.jsp?thread=246483) hits the nail on the head:

>  In most languages instead, classes
> are used as a namespace control
> mechanism, performing double duty -
> namespace control should be the job of
> modules.

Excellent point and those are just a few highlights from the second post in the series.  You should give them all a read if your interested in the downsides of mixins:

 - [Part 1](https://www.artima.com/weblogs/viewpost.jsp?thread=246341)
 - [Part 2](https://www.artima.com/weblogs/viewpost.jsp?thread=246483)
 - [Part 3](https://www.artima.com/weblogs/viewpost.jsp?thread=254367)
 - [Part 4](https://www.artima.com/weblogs/viewpost.jsp?thread=254507)