from py2neo import Graph
import backend.wikiparse.settings as settings
__author__ = 'Edward.Kent'


class WikiGraph(object):

    def __init__(self):
        self.graph = Graph(self.get_uri(settings.NEO4J_SERVER, settings.NEO4J_PORT, settings.NEO4J_USERNAME,
                                        settings.NEO4J_PASSWORD))

    @staticmethod
    def get_uri(server_path, port, username, password):
        return "http://{}:{}@{}:{}/db/data".format(username, password, server_path, port)

    def add_article(self, title, id=None):
        if id is not None:
            query = """MERGE (article:Article { title:'{title}'})
                ON CREATE SET article.id = {id}
                """

            self.graph.cypher.execute(query, title=title, id=id)

        else:
            query = """MERGE (article:Article { title:'{title}'})
                """

            self.graph.cypher.execute(query, title=title)

    def add_link(self, from_title, to_title):
        query = """MERGE (from:Article {title:{from_title}})-[rel:RELATED_TO]->(to:Article {title:{to_title}})
                    ON CREATE SET rel.weight = 1
                    ON MATCH SET rel.weight = rel.weight + 1
                """

        self.graph.cypher.execute(query, from_title=from_title, to_title=to_title)

# def test():
#     test_name = 'Test article'
#     test_id = 1
#
#     test_name_2 = 'Test article 2'
#     test_id_2 = 10
#
#     graph = WikiGraph()
#
#     graph.add_article(test_name, test_id)
#     graph.add_article(test_name_2, test_id_2)
#     graph.add_link(test_name, test_name_2)
#     graph.add_link(test_name, test_name_2)
#
#
# if __name__=='__main__':
#     test()