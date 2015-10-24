from parser import parse
import settings
import sys

__author__ = 'Edward.Kent'


def run():
    parse.parse(settings.WIKIPEDIA_XML_FILEPATH, limit=10000)

if __name__ == '__main__':
    run()
    sys.exit()
