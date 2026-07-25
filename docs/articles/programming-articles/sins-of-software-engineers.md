---
title: "Sins of Software Engineers"
date: 2014-06-09
categories:
  - Programming articles
---

# Sins of Software Engineers
Here's a [very opinionated article on bad scientific code and best practices](http://www.yosefk.com/blog/why-bad-scientific-code-beats-code-following-best-practices.html).  It's hard not to be offended by the author claiming Software Engineer's jobs are trivial.  The problem with the article is that scientists need Software Engineers and vice versa.  We should be working together, not writing articles diminishing each other's professions.

The author manages to point out several flaws in typical high-brow Software Engineer code, despite the frantic ranting and narrow-minded view of the profession.  I'm honest enough to know that I've been guilty of several of these from time to time:

> - Multiple/virtual/high-on-crack inheritance
> - 7 to 14 stack frames composed principally of thin wrappers, some of
> them function pointers/virtual
> functions, possibly inside interrupt
> handlers or what-not
> - Files spread in umpteen directories
> - Lookup using dynamic structures from hell - dictionaries of names where the
> names are concatenated from various
> pieces at runtime, etc.
> - Dynamic loading and other grep-defeating techniques
> - A forest of near-identical names along the lines of DriverController,
> ControllerManager, DriverManager,
> ManagerController, controlDriver ad
> infinitum - all calling each other
> - Templates calling overloaded functions with declarations hopefully
> visible where the template is defined,
> maybe not
> - Decorators, metaclasses, code generation, etc. etc.

However, it's not that these practices are **always bad**, but that they should be used with caution.
