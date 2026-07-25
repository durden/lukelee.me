---
title: "Python Packaging"
date: 2014-10-23
categories:
  - Programming articles
---

# Python Packaging
[Python](http://python.org) packaging is a source of constant frustration for
me.  I've experimented with different package layouts and
[setup.py files](https://docs.python.org/2/distutils/setupscript.html), but none of them have met my expectations.

I'm constantly searching for new ways to package projects. Luckily, this
[detailed article on Python package layout](http://blog.ionelmc.ro/2014/05/25/python-packaging/)
makes solid recommendations. I'll be adding a lot of these ideas to my next project.

Read the
[entire article](http://blog.ionelmc.ro/2014/05/25/python-packaging/), but here
are my take-home points.

### Import Parity

Have you released a package only to notice your imports are broken
after installing with [pip](https://pip.pypa.io/en/latest/) or
[setuptools](https://pypi.python.org/pypi/setuptools)?  I've done this more
times than I like to admit.

The issue is:

    The current directory is implicitly included in sys.path; but not so when
    installing & importing from site-packages. Users will never have the same
    current working directory as you do.

    This constraint has beneficial implications in both testing and packaging:

    You will be forced to test the installed code (e.g.: by installing in a
    virtualenv). This will ensure that the deployed code works (it's packaged
    correctly) - otherwise your tests will fail. Early. Before you can publish
    a broken distribution.

    You will be forced to install the distribution. If you ever uploaded a
    distribution on PyPI with missing modules or broken dependencies it's
    because you didn't test the installation. Just beeing able to successfuly
    build the sdist doesn't guarantee it will actually install !

### Tests placement

Where do you place your tests in your projects?  I prefer a *tests*
directory in each subpackage so tests are close to the code they're
testing.  This works, but it's unrealistic.  It's the issue of import parity
again. The imports are different between tests and what the end-user
encounters, especially if you are using
[relative imports](http://legacy.python.org/dev/peps/pep-0328/#rationale-for-relative-imports).

This isn't a *problem*, but it further distances your tests from the reality of
the user. It's important to get as
[close to the user experience](http://www.slideshare.net/lukelee11/writing-dumb-tests/25)
as possible.