---
title: "Hidden complexity"
date: 2014-05-30
categories:
  - Programming articles
---

# Hidden complexity

Here's a
[nerve-racking and truthful article](http://tburette.github.io/blog/2014/05/25/so-you-want-to-write-your-own-CSV-code/)
on the hidden complexity when writing a truly portable and solid CSV parser.
Makes you think twice before writing your own CSV parser like this:

<pre>
    for line in file:
        tokens = line.split(',')
</pre>

Trust the Python standard library and do this instead when parsing CSV files:

<pre>
    import csv
</pre>

The [csv module](https://docs.python.org/2/library/csv.html) can feel
over-engineered and complicated at times.  However, parsing CSV is not entirely
trivial, unless you have the luxury of writing both the CSV writer *and*
reader.  Then, you might be able to get away with very simple parsing
techniques.
