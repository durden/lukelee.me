---
title: "Verifying test independence"
date: 2014-10-29
categories:
  - Programming articles
---

# Verifying test independence

Tests should not depend on each other to pass. In general, each test should
perform its' operation in complete isolation. This is clear from standard
testing framework such as
[JUnit](http://junit.org/),
[unittest](https://docs.python.org/2.7/library/unittest.html), and
[pytest](http://pytest.org/latest/).  Notice the concept of *cleaning up* is
introduced very early in the documentation.

Each test is encouraged to handle setting up its' environment as well as
cleaning up.  This is good practice and can prevent sudden test failures when
introducing a new test.

Have you ever run into a situation where adding a new test suddenly causes
another, seemingly unrelated test to fail?

This is a difficult issue to debug. It's most likely a side-effect of the test
execution order. One test somewhere in your test suite is not setting up or
cleaning up properly.

So, writing independent tests is very important, but how can you be sure you've
achieved this goal?

### Random order

One *trick* I use is to randomize the order my tests are run every now and
then. I use [pytest](http://pytest.org/latest/) as my testing framework, and
there's a
[nice plugin to randomize test execution](https://github.com/klrmn/pytest-random).
I install this plugin and use the --random option to mix things up a bit.

Mix your tests up every once in a while and see if something fails.  There's a
good chance any failures you see (assuming your tests pass beforehand) are due
to subtle dependency issues.

### Downsides

There's one downside. Running with the --random option once doesn't guarantee
you are free of test dependencies. Remember, the order is random. The random
order can hide the dependencies just as your *normal* test order can.

There's not an easy way to tell how many times you need to run with `--random`
to verify this.  Sure, you could do the math, track all the possible
permutations and verify you try them all.  You could even write code to do
that.

However, periodically running tests in a random order provides a higher degree
of confidence in your test independence, and it's easy with
[pytest](http://pytest.org/latest/) and the
[pytest-random plugin](https://github.com/klrmn/pytest-random).
