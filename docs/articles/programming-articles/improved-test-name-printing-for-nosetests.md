---
title: "Improved test name printing for nosetests"
date: 2015-03-30
categories:
  - Programming articles
---

# Improved test name printing for nosetests
I reach for [pytest](http://pytest.org/latest/) first when setting up a new project.  However, I still have some old projects using the [nose framework](http://nose.readthedocs.org/en/latest/).  [Nose](http://nose.readthedocs.org/en/latest/) is great, but [pytest](http://pytest.org/latest/) provides better output and shorter syntax for testing, command-line options, etc.  I don't want to convert my old projects over because [nose](http://nose.readthedocs.org/en/latest/) is still useful except for one nagging issue.  The syntax for running a single test from the command-line is frustrating.

For example, say I have a bunch of tests in a file located at `tests/test_external_apps.py`, but I only want to run the one called `testLaunch`.  That test is written with Python's [unittest framework](https://docs.python.org/2/library/unittest.html), and I use nose to run it.  The default syntax requires the full path to the test module and then additional syntax using a colon to denote the class.  So, calling my single test would look like this `tests.test_external_apps.TestLaunchExternalApps:testLaunch`.

That is a lot to type.  To make matters worse the default output of a test failure with nose doesn't use this syntax:



```python
======================================================================
ERROR: testLaunch (tests.test_external_apps.TestLaunchExternalApps)
----------------------------------------------------------------------
```



So, you can't easily copy and paste the output to re-run the failed test.  Yes, there is an option, `--failed`, for re-running the previously failed tests.  This is great, but often times I might have a bunch of test failures in a single run. Then, I want to run each test individually and fix them one at a time.

## Plugins to the rescue

It would be much better if the output of a failure at least printed the test information in the syntax needed by the command-line.  Luckily, a plugin exists that does this called [nose_runnable_test_names](https://github.com/coldeasy/nose_runnable_test_names).  You can install it with the standard `pip install nose_runnable_test_names` routine and then use the new command-line argument `--with-runnable-test-names`.  The new output is easy to copy and paste:



```python
======================================================================
ERROR: tests.test_external_apps:TestLaunchExternalApps.testLaunch
----------------------------------------------------------------------
```



What a great example of the [Unix philosophy](https://en.wikipedia.org/wiki/Unix_philosophy#Do_One_Thing_and_Do_It_Well).