# -*- coding: utf-8 -*-

__author__ = 'Peter.Ogden'
__copyright__ = 'Copyright (C) 2015, Auto Trader UK'

import re


def _get_all_linked_articles(_text):
    regex = re.compile("\[\[(.*?)\]\]")
    links_with_pipes = regex.findall(_text)
    links = []
    for link in links_with_pipes:
        article_name = link.split('|')[0]
        links.append(article_name)
    return links


def _get_count_of_items(links):
    _link_count = {}
    for link in links:
        if link not in _link_count.keys():
            _link_count[link] = 1
        else:
            _link_count[link] += 1
    return _link_count


def get_count_of_links(_text):
    links = _get_all_linked_articles(_text)
    _link_count = _get_count_of_items(links)
    return _link_count


if __name__ == '__main__':
    _file = open(r'C:\Users\peter.ogden\PycharmProjects\jeph_pynode\backend\fixtures\test_wikipedia_snippet.xml', 'r')
    text = _file.read()
    link_count = get_count_of_links(text)
    print(link_count)
