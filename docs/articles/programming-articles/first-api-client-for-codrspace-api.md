---
title: "First API client for codrspace API"
date: 2012-05-18
categories:
  - Programming articles
---

# First API client for codrspace API
I created this project called [frappy](http://github.com/durden/frappy) a while back that attempts to make it easy to wrap web APIs by implementing a small wrapper class.  Currently it supports the following services out of the box:

- [github](http://github.com) [code](https://github.com/durden/frappy/blob/master/frappy/services/github.py)

- [forrst](http://forrst.com) [code] (https://github.com/durden/frappy/tree/master/frappy/services/forrst.py)

- [twitter](https://github.com/durden/frappy/blob/master/frappy/services/twitter/twitter.py)

- And now.... [Codrspace](https://github.com/durden/frappy/blob/master/frappy/services/codrspace.py)!

You can get your API code by logging in to codrspace and going [here](http://codrspace.com/api-settings/).  Check out the module doctests for usage details.  So, plug in your API key and go for it!
