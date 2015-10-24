from backend.wikiparse.parser import parse
from backend.graph.graph import WikiGraph
import settings
import sys

__author__ = 'Edward.Kent'


def run():
    graph = WikiGraph()
    parser = parse.Parser(graph)
    parser.whole_file_parse(settings.WIKIPEDIA_XML_FILEPATH_TEST, limit=100000)

if __name__ == '__main__':
    run()
    sys.exit()
