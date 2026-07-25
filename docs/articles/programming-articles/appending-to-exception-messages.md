---
title: "Appending to exception messages"
date: 2013-04-24
categories:
  - Programming articles
---

# Appending to exception messages
It's pretty common to catch an exception, do some cleanup, then re-raise that exception.  This is pretty straight-forward.  However, often times I want to re-raise this exception with a modified error message.

It's possible to handle this by doing something like this:

<pre>
try:
    subprocess.Popen(['ls', '-l'])
except Exception as err:
    log.error('Failed launching "ls" command %s' % (err))
    raise
</pre>

This works and allows the caller to see more-detailed information and still get the original exception.  The downside of this approach is the error is printed at a low-level.  What if the caller doesn't deem this exception important enough to report at the *error* log level or even important enough to report at all?  Unfortunately the above solution doesn't allow for this because the caller cannot control how the reporting is handled.

So, there are times when a lower-level function wants to attach additional information and re-raise an exception.  This allows the caller to make the decision to print the error, etc.

I wasn't too sure about the *best* way to do this.  Fortunately, I found a great [Stack overflow post](http://stackoverflow.com/questions/6062576/adding-information-to-a-python-exception) about this.

The syntax is a bit ugly in my opinion, but the solution maintains the original stack trace, which is a nice benefit:

<pre>
def bar(arg1):
    try:
       foo()
    except Exception as e:
        import sys
        raise type(e), type(e)(e.message + 
                               'happens at %s'%arg1), sys.exc_info()[2]
</pre>