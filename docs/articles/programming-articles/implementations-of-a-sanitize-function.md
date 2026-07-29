---
title: "Implementations of a sanitize function"
date: 2013-01-10
categories:
  - Programming articles
---

# Implementations of a sanitize function
I was thinking about different ways to implement a function like `sanitize(unsanitized_input, ignored_words)` in [Python](http://python.org).

I came up with a few implementations and noted the downsides of each, etc.  Just a little snippet that others might benefit from.

Go [comment](https://gist.github.com/4504120) on it with your own implementation if I missed some good ideas.

[https://gist.github.com/durden/4504120](https://gist.github.com/durden/4504120)

I also included some code to check the performance of the functions.  Obviously, they all perform fairly close to each other, but just something interesting to think about in your free time:



```text
----- Function Performance -----
sanitize_1 1.100186 secs
sanitize_2 0.661218 secs
sanitize_3 0.664413 secs
sanitize_4 0.682067 secs
sanitize_5 0.983952 secs
```

