---
title: "Dictionary KeyError with assertRaises"
date: 2012-06-13
categories:
  - Programming articles
---

# Dictionary KeyError with assertRaises
Have you ever wanted to write a unit test that verifies a key doesn't exist in a dictionary?  If so, you've probably done it several ways:

<pre>
self.assertIn('mykey', mydict.keys())

try:
    tmp = mydict[mykey]
except KeyError:
    pass
else:
    self.fail()

self.assertEqual(mydict.get(mykey), None)
self.assertIsNone(mydict.get(mykey))
</pre>

You can probably come up with various other ways using self.assertListEqual(), etc.  However, none of these test the actual statement mydict[mykey], except the long try/except code above.  I know that essentially using dict.get() does the same thing, etc.  I still don't think it's as **good**.

Fortunately there is a [special assert statement](http://docs.python.org/library/unittest.html#unittest.TestCase.assertRaises) in the [unittest module](http://docs.python.org/library/unittest.html) just for an occasion like this.  However, it only takes a callable so that rules out something like this:

<pre>
self.assertRaises(KeyError, mydict[mykey])
</pre>

**Lambda to the rescue!**

<pre>
self.assertRaises(KeyError, lambda: mydict[mykey])
</pre>

Using [lambda](http://docs.python.org/tutorial/controlflow.html#lambda-forms) turns our dictionary lookup into a callable which allows us to pass a single statement anywhere a function or a [callable](http://docs.python.org/reference/datamodel.html#object.__call__) object is required.

This is a great testing use-case for this nice little anonymous function.  It allows us to test the statement exactly as it would appear in code with the assertRaises() method.