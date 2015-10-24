from backend.wikiparse.parser import parse
import settings
import sys

__author__ = 'Edward.Kent'


def run():
    parse.whole_file_parse(settings.WIKIPEDIA_XML_FILEPATH_TEST, limit=10000)

if __name__ == '__main__':
    run()
    sys.exit()
