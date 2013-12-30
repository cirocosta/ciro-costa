from cirofeed.models import Source,Article,Category
from datetime import datetime
from utils import feedparser
from google.appengine.ext import ndb

""" Abstracao da maquina para download de feed e transformacao em entidades
para database.

Buscar como tornar multi-thread depois. 
"""

class FeedParserEtagException(Exception):
    pass


class Parser(object):
    def __init__(self):
        self.getSources()

    def getSources(self):
        self.sources = Source.query().iter()

    def executeSourceDownloads(self):
        while self.sources.has_next():
            self.downloadSource(self.sources.next())

    def downloadSource(self,source):
        if source.etag != None:
            d = feedparser.parse(source.url,etag=source.etag)
        else:
            d = feedparser.parse(source.url)
        save_in_db = False
        articles = []
        if d.has_key('status'):
            if d.status == 200:
                if d.has_key('etag'):
                    save_in_db = True
                    source.etag = d.etag
                for entry in d.entries:
                    title = entry.title \
                        if entry.has_key('title') \
                        else None
                    summary = entry.summary \
                        if entry.has_key('summary') \
                        else None
                    description = entry.description \
                        if entry.has_key('description') \
                        else None
                    link = entry.link \
                        if entry.has_key('link') \
                        else None 
                    article = Article(parent=ndb.Key('Article',source.name),\
                        published=datetime(*entry.published_parsed[:6]),\
                        source=source.key,title=title,description=description,\
                        summary=summary,link=link)
                    articles.append(article)
                if save_in_db:
                    self.bulkEntityInsertion(articles)
                    source.put()
        print articles

    @ndb.transactional
    def bulkEntityInsertion(self,entities):
        for entity in entities:
            entity.put()



