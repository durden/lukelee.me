---
title: "Connecting PyQt signals with decorators"
date: 2013-04-04
categories:
  - Programming articles
---

# Connecting PyQt signals with decorators
I've been writing [PyQt](http://www.riverbankcomputing.com/software/pyqt/intro) for several years now and just ran across a [QSignalMapper code snippet](http://pysnippet.blogspot.com/2010/06/qsignalmapper-at-your-service.html) demonstrating the process of connecting a signal to a slot with a decorator.  I suppose this is not a common design within the PyQt community.  Is there a reason for this?

Consider the following example of how `connect` can be used as a decorator:



```python
# Handle grid clicks here  
@win.clicked.connect  
def clicked(index):  
    print "Button at:", index, " - text:", items[index].text()
```



It never occurred to me, but the [connect](http://pyqt.sourceforge.net/Docs/PyQt4/new_style_signals_slots.html#connecting-disconnecting-and-emitting-signals) method of a [pyqtSignal object](http://pyqt.sourceforge.net/Docs/PyQt4/new_style_signals_slots.html#defining-new-signals-with-pyqtsignal) is **almost** a decorator by definition [1]:

> A decorator is any callable Python
> object that is used to modify a
> function, method or class definition.
> A decorator is passed the original
> object being defined and returns a
> modified object, which is then bound
> to the name in the definition.

So, we *can* use `connect` as a decorator, but is it the *right* way to do signal connection?

## Decorator 'surprise'

Notice I said **almost** because a decorator also **returns** a new callable.  The [connect](http://pyqt.sourceforge.net/Docs/PyQt4/new_style_signals_slots.html#connecting-disconnecting-and-emitting-signals) doesn't return anything, technically it returns `None`.  So, using `connect` as a decorator causes a subtle side-effect that is a bit destructive.  The `connect` decorator in the scenario above took a publicly available function and *removed* it.

This could be a bit surprising for newcomers.  However, I think this scenario provides a good jumping off point for thinking about what decorators really are and how the [Decorator Design Pattern](http://en.wikipedia.org/wiki/Decorator_pattern) works in general.  I definitely do not want to imply that the above example is *bad*, just that it's a bit surprising and subtle.

## Lessons

The takeaway from this is that you **can** connect signals and slots with a decorator.  This approach provides a few readability benefits:

 - Makes obvious connection between a function and a signal
 - Concise way of taking a 'normal' function and 'modifying' it to be a PyQt slot

However, there are a few downsides as well:

 - `connect` essentially removes the function (now a PyQt slot) from namespace
 - Adds restriction that the function/slot cannot be re-used by any non-signal code

Another restriction that's not immediately obvious is there is no way to use this *trick* when the function/slot is declared within a class and relies on `self`.  Remember, decorators are evaluated at **definition time not runtime**.  So, the decorator line itself cannot refer to `self`.

## Decorator fail

For example, you cannot use `connect` to write a decorator that connects to a signal declared **within** a class.  The following example should provide enough context to demonstrate this restriction using the [Model-View-Controller](http://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller) design pattern.

[https://gist.github.com/durden/5310601](https://gist.github.com/durden/5310601)

## Decision

I like that `connect` *can* be used as a decorator and in some instances it makes the code much more readable.  The [QSignalMapper snippet](http://pysnippet.blogspot.com/2010/06/qsignalmapper-at-your-service.html) demonstrates some of the benefits.  However, that is an example and not a full, complex application.  So, in general I think the downsides of using `connect` as a decorator outweigh the benefits in most *large* applications.

However, this is not a black and white scenario.  You'll have to carefully think about your scenario and decide which option provides the most benefit [2].  Hopefully now you can clearly see the tradeoffs of this design choice.

### Bonus: Verify for yourself

You should try this to convince yourself I'm not lying to you.  Run the following example and you'll notice you get a `TypeError` because the `clicked` method is `None` after the decorator:

[https://gist.github.com/durden/5310356](https://gist.github.com/durden/5310356)

[1] [Definition of Python decorator](http://en.wikipedia.org/wiki/Python_syntax_and_semantics#Decorators)

[2] You *could* write your own decorator that wraps the use of `connect` and returns a callable.  This would avoid the biggest pitfall of `connect` as a decorator, but in my opinion this adds another layer of abstraction that is unnecessary with something as mundane and simple as signal connection. 