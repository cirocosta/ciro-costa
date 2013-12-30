import webapp2
import settings
import index.views
import guestbook.views
import cirofeed.views

application = webapp2.WSGIApplication([
    ('/',                       index.views.IndexPage),
    ('/guestbook',              guestbook.views.MainPage),
    ('/guestbook/sign',         guestbook.views.Guestbook),
    ('/cirofeed',               cirofeed.views.IndexPage),
    ('/cirofeed/categories',    cirofeed.views.CategoriesPage),
    ('/cirofeed/categories/add',cirofeed.views.CategoriesAdd),
    ('/cirofeed/sources',       cirofeed.views.SourcesPage),
    ('/cirofeed/sources/delete',cirofeed.views.SourcesDelete),
    ('/cirofeed/sources/add',   cirofeed.views.SourcesAdd),
    ('/cirofeed/sources/details/([a-zA-Z0-9\-\_]+)',\
    	cirofeed.views.SourcesDetails),
], debug=settings.DEBUG)