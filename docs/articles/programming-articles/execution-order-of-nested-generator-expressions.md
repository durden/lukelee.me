---
title: "Execution order of nested generator expressions"
date: 2014-03-28
categories:
  - Programming articles
---

# Execution order of nested generator expressions
What does this print?



```python
units = [1, 2]
tens = [10, 20]
nums = (a + b for a in units for b in tens)
units = [3, 4]
tens = [30, 40]
print nums.next()
```



I was surprised by the result because of the subtle way [generator expressions are executed](http://docs.python.org/2/reference/expressions.html#generator-expressions).  The reasoning makes sense, which is to preserve your sanity when there's an error triggered by the generator.

This is a neat example of something I've always taken for granted.  One could argue writing code like this is a bit obtuse and should be avoided.  However, this is still an interesting detail to be aware of.

Check out the following articles for quiz-like questions and a discussion of surprising Python 'quirks.'

- [Surprising Python](http://ballingt.com/2014/03/23/surprising-python.html)
- [Reid's Python quiz](http://web.archive.org/web/20101009122154/http://web.mit.edu/rwbarton/www/python.html)