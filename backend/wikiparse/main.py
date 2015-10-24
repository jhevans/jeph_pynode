from backend.wikiparse.parser import parse
from backend.graph.batch_links import WikiLinksGraph
import settings
import sys

__author__ = 'Edward.Kent'


def run():
    graph = WikiLinksGraph()
    parser = parse.Parser(graph)
    parser.whole_file_parse(settings.WIKIPEDIA_XML_FILEPATH_TEST)

if __name__ == '__main__':
    run()
    sys.exit()
