---
title: "Dangers of syntax highlighing"
date: 2014-05-18
categories:
  - Programming articles
---

# Dangers of syntax highlighing

Here's a very
[interesting article on the effects of syntax highlighting](https://medium.com/web-dev/6f83add748c9).

As most Software Engineers, I'm very particular about my syntax coloring.
However, I've never given thought to how comments typically are de-emphasized.
It's something worth pondering, especially since my chosen color scheme of
years, [desert](http://hans.fugal.net/vim/colors/desert.html), uses a somewhat
understated shade of blue.

The effects of comment colors is interesting, but I was drawn to the article's
discussion on diff colors.

The article cites several very popular quotes on the concept of less code is
better code [1]:

    But we all know, and we’ve all known for a long time, that less is more. ‘The
    best code is no code at all.’ ‘I have made this function so long only because I
    did not have the time to make it shorter.’ More code equals more bugs.

I think most Software Engineer's would agree with those sentiments.  However, I
never realized how the standard diff colors drive home the opposite:

    I shouldn’t need to tell you that red and green have another important meaning:
    red means bad and green means good.

    Our diff viewer, then, tells us that deletions are bad, dangerous, and possibly
    an error, while insertions are good, safe, and successful. More code good. Less
    code bad.

Seems like a reasonable conclusion to make, and one that I agree with.
However, it's interesting how difficult it was for me to read the author's
alternative diff colors, blue and olive.

I am one of those people that looks at diffs all day and retraining my eyes for
this would be difficult.  However, maybe it's a worthwhile decision to make?
Now if only I could convince the entire team to join the experiment.

What do you think?  Would you try the alternative diff colors?

[1] See the article's text for links to the actual quotes and citations.
