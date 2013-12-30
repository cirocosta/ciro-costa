What's This?
========

This is the repo that contains all of the source code of my personal website that [currently runs here](http://ciro-costa.appspot.com).

What's cool here?
========
Cirofeed
-------
Web application that i'm developping to get the link of some things that i enjoy following on the internet (super simple feed follower).

Its already using: [feedparser ](http://code.google.com/p/feedparser/) for parsing, [Channel API](https://developers.google.com/appengine/docs/python/channel/) for websockets-a-like, [Cron](https://developers.google.com/appengine/docs/python/config/cron) for task schedulin in production, [Celery](http://www.celeryproject.org/) for task scheduling in local dev.  

Planning to use: [GCM For Chrome](http://developer.chrome.com/apps/cloudMessaging.html) for instant notification on chrome app, [Mandrill](http://mandrill.com/) as main mailing api.

- Problems: sub-reddits, e.g, don't provide etag/last-modified headers. For these cases i'll create a validator so that these websites will have to be 'for moment-view only'

Guestbook
-------
Guestbook is a simple guestbook application that let users sign it with a comment. That's the first app that you create when getting into appengine so i decided to mantain the code as it is but just with a better template.


Ps.:
======
The project lacks of a good documentation and testing scripts. 
I plan to do that but as it requires time, it will come soon.