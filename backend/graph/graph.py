from py2neo import Graph
from backend.wikiparse import settings
__author__ = 'Edward.Kent'


class Graph(object):

    def __init__(self):
        self.graph = Graph(self.get_uri(settings.NEO4J_SERVER, settings.NEO4J_PORT, settings.NEO4J_USERNAME,
                                        settings.NEO4J_PASSWORD))

    @staticmethod
    def get_uri(server_path, port, username, password):
        return "http://{}:{}@{}:{}/db/data".format(username, password, server_path, port)

    def add_article(self, title, id):
        query = """MERGE (article:Article {{ title:'«title»'}})
            ON CREATE SET article.id = «id»
            """

        self.graph.cypher.execute(query, title=title, id=id)

    def add_link(self, from_title, to_title):
        query = """MERGE (from:Article {title:«from_title»})-[rel:RELATED_TO]->(to:Article {title:«to_title»})
                    ON CREATE SET rel.weight = 1
                    ON MATCH SET rel.weight = re.weight + 1
                """

        self.graph.cypher.execute(query, from_title=from_title, to_title=to_title)
