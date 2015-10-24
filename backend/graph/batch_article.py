__author__ = 'Edward.Kent'

from py2neo import Graph
import backend.wikiparse.settings as settings
__author__ = 'Edward.Kent'


class WikiArticleGraph(object):

    def __init__(self):
        self.graph = Graph(self.get_uri(settings.NEO4J_SERVER, settings.NEO4J_PORT, settings.NEO4J_USERNAME,
                                        settings.NEO4J_PASSWORD))
        self.reset_batch()
        self.query_count = 0
        self.batch_size = 1000


    @staticmethod
    def get_uri(server_path, port, username, password):
        return "http://{}:{}@{}:{}/db/data".format(username, password, server_path, port)

    def add_article(self, title, id):
        self.do_batch_article_query(title, id)

    def add_link(self, from_title, to_title, count=1):
        query = """MERGE (from:Article {title:{from_title}})-[rel:RELATED_TO]->(to:Article {title:{to_title}})
                    ON CREATE SET rel.weight = 1
                    ON MATCH SET rel.weight = rel.weight + {count}
                """
        self.do_batch_query(query, from_title=from_title, to_title=to_title, count=count)

    def add_links(self, from_title, dict_of_links):
        for link in dict_of_links.keys():
            count = dict_of_links[link]
            self.add_link(from_title, link, count=count)

    def get_related_articles(self, article_title):
        query = """MATCH (article1:Article {title: {title}})-[:RELATED_TO]->(article2: Article) RETURN article2"""

        result = self.graph.cypher.execute(query, title=article_title)
        return result

    def do_batch_article_query(self, id, name):
        with open(settings.BATCH_ARTICLE_FILE, 'w+') as batch_file:
            batch_file.write("{},{}\n".format(id, name))
        self.query_count += 1
        if self.query_count >= self.batch_size:
            self.purge_queries()

    def purge_queries(self):
        query = """LOAD CSV WITH HEADERS FROM "file://{}" AS csvLine
            CREATE (a:Article { wikiid: toInt(csvLine.wikiid), title: csvLine.title })
        """.format(settings.BATCH_ARTICLE_FILE)
        self.graph.cypher.execute(query)
        self.query_count = 0
        self.reset_batch()

    def reset_batch(self):
        with open(settings.BATCH_ARTICLE_FILE, 'w') as batch_file:
            batch_file.write("wikiid,title\n")



# def test1():
#     test_name = 'Test article 3'
#     test_id = 2
#
#     test_name_2 = 'Test article 4'
#     test_id_2 = 12
#
#     graph = WikiGraph()
#
#     graph.add_article(test_name, test_id)
#     graph.add_article(test_name_2, test_id_2)
#     graph.add_link(test_name, test_name_2)
#     graph.add_link(test_name, test_name_2)
#
#
#
# def test2():
#     test_name = 'Test article 3'
#     graph = WikiGraph()
#     print graph.get_related_articles(test_name)
#
# if __name__ == '__main__':
#     test2()
