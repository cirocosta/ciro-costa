from google.appengine.ext import ndb

class Category(ndb.Model):
	name = ndb.StringProperty()
	description = ndb.TextProperty()

class Source(ndb.Model):
	name = ndb.StringProperty(indexed=True)
	url = ndb.StringProperty()
	image = ndb.StringProperty()
	description = ndb.TextProperty()
	category = ndb.KeyProperty(kind=Category)

class Article(ndb.Model):
	name = ndb.StringProperty(indexed=True)
	date = ndb.DateTimeProperty(indexed=True)
	description = ndb.TextProperty()
	link = ndb.StringProperty()
	source = ndb.KeyProperty(kind=Source)
	category = ndb.KeyProperty(kind=Category)
