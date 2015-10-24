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
            query = """MERGE (article:Article { title:{title}})
                ON CREATE SET article.id = {id}
                """

            self.graph.cypher.execute(query, title=title, id=id)

        else:
            query = """MERGE (article:Article { title:{title}})
                """

            self.graph.cypher.execute(query, title=title)

    def add_link(self, from_title, to_title, count=1):
        query = """MERGE (from:Article {title:{from_title}})-[rel:RELATED_TO]->(to:Article {title:{to_title}})
                    ON CREATE SET rel.weight = 1
                    ON MATCH SET rel.weight = rel.weight + {count}
                """

        self.graph.cypher.execute(query, from_title=from_title, to_title=to_title, count=count)

    def get_related_articles(self, article_title):
        query = """MATCH (article1:Article {title: {title}})-[:RELATED_TO]->(article2: Article) RETURN article2"""

        result = self.graph.cypher.execute(query, title=article_title)
        return result


def test1():
    test_name = 'Test article 3'
    test_id = 2

    test_name_2 = 'Test article 4'
    test_id_2 = 12

    graph = WikiGraph()

    graph.add_article(test_name, test_id)
    graph.add_article(test_name_2, test_id_2)
    graph.add_link(test_name, test_name_2)
    graph.add_link(test_name, test_name_2)



def test2():
    test_name = 'Test article 3'
    graph = WikiGraph()
    print graph.get_related_articles(test_name)

if __name__ == '__main__':
    test2()
