from backend.wikiparse.parser import parse
from backend.graph.batch_article import WikiArticleGraph
import settings
import sys

__author__ = 'Edward.Kent'


def run():
    graph = WikiArticleGraph()
    parser = parse.Parser(graph)
    parser.whole_file_parse(settings.WIKIPEDIA_XML_FILEPATH_TEST, limit=1000)

if __name__ == '__main__':
    run()
    sys.exit()
