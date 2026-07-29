---
title: "Dealing with special characters in JSON and Handlebars.js templates"
date: 2012-07-07
categories:
  - Programming articles
---

# Dealing with special characters in JSON and Handlebars.js templates
I recently had to dive in much deeper into [Handlebars.js](http://handlebarsjs.com/) while working on a new feature to the nifty [Syte project](https://github.com/rigoneri/syte/).  [Handlebars.js](http://handlebarsjs.com/) is just one of the many client-side [Javascript templating languages](http://engineering.linkedin.com/frontend/client-side-templating-throwdown-mustache-handlebars-dustjs-and-more) available these days.

The project is relatively mature and pretty easy to work with.  However, I ran into a weird problem with the template language itself and some of syntax/reserved characters.  [Handlebars.js](http://handlebarsjs.com/) reserves the '#' character for some of the [block helpers](http://handlebarsjs.com/block_helpers.html).

These helpers are useful for handling small amounts of logic like if and loop statements.  However, what happens when you are passing in a [JSON](http://www.json.org/) context variable that uses '#' as a key?

Take the below snippet of JSON from a call to the [last.fm](http://lastfm.com) API:



```json
{
    "recenttracks": {
        "@attr": {
            "page": "1", 
            "perPage": "10", 
            "total": "54185", 
            "totalPages": "5419", 
            "user": "durden2.0"
        }, 
        "track": [
            {
                "album": {
                    "#text": "Shake! Shake! Shake!", 
                    "mbid": "03a8bcdb-112b-4d75-973a-2b727f1020ee"
                }, 
            }
    ]
}
```



Ideally in the template you would use something like this to render the '#text' information in html:


```html
{{#with recenttracks }}
  <ul> 
    {{#each track}}
        <li> {{album.#text}} </li>
    {{/each}}
  </ul>
{{/with}}
```



Unfortunately this will not work since '#' is reserved by the templating language itself.

I couldn't seem to find a good way to accomplish this without parsing all of the JSON myself just to make a new JSON object without '#' in the keys.  This seems like a bunch of work so I went to the [Internet](http://google.com) for a solution.

I found a few interesting [Github](http://github.com) issues related to this topic:

 - [Unable to parse special characters](https://github.com/wycats/handlebars.js/issues/110)
 - [Complex JSON object and illegal '#' property](https://github.com/wycats/handlebars.js/issues/229)

Neither of these really had a solution, but I did stumble on a way to 'register helpers' using the Handlebars.registerHelper() functionality.  This is similar to [custom tags/filters](https://docs.djangoproject.com/en/dev/howto/custom-template-tags/) in the [Django](http://djangoproject.com) world.

Essentially it allows you to specify a 'function' to pass the template variable through, which turns out to be a good way to temporarily 'bounce out' of the [Handlebars.js](http://handlebarsjs.com/)  templating language and back to standard Javascript code.  Getting the requested variable out is easy with the normal syntax for [associative arrays](http://www.pageresource.com/jscript/jarray2.htm) once your in standard Javascript code.

For example, here is the simple solution once all these pieces are put together:

 - Code to be placed anytime BEFORE calling your template with the special '#' character:


```javascript
Handlebars.registerHelper('text', function(obj) {
        return obj['#text'];
    });
```



 - Template code to use above helper:


```html
{{#with recenttracks }}
  <ul> 
    {{#each track}}
        <li> {{text album}} </li>
    {{/each}}
  </ul>
{{/with}}
```



I also posted this [solution](https://github.com/wycats/handlebars.js/issues/229#issuecomment-6826100) on the previously mentioned [Github issue](https://github.com/wycats/handlebars.js/issues/229) so be sure to go there and follow the on-going discussion.