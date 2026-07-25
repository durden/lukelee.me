---
title: "Downsides of exception handling languages"
date: 2013-12-12
categories:
  - Programming articles
---

# Downsides of exception handling languages
I recently read an [article on the reliability of C](http://tratt.net/laurie/blog/entries/how_can_c_programs_be_so_reliable), and it reminded me of my frustrations with exception handling languages, specifically Python:

> In other words, when one calls a
> function like stat in C, the
> documentation lists all the failure
> conditions; the user can then easily
> choose which errors conditions he
> wishes his program to recover from,
> and which are fatal to further
> execution (in extsmail, out of memory
> errors are about the only fatal
> errors). This is a huge difference in
> mind-set from exception based
> languages, where the typical
> philosophy is to write code as normal,
> only rarely inserting try ... catch
> blocks to recover from specific errors
> (which are only sporadically
> documented).

I can relate to this directly because I was a professional C programmer for almost 5 years.  I write almost all Python these days, and I love exception handling.  However, because of my C background, I'm constantly worried I'm missing potential useful error cases.  Yes, it's nice to write a function without any error handling and essentially punt those complications to other function' in your call stack.

However, it's frustrating to write reliable Python code because the documentation and philosophy make tracking down all possible exceptions difficult.  In fact, I'm not aware of a good way, besides lots of manual inspection, to determine all the possible exceptions that can be raised by a library call.  This is even more difficult once you start to consider Python's dynamic nature and the ability to [monkey patch](http://en.wikipedia.org/wiki/Monkey_patch) code.  However, the problem is still difficult with those complications aside. 

Sometimes finding all the possible exceptions is easy if the code base is small.  However, tracking down all the possible error cases, exceptions, gets extremely difficult as your project grows in size.  

I'd love to see some kind of tool that can do this, but it's not a trivial problem.  The Java world tries to solve this with checked and unchecked exceptions and documenting possible exceptions in the function headers.

The Python community could do something very similar, but I'm reluctant to ever rely on a function comment to reliably tell me such important information.  After all, I routinely forget to update my own function comments.

Unfortunately, I don't have a solution, but I'd love to start a discussion.  So, let me know if there's some project or documentation reference that can provide the possible exceptions for a call trace or entry point.
