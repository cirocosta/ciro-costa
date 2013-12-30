from google.appengine.ext import ndb

class Category(ndb.Model):
    name = ndb.StringProperty()
    description = ndb.TextProperty()


class Source(ndb.Model):
    name = ndb.StringProperty(indexed=True)
    url = ndb.StringProperty()
    image = ndb.StringProperty()
    description = ndb.TextProperty()
    etag = ndb.StringProperty()
    category = ndb.KeyProperty(kind=Category)


class Article(ndb.Model):
    title = ndb.StringProperty(indexed=True)
    summary = ndb.TextProperty()
    description = ndb.TextProperty()
    published = ndb.DateTimeProperty(indexed=True)
    link = ndb.StringProperty()
    source = ndb.KeyProperty(kind=Source)
