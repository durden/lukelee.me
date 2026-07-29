---
title: "Flatten Python lists with itertools module"
date: 2012-05-31
categories:
  - Programming articles
---

# Flatten Python lists with itertools module
Every now and then you end up with a data structure that looks like this:



```python
listOflists = [[1,2,3],[4,5,6]]
```



Then you would like to 'flatten' this list to essentially loop over it as a single list instead of a list of 2 separate, smaller lists.  Well, check out the [itertools module](http://docs.python.org/library/itertools.html#module-itertools) for a good [recipe](http://docs.python.org/library/itertools.html#itertools.chain) on how to do this.



```python
def flatten(listOfLists):
    "Flatten one level of nesting"
    return chain.from_iterable(listOfLists)
```

