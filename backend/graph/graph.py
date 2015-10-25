import cherrypy
from py2neo import Graph
import backend.wikiparse.settings as settings
import random
__author__ = 'Edward.Kent'


class WikiGraph(object):

    def __init__(self):
        self.graph = Graph(self.get_uri(settings.NEO4J_SERVER, settings.NEO4J_PORT, settings.NEO4J_USERNAME,
                                        settings.NEO4J_PASSWORD))
        self.transaction = self.graph.cypher.begin()
        self.query_count = 0
        self.batch_size = 40


    @staticmethod
    def get_uri(server_path, port, username, password):
        return "http://{}:{}@{}:{}/db/data".format(username, password, server_path, port)

    def add_article(self, title, id=None):
        if id is not None:
            query = """MERGE (article:Article { title:{title}})
                ON CREATE SET article.wikiid = {id}
                """

            self.do_batch_query(query, title=title, id=id)

        else:
            query = """MERGE (article:Article { title:{title}})
                """

            self.do_batch_query(query, title=title)

    def add_link(self, from_title, to_title, count=1):
        query = """MERGE (from:Article {title:{from_title}})-[rel]->(to:Article {title:{to_title}})
                    ON CREATE SET rel.weight = 1
                    ON MATCH SET rel.weight = rel.weight + {count}
                """
        self.do_batch_query(query, from_title=from_title, to_title=to_title, count=count)

    def add_links(self, from_title, dict_of_links):
        for link in dict_of_links.keys():
            count = dict_of_links[link]
            self.add_link(from_title, link, count=count)

    def get_related_articles(self, article_title, limit=None, destinationTitle=None):
        if limit is None:
            # query = """MATCH (article1:Page {title: {title}})-[rel]->(article2: Page) RETURN article2"""
            # result = self.graph.cypher.execute(query, title=article_title)
            # output = [node[0]["title"] for node in result]
            # if len(output) == 0:
            query = """MATCH (article1:Page)-[rel]->(article2: Page)
            WHERE article1.title =~ {title}
            RETURN article2"""
            result = self.graph.cypher.execute(query, title='(?i)'+article_title)
            output = [node[0]["title"] for node in result]

            return output
        else:
            if destinationTitle is None:
                limit = int(limit)
                # query = """MATCH (article1:Page {title: {title}})-[rel]->(article2: Page) WITH article2, rand() as r RETURN article2 ORDER BY r LIMIT {limit}"""
                # result = self.graph.cypher.execute(query, title=article_title, limit=limit)
                # output = [node[0]["title"] for node in result]
                # if len(output) == 0:
                query = """MATCH (article1:Page)-[rel]->(article2: Page)
                WHERE article1.title =~ {title}
                RETURN article2
                LIMIT {limit}
                """
                result = self.graph.cypher.execute(query, title='(?i)'+article_title, limit=limit)
                output = [node[0]["title"] for node in result]


                return output

            else:

                shortest_path = self.get_shortest_path(article_title, destinationTitle)
                next_node = shortest_path[1]

                limit = int(limit) - 1  # insert the correct answer separately
                # query = """MATCH (article1:Page {title: {title}})-[rel]->(article2: Page)
                #  WHERE article2.title <> {correct}
                #  WITH article2, rand() as r RETURN article2 ORDER BY r LIMIT {limit}"""
                # result = self.graph.cypher.execute(query, title=article_title, limit=limit, correct=next_node)
                # output = [node[0]["title"] for node in result]
                # if len(output) == 0:
                query = """
                MATCH (article1:Page)-[rel]->(article2: Page)
                WHERE article1.title =~ {title} AND article2.title <> {correct}
                WITH article2, rand() as r RETURN article2 ORDER BY r LIMIT {limit}
                """
                result = self.graph.cypher.execute(query, title='(?i)'+article_title, limit=limit, correct=next_node)
                output = [node[0]["title"] for node in result]
                output.append(next_node)
                random.shuffle(output)
                return output




        raise Exception()

    def get_shortest_path(self, from_title, to_title):
        # query="""
        # MATCH (a:Page { title:{from_title}}),(b:Page { title: {to_title} }),
        # p = shortestPath((a)-[*..limit]-(b))
        # RETURN p
        # """.replace('limit', str(settings.SHORTEST_PATH_LIMIT))
        # result = self.graph.cypher.execute(query, from_title=from_title, to_title=to_title)
        # if len(result) == 0:
        query="""
        MATCH (a:Page),(b:Page)
        WHERE a.title =~ {from_title} AND b.title =~ {to_title}
        WITH a, b MATCH
        p = shortestPath((a)-[*..limit]-(b))
        RETURN p
        """.replace('limit', str(settings.SHORTEST_PATH_LIMIT))
        result = self.graph.cypher.execute(query, from_title='(?i)'+from_title, to_title='(?i)'+to_title)
        if len(result) == 0:
            raise cherrypy.NotFound()

        nodes = result[0][0].nodes
        output = [node["title"] for node in nodes]
        return output

    def get_random_node(self):
        offset = random.uniform(0, settings.NODE_COUNT)

        query = """
        MATCH (a:Page) RETURN a SKIP {random_offset} LIMIT 1"""
        result = self.graph.cypher.execute(query, random_offset=offset)
        output = result[0][0]["title"]
        return output

    def get_random_nodes(self):
        max_tries = 999
        for i in range(max_tries):
            try:
                random_node_1 = self.get_random_node()
                random_node_2 = self.get_random_node()
                path_length = len(self.get_shortest_path(random_node_1, random_node_2))
                assert path_length > 0
                return random_node_1, random_node_2, path_length
            except:
                continue

    def do_batch_query(self, query, **kwargs):
        self.transaction.append(query, **kwargs)
        self.query_count += 1
        if self.query_count >= self.batch_size:
            self.purge_queries()

    def purge_queries(self):
        self.transaction.commit()
        self.query_count = 0
        self.transaction = self.graph.cypher.begin()



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
