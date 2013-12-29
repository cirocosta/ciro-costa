import webapp2
import settings

from google.appengine.ext import ndb
from cirofeed.models import Article,Source,Category

class IndexPage(webapp2.RequestHandler):
    def get(self):
        categories = Category.query()
        sources = Source.query()
        template_values = {
            'categories'    :   categories,
            'sources'       :   sources
        }        

        template = settings.JINJA_ENVIRONMENT.get_template(\
            'cirofeed/index.html')
        self.response.write(template.render(template_values))


class CategoriesPage(webapp2.RequestHandler):
    def get(self):
        categories = Category.query()
        template_values = {
            'categories'    :   categories,
        }
        template = settings.JINJA_ENVIRONMENT.get_template(\
            'cirofeed/categories.html')
        self.response.write(template.render(template_values))


class CategoriesAdd(webapp2.RequestHandler):
    def post(self):
        name = self.request.get('category_name')
        description = self.request.get('category_description')

        ancestor_key = ndb.Key('Category',name)
        category = Category(parent=ancestor_key,name=name,\
            description=description)
        category.put()

        self.redirect('/cirofeed/categories')
        

class SourcesPage(webapp2.RequestHandler):
    def get(self):
        sources = Source.query()
        categories = Category.query()
        template_values = {
            'sources'   :   sources,
            'categories':   categories,
        }
        template = settings.JINJA_ENVIRONMENT.get_template(\
            'cirofeed/sources.html')
        self.response.write(template.render(template_values))


class SourcesAdd(webapp2.RequestHandler):
    def post(self):
        name = self.request.get('source_name')
        description = self.request.get('source_description')
        category = self.request.get('source_category')
        url = self.request.get('source_link')

        if link != None and name != None:
            category_iter = Category.query(Category.name == category).iter()
            try:
                categ = category_iter.next()
                source = Source(parent=ndb.Key('Source',name),name=name,\
                    description=description,category=categ.key,url=url)
                source.put()
            except StopIteration:
                categ = None
        self.redirect('/cirofeed/sources')


class RefreshDb(webapp2.RequestHandler):
    def get(self):
        self.response.write('lol')