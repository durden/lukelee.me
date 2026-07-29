---
title: "XML parsing in Python"
date: 2012-03-30
categories:
  - Programming articles
---

# XML parsing in Python
Parsing XML in Python isn't difficult.  In fact, the difficulty comes from the fact that there are so many choices including modules packaged in the standard library.

I came across [this great resource](http://eli.thegreenplace.net/2012/03/15/processing-xml-in-python-with-elementtree/) to explain a lot of the options and when to use what.

The article doesn't point out another potential parsing option, [lxml](http://lxml.de/).  I've had personal experience with this library and been generally happy with the performace.  The documentation is a bit confusing at times, but it gets the job done.

Another useful thing to look into is the [objectify](http://lxml.de/objectify.html) interface for lxml found in the lxml.objectify module.  The main point of this interface is to make interacting with xml more 'pythonic' and somewhat obscure the fact that you are working with xml in the first place.  It is very useful if you are parsing simple data types like int, float, string, etc. out of xml files.

I've found that using objectify to deal with sequence types like lists and dictionaries is a bit cumbersome.  However, I haven't fully explored the possibilities.  However, I was able to easily serialize sequence types to xml and back to python objects by using some ideas from objectify.  Namely the idea of storing the python type as an attribute on the xml node when saving it.  This is a great idea and allows you to deserialize the xml into a python object easily.  For example, if the xml denotes a python dict, you can see this and easily traverse the xml converting xml tags to dictionary keys.



```python
def _xmlElementToDict(element):
    """Convert given xml element to a dict"""

    setting = {}

    for sub_el in element.iterchildren():
        setting[sub_el.tag] = _xmlElementToSimpleBuiltInType(sub_el)

    return setting

def _xmlElementToSimpleBuiltInType(element):
    """Convert xml element to a built-in 'simple' type (int/float/bool/etc)"""

    pytype = element.get('pytype')

    # Convert simple types
    conv_func = getattr(__builtin__, pytype, None)

    if conv_func is None:
            return None

    # Caveat, only '' will be converted to False by bool()
    if pytype == 'bool' and element == 'False':
        return False

    return conv_func(element.text)
```



Notice how storing the actual type conversion function, 'int', 'float', etc., allows use to parse it out and convert it directly without having to try a bunch of different types or clutter up the code with a complicate if/else.  Pretty fancy huh?