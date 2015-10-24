__author__ = 'Edward.Kent'

import cherrypy

test_string = 'Behold a string'

class Server(object):

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def test_json(self):
        return test_string

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self, request=None): # Refactor to PUT
        if request is not None:
            reply = self._PUT_method(request)
        return reply

    def _PUT_method(self, request):
        return test_string


if __name__ == '__main__':
    cherrypy.quickstart(Server())