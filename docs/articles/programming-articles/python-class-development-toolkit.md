---
title: "Python class development toolkit"
date: 2013-07-24
categories:
  - Programming articles
---

# Python class development toolkit
You'll probably recognize the name Raymond Hettinger if you lurk on the
[Python mailing-lists](http://mail.python.org/pipermail/python-dev/) or
have ever been to a [Pycon](http://us.pycon.org/2014/) event.  He's a great
speaker and has
[several great Python talks](http://pyvideo.org/speaker/138/raymond-hettinger).
I recently watched one of his
[talks from Pycon 2013 about class development](https://www.youtube.com/watch?v=HTLu2DFOdTg).
As usual, the talk is full of great tidbits for beginners and old-timers.
There's a nice discussion on iterative class design and a few key features that
aren't always touched on in books and tutorials:

- [classmethod](http://docs.python.org/2/library/functions.html#classmethod)
- [staticmethod](http://docs.python.org/2/library/functions.html#staticmethod)
- [__slots__](http://docs.python.org/2/reference/datamodel.html#slots)

Spoiler alert: `__slots__` is **not** inherited by classes!

The real gem of knowledge, for me, was a discussion of
[name mangling](https://en.wikipedia.org/wiki/Name_mangling#Name_mangling_in_Python)
that comes in at around the
[33 minute mark](https://www.youtube.com/watch?v=HTLu2DFOdTg&t=33m25s) where
Mr. Hettinger, being a core developer, mentioned the initial reason behind the
name mangling concept.  It turns out name mangling was never meant to make
things 'private' in the sense that things are 'private' in other
[Object Oriented languages](https://en.wikipedia.org/wiki/Object-oriented_programming)
like [C++](https://en.wikipedia.org/wiki/C%2B%2B) and
[Java](https://en.wikipedia.org/wiki/Java_(programming_language)).

This 'private' misconception is something I've heard several times over the
years.  In fact, I looked around and found a
[good discussion of the initial concept behind name mangling](http://docs.python.org/release/1.5/tut/node67.html)
from [Guido](http://www.python.org/~guido/) himself.  In short, the real
purpose of the double underscore, dunder, is to make a 'class local reference.'

Remember, most of the time `self` means you or your subclasses, but
occasionally you need it to be *just you*.  In other words, it's meant as a way
to to verify that the `self` in your method is actually who you think it is.

The [video](https://www.youtube.com/watch?v=HTLu2DFOdTg) gives a good example:

<pre>
class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # This will call self.perimeter() which in the case of Tire is
        # Tire.perimeter(), not Circle.perimeter.
        p = self.perimeter()

        r = p / math.pi / 2.0
        return math.pi * r ** 2.0

class Tire(Circle):
    def perimeter(self):
        return Circle.perimeter(self) * 1.25
</pre>

This code makes it difficult to keep a local copy of our original `perimeter`
method since it could be overridden by subclasses.  The naive solution to this
would be to do something like the following:

<pre>
class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # This will call self.perimeter() which in the case of Tire is
        # Tire.perimeter(), not Circle.perimeter.
        p = self.perimeter()

        r = p / math.pi / 2.0
        return math.pi * r ** 2.0

    _perimeter = perimeter
</pre>

Of course, this doesn't really work because subclasses could also override this
new `_perimeter` attribute.  So, the solution is to use the double underscore
naming convention because [Python](http://python.org) automatically does the
name translation for us.  This ensures we use our own `perimeter()`, not one
from a derived class, because the dunder, `__`, will add the class name.

If this concept interests you, and you would like to hear **and** see an
even better discussion of this topic
[watch the video](https://www.youtube.com/watch?v=HTLu3DFOdTg).