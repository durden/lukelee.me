---
title: "Using lambda with pyqt signals"
date: 2012-06-18
categories:
  - Programming articles
---

# Using lambda with pyqt signals
I wanted to share another great usage for the [lambda keyword](http://docs.python.org/tutorial/controlflow.html#lambda-forms) when working with [PyQt](http://www.riverbankcomputing.co.uk/software/pyqt/intro) in addition to [more popular extra arguments use case](http://eli.thegreenplace.net/2011/04/25/passing-extra-arguments-to-pyqt-slot/).

I used the [lambda](http://docs.python.org/tutorial/controlflow.html#lambda-forms) 'trick' to add a custom context menu to a table header in a [QTableWidget](http://www.riverbankcomputing.co.uk/static/Docs/PyQt4/html/qtablewidget.html).

The following snippet is a brief example of using a  [lambda](http://docs.python.org/tutorial/controlflow.html#lambda-forms) 'function' to pass the screen position of a right-click operation alongside the [triggered](http://www.riverbankcomputing.co.uk/static/Docs/PyQt4/html/qaction.html#triggered) signal.  This position is then used inside of a [QTableWidget](http://www.riverbankcomputing.co.uk/static/Docs/PyQt4/html/qtablewidget.html) to detect which row/column were clicked on.

<pre>
    def _addContextMenu(self):
        header_item.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        header_item.customContextMenuRequested.connect(self.showContextMenu)

    def showContextMenu(self, position):
        deselect_others = QtGui.QAction("Deselect &others", self)
        deselect_others.triggered.connect(lambda: self.deselectOthers(position))

        menu = QtGui.QMenu()
        menu.addAction(deselect_others)
        menu.exec_(self.sender().mapToGlobal(position))

    def deselectOthers(self, position):
        print self.indexAt(position).row()
        print self.indexAt(position).column()
</pre>