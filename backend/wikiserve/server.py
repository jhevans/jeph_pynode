from backend.graph.graph import WikiGraph

__author__ = 'Edward.Kent'

import cherrypy

from backend.wikiserve.article import Article
from backend.wikiserve.mock_graph import MockWikiGraph

test_string = 'Behold a string'

no_title_response = 'Invalid arguments'

class Server(object):

    def __init__(self, wikigraph):
        self.wikigraph = wikigraph

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def test_json(self):
        return test_string

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def related(self, title=None, limit=None, destinationTitle=None): # Refactor to PUT
        if title is not None:
            response = {}
            response['name'] = title
            response['linkedArticles'] = self.wikigraph.get_related_articles(title, limit=limit, destinationTitle=destinationTitle)
            return response
        else:
            return no_title_response

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def shortestPath(self, fromTitle=None, destinationTitle=None): # Refactor to PUT
        if fromTitle is not None:
            assert destinationTitle is not None
            path = self.wikigraph.get_shortest_path(fromTitle, destinationTitle)
            if len(path) == 0:
                raise cherrypy.NotFound()

            response = {}
            response['length'] = len(path)
            response['articles'] = path

            return response
        else:
            return no_title_response


if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '0.0.0.0',
                            'server.socket_port': 8080,
                            })
    mock_wikigraph = WikiGraph()
    cherrypy.quickstart(Server(mock_wikigraph))

