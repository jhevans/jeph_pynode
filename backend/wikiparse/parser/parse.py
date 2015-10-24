__author__ = 'Edward.Kent'

from lxml import etree
from backend.wikiparse.parser import links_counter
from backend.graph.graph import WikiGraph
import datetime

ns = '{http://www.mediawiki.org/xml/export-0.10/}'

class Parser(object):

    def __init__(self, graph):
        """
        :param graph:
        :type graph: WikiGraph
        """
        self.graph = graph

    def whole_file_parse(self, filepath, limit=None):

        context = etree.iterparse(open(filepath, 'r'), events=('end',))

        element_count = 0
        page_count = 0
        start_time = datetime.datetime.now()

        for (event, elem) in context:
            if elem.tag == ns+'page':
                # do things here
                self.parse_links(elem)
                page_count += 1
                if page_count %100 == 0:
                    print page_count, '...'

                elem.clear()
                while elem.getprevious() is not None:
                    del elem.getparent()[0]

            element_count += 1

            if limit is not None:
                if element_count >= limit:
                    break

        self.graph.purge_queries()
        del context

        end_time = datetime.datetime.now()

        print end_time
        print page_count
        print element_count
        print end_time - start_time

    def parse_article(self, element):
        """
        Parses a wikipedia 'page', adding the article title and id to the graph
        """

        try:
            redirect = element.find(ns+'redirect')
            if redirect is not None:
                return None
            title = element.find(ns+'title').text.encode('utf-8')
            id = element.find(ns+'id').text
            self.graph.add_article(title, id)

        except Exception as e:
            print e
            return None

    def parse_links(self, element):
        """
        Parses a wikipedia 'page', adding links from the article
        """
        try:
            redirect = element.find(ns+'redirect')
            if redirect is not None:
                return None
            title = element.find(ns+'title').text.encode('utf-8')
            id = element.find(ns+'id').text
            revision = element.find(ns+'revision')
            text = revision.find(ns+'text').text.encode('utf-8')
            count_of_links = links_counter.get_count_of_links(text)
            self.graph.add_links(title, count_of_links)

        except Exception as e:
            return None


