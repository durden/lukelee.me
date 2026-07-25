---
title: "Verbose Python"
date: 2012-06-15
categories:
  - Programming articles
---

# Verbose Python
Ever wonder what happens when you try to import a third-party module?  Sometimes it's useful to know exactly where the Python interpreter is looking and what happens.  I sometimes get curious about this or end up debugging some weird missing import, etc.

The solution: `python -v`

This runs the interpreter in verbose mode to trace imports.  You can even specify it multiple times to increase the verbosity, `python -v -v` will give even more information.