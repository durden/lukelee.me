---
title: "Useful context manager for PyQt slot disconnection"
date: 2013-02-28
categories:
  - Programming articles
---

# Useful context manager for PyQt slot disconnection
Every now and then you might want to temporarily [disconnect](http://pyqt.sourceforge.net/Docs/PyQt4/qobject.html#disconnect-2) a [PyQt](http://www.riverbankcomputing.com/software/pyqt/intro) slot, run some arbitrary amount of code, and ensure the slot is connected again.  Unfortunately, it's too easy to forget to reconnect that slot, which can lead to some lost time debugging a 'trivial' issue.  So, I created a very simple little context manager to do this:

[https://gist.github.com/durden/5060373](https://gist.github.com/durden/5060373)