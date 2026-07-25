---
title: "Python exec performance"
date: 2012-07-09
categories:
  - Programming articles
---

# Python exec performance
I finally got around to reading [Be careful with exec and eval in Python](http://lucumr.pocoo.org/2011/2/1/exec-in-python/) from the always insightful [Armin Ronacher](http://lucumr.pocoo.org/about/).  This is not your typical 'exec/eval is dangerous' post.  I distilled the lengthy article to the following useful sidenotes:

 - Useful semi-low level discussion of [how imports work](http://lucumr.pocoo.org/2011/2/1/exec-in-python/#behind-the-scenes-of-imports)

 - [Performance of exec](http://lucumr.pocoo.org/2011/2/1/exec-in-python/#performance-characteristics):

      - Always use `compile()` if you need to run statement multiple times

      - Always run exec in local scope