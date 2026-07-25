---
title: "Good discussion of MVC and Qt"
date: 2013-02-11
categories:
  - Programming articles
---

# Good discussion of MVC and Qt
I've always been a little bit confused by [Qt](http://qt.nokia.com/)'s [model/view](http://doc.qt.digia.com/stable/model-view-programming.html) terminology.  Luckily, I'm not the only one with this confusion and found a great [stackoverflow post](http://stackoverflow.com/questions/5543198/why-qt-is-misusing-model-view-terminology) on the subject.

It started to make more sense when I realized that the traditional [MVC](http://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller) terminology doesn't really apply to Qt at the application level.  The trick to understanding Qt's terminology is to realize the [model/view](http://doc.qt.digia.com/stable/model-view-programming.html) concept only applies to a single UI component.  Qt's documentation doesn't provide any guidance into how to construct an application wide [MVC](http://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller) architecture.