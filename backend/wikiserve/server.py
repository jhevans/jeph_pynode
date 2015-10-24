__author__ = 'Edward.Kent'

import cherrypy

from backend.wikiserve.article import Article

test_string = 'Behold a string'

no_id_response = 'Invalid arguments'

class Server(object):

    def __init__(self, wikigraph):
        self.wikigraph = wikigraph

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def test_json(self):
        return test_string

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self, article_id=None): # Refactor to PUT
        if article_id is not None:
            reply = self._PUT_method(article_id)
        else:
            reply = no_id_response
        return reply

    def _PUT_method(self, article_id):
        active_article = self._get_article(article_id)
        response = self._get_response(active_article)
        return response

    def _get_article(self, article_id):
        return Article(article_id, self.wikigraph)

    def _get_response(self, active_article):
        response = {}
        response['pageid'] = active_article.page_id
        response['name'] = active_article.name
        response['linkedArticles'] = active_article.related_articles
        return response


if __name__ == '__main__':
    cherrypy.quickstart(Server())

