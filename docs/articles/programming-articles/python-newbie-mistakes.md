---
title: "Python newbie mistakes"
date: 2013-07-11
categories:
  - Programming articles
---

# Python newbie mistakes
[Great article](http://blog.amir.rachum.com/post/55024295793/python-common-newbie-mistakes-part-2) on Python newbie mistakes by Amir Rachum.  The article is a short read and has some nice realizations for new Python developers as well as seasoned veterans.

> The first misconception is that
> Python, being an interpreted language
> (which is awesome, I think we can all
> agree), is executed line-by-line. In
> truth, Python is being executed
> statement-by-statement. To get a feel of what I mean, go to your favorite shell (you aren’t using the default one, I hope) and type the following:

<pre>
def foo():
</pre>
> Press Enter. As you can see, the shell
> didn’t offer any output and it’s
> clearly waiting for you to continue
> with your function definition. It will
> continue to do so until you finish
> declaring you function. This is
> because a function declaration is a
> statement. Well, it’s a compound
> statements, that includes within it
> many other statements, but a statement
> notwithstanding. The content of your
> function isn’t being executed until
> you actually call it. What is being
> executed is that a function object is
> being created.
