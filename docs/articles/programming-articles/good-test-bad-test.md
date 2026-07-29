---
title: "Good test, bad test"
date: 2015-05-06
categories:
  - Programming articles
---

# Good test, bad test
[Good Test, Bad Test](http://late.am/post/2015/04/20/good-test-bad-test.html) is an insightful article.  The article has opinions that are sure to be polarizing, but the reasoning is spot on.  For example, doing this:



```python
self.assertEqual(
    datetime(2015, 3, 11, 20, 9, 25),
    parsed_dict["date"],
)
self.assertEqual("GET", parsed_dict["method"])
self.assertEqual("/foo", parsed_dict["path"])
self.assertEqual("bar=baz", parsed_dict["query"])
```



instead of this:



```python
self.assertEqual({
    "date": datetime(2015, 3, 11, 20, 9, 25),
    "method": "GET",
    "path": "/foo",
    "query": "bar=baz",
}, parsed_dict)
```



The former is more code, but the useful error messages pay dividends if this test fails.  You'll thank yourself when you spend a day refactoring and chasing test failures.

Also, there are quite a few quotes to remember when looking through your test code:

 1. > Whenever you write a test, you have to consider: what would cause this test case to pass when it ought to fail? 
 2. > It's important to acknowledge that tests can smell just as well as real code. We deal with code smell in a test suite the same as we would in any other type of code -- with thought and care.