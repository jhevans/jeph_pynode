__author__ = 'Edward.Kent'

from py2neo import Graph
import backend.wikiparse.settings as settings

__author__ = 'Edward.Kent'


class WikiLinksGraph(object):
    def __init__(self):
        self.graph = Graph(self.get_uri(settings.NEO4J_SERVER, settings.NEO4J_PORT, settings.NEO4J_USERNAME,
                                        settings.NEO4J_PASSWORD))
        self.reset_batch()
        self.query_count = 0
        self.batch_size = 10000

    @staticmethod
    def get_uri(server_path, port, username, password):
        return "http://{}:{}@{}:{}/db/data".format(username, password, server_path, port)

    def add_article(self, title, id):
        self.do_batch_article_query(id, title)

    def add_link(self, from_title, to_title, count=1):
        self.do_batch_link_query(from_title, to_title, count)

    def add_links(self, from_title, dict_of_links):
        for link in dict_of_links.keys():
            count = dict_of_links[link]
            self.add_link(from_title, link, count=count)

    def do_batch_link_query(self, from_title, to_title, weight):
        from_title = from_title.replace('"', '').replace('\\', '').lower()
        to_title = to_title.replace('"', '').replace('\\', '').lower()

        with open(settings.BATCH_LINK_FILE, 'a') as batch_file:
            batch_file.write("{},{},{}\n".format(from_title, to_title, weight))
        self.query_count += 1
        if self.query_count >= self.batch_size:
            self.purge_queries()

    def purge_queries(self):
        query = """LOAD CSV WITH HEADERS FROM "file://{}" AS csvLine
            MATCH (from: Article2 {{title_lower:csvLine.from_title}}), (to:Article2 {{title_lower:csvLine.to_title}})
            MERGE (from)-[rel:RELATED_TO]->(to)
            ON CREATE SET rel.weight = toInt(csvLine.weight)
            ON MATCH SET rel.weight = rel.weight + toInt(csvLine.weight)
        """.format(settings.BATCH_LINK_FILE)
        self.graph.cypher.execute(query)
        self.query_count = 0
        self.reset_batch()

    def reset_batch(self):
        with open(settings.BATCH_LINK_FILE, 'w') as batch_file:
            batch_file.write("from_title,to_title,weight\n")

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
