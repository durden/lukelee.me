---
title: "PyQt signal styles"
date: 2012-08-16
categories:
  - Programming articles
---

# PyQt signal styles
Newer versions of [PyQt](http://www.riverbankcomputing.co.uk/software/pyqt/intro)
(starting with version 4.5) have support for
[two](http://www.riverbankcomputing.co.uk/static/Docs/PyQt4/html/new_style_signals_slots.html) different styles of syntax for signals.

I prefer to use the new-style simply because it looks cleaner and closer to
native [Python](http://python.org).  I don't like having to specify types and
function calls in strings like:



```python
self.connect(self.listWidget, SIGNAL("itemClicked(QListWidgetItem *)"), self.itemSelected)
```



This syntax seems to expose too much of the native C++ nature of
[Qt](http://qt.nokia.com/).

I've always used the new syntax:



```python
self.listWidget.itemClicked.connect(self.itemSelected)
```



This choice served me well until I started experimenting with  
[Qt Designer and pyuic4](http://www.riverbankcomputing.co.uk/static/Docs/PyQt4/html/designer.html)
to generate GUI code.  The issue is that pyuic4 generates code with the
old-style signal syntax.  I suppose this isn't a real problem since the whole
point of using GUI code generation tools is to avoid having to write and/or see
GUI code.

But, what happens when you want to manually disconnect a signal that is
automatically hooked up by the auto-generated code?

I don't want to use this old-style syntax in my own code.  So when I recently
needed to disconnect a signal from auto-generated code I chose to use the
new-style syntax like the following:



```python
self.buttonBox.accepted.disconnect(self.accept)
```



This __looks__ correct, but I kept running into this error:



```python
self.buttonBox.accepted.disconnect(self.accept)
TypeError: disconnect() failed between 'accepted' and 'accept'
```



What is going on here?  I know the signal is connected by the auto-generated
code!

I found the
[answer](http://python.6.n6.nabble.com/Possible-bug-with-new-signal-slot-connection-td4974638.html)
after a bit of searching around.  The end result is that you __cannot__
[mix and match](http://www.riverbankcomputing.co.uk/static/Docs/PyQt4/html/new_style_signals_slots.html#mixing-new-style-and-old-style-connections)
syntax styles on the __same__ object.  So, if a particular signal is connected
with the old-style syntax then it must be disconnected with the old-style.

However, you can mix and match the syntax styles across __different__ objects.

So to resolve my issue I have two choices:

1. Manually edit the auto-generated code (and remember to do so everytime it's regenerated)

2. Use one line of the old-style syntax in my hand-written code.

I chose the latter because it's the easiest and least error-prone solution.

This is probably something to keep in mind if you, like me, prefer the
new-style syntax but still want to use
[Qt Designer and pyuic4](http://www.riverbankcomputing.co.uk/static/Docs/PyQt4/html/designer.html).