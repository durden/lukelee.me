---
title: "Carefully choose function and method names when writing tests with nose"
date: 2012-03-23
categories:
  - Programming articles
---

# Carefully choose function and method names when writing tests with nose
The [nose](http://readthedocs.org/docs/nose) testing package is really great.  It allows you to run a single command and instantly it will find and run all of your tests.  You have to implicitly *tell* nose how to find your tests.  This is done with one of the following:

 - Write your tests in a [python-friendly](http://docs.python.org/library/unittest.html) way

 - Use the built-in nose naming conventions

Using the built-in unittest style of creating tests is really nice and should be considered.  However, the nose naming conventions apply (by default) regardless of whether you use the unittest module or not.  So, it's useful to know what they are to avoid creating a function/method using these conventions when not intending for it to be involved in your test execution.

The conventions are spelled out in their documentation, but in my experience this is easy to forget.

First off, nose has the concept of a 'testMatch' regular expression which tells you whether or not something is a test.  The default regex (it can be customized) is


```python
((?:^|[\\b_\\.-])[Tt]est)
```



You can pretty much just think of this as **anything that has 'test' or 'Test'**.  This makes sense, all things named like tests are tests.

The gotcha part of this naming convention is in the realm of test fixtures, packages, modules, etc.  See, there are a lot of other concepts nose allows for when writing setup/teardown functionality for your tests at the class, module, and package levels.  For example, the following list of words are considered **special** to nose:

- setup

- setup_package

- setUp

- setUpPackage

- teardown

- teardown_package

- tearDown

- tearDownPackage

- setup_module

- setUpModule

- teardown_module

- tearDownModule

- setup_class

- setupClass

- setUpClass

- setupAll

- setUpAll

- teardown_class

- teardownClass

- tearDownClass

- teardownAll

- tearDownAll

Most of these are self-explanatory with maybe the except of the variants of 'all.' These are for the class level setup/teardown meaning each will be run at the start and end of the class of tests respectively.

So, what's the big deal here?  This can be a problem if you happen to make a function or method named after any of the above **special** names.  You might not want this code to run in the context that nose will invoke it.  Also, your *misnamed* function or method might not even be related to testing at all!

However, nose doesn't know this.  Thus, it will run these when it feels appropriate regardless of whether you call it explicitly in your code or not.

For more information on these naming conventions, see [writing-tests](http://readthedocs.org/docs/nose/en/latest/writing_tests.html) in the official nose documentation.