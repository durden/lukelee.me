---
title: "Quickly transform every element into a tuple"
date: 2012-03-22
categories:
  - Programming articles
---

# Quickly transform every element into a tuple
There are times when I need to return a tuple for some reason but would like to use a little one-liner list comprehension to transform each element in the tuple.

For example, say I have a tuple of red, green, blue for setting a color in a GUI element.  I might have for some reason done some floating point math to arrive at the original rgb value.  However, before returning this I want to ensure that all elements in the color tuple are integers.

I could do the following:



```python
rgb = (254.5, 255.0, 5)
rgb_list = []

for color in rgb:
    rgb_list.append(int(color))

return tuple(rgb_list)
```



This is very straight-forward code to follow, but takes up a lot of space for something so simple.  How can we do this is a shorter way and still not lose any readability? List comprehensions!



```python
rgb = (254.5, 255.0, 5)
tuple([int(color) for color in rgb])
```



Not too bad!  However, if you really want to get fancy you could use map():


```python
rgb = (254.5, 255.0, 5)
tuple(map(int, rgb))
```



At this small of an example the choice between any of these is really up to your style and what you think is readable.  I don't think performance really enters into the conversation yet, but just for fun how do the list comprehension and map compare performance wise?



```python
>>> from timeit import timeit
 >>> timeit('tuple([int(color) for color in (254.5, 255.0, 5)])')
0.7590341567993164

 >>> timeit('tuple(map(int, (254.5, 255.0, 5)))')
0.7299971580505371
```



There is a difference, but it's pretty small.  Again, this doesn't really matter all that much at this scale, but it's something worth keeping in mind.