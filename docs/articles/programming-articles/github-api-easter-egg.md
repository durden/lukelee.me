---
title: "Github API easter egg"
date: 2012-11-25
categories:
  - Programming articles
---

# Github API easter egg
I cannot remember where I found [this easter egg](https://api.github.com/zen), but it's kind of fun.  As you can see, [Github](https://github.com) is always having fun.

While on the topic of fun, why not write a little script to see how many unique zen quotes we can collect?

[https://gist.github.com/durden/4144148](https://gist.github.com/durden/4144148)

Note that the script isn't fully-featured or error proof.  I just hacked it together.  The biggest problem with it is that the [Github API](http://developer.github.com/v3/) only allows 60 unauthenticated requests per hour.  The script should detect that it was rate limited and automatically wait an hour before going again in order to keep trying to detect unique quotes.  Feel free to fix it up by forking the [gist](https://gist.github.com/4144148) or posting a reply to it with a better version.