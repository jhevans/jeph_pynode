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
            response['articles'] = self.wikigraph.get_related_articles(title, limit=limit, destinationTitle=destinationTitle)
            return response
        else:
            return no_title_response

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def shortestPath(self, title=None, destinationTitle=None): # Refactor to PUT
        if title is not None:
            assert destinationTitle is not None
            path = self.wikigraph.get_shortest_path(title, destinationTitle)
            if len(path) == 0:
                raise cherrypy.NotFound()

            response = {}
            response['length'] = len(path)
            response['articles'] = path

            return response
        else:
            return no_title_response

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def randomTitle(self):
        return {'name': self.wikigraph.get_random_node()}

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def randomTitles(self):
        title_1, title_2, path_length = self.wikigraph.get_random_nodes()
        return {'title1': title_1,
                'title2': title_2,
                'pathLength': path_length,
                }


if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '0.0.0.0',
                            'server.socket_port': 8080,
                            })
    mock_wikigraph = WikiGraph()
    cherrypy.quickstart(Server(mock_wikigraph))
