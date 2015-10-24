__author__ = 'Edward.Kent'

from lxml import etree


import datetime

ns = '{http://www.mediawiki.org/xml/export-0.10/}'


def whole_file_parse(filepath, limit=None):

    context = etree.iterparse(open(filepath, 'r'), events=('end',))

    element_count = 0
    page_count = 0
    start_time = datetime.datetime.now()

    for (event, elem) in context:
        if elem.tag == ns+'page':
            # do things here
            page_parse(elem)
            page_count += 1
            elem.clear()
            while elem.getprevious() is not None:
                del elem.getparent()[0]

        element_count += 1

        if page_count %100000 == 0:
            print page_count, '...'

        if limit is not None:
            if element_count >= limit:
                break
    del context

    end_time = datetime.datetime.now()

    print end_time
    print page_count
    print element_count
    print end_time - start_time


def page_parse(element):
    """
    Parses a wikipedia 'page', returning the page title, id, and a dictionary of links

    :param element:
    :rtype: (str, str, dict)
    """

    try:
        redirect = element.find(ns+'redirect')
        if redirect is not None:
            return None
        title = element.find(ns+'title').text.encode('utf-8')
        id = element.find(ns+'id').text
        revision = element.find(ns+'revision')
        text = revision.find(ns+'text').text.encode('utf-8')

        #TODO: process text here
    except Exception as e:
        return None
