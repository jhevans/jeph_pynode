# -*- coding: utf-8 -*-

__author__ = 'Peter.Ogden'
__copyright__ = 'Copyright (C) 2015, Auto Trader UK'

import re


def _get_all_linked_articles(_text):
    """
    Runs a regex on a text string that recognises strings of text wrapped in double square braces
    :param _text:
    :rtype: list of strings
    """
    regex = re.compile("\[\[(.*?)\]\]")
    links_with_pipes = regex.findall(_text)
    links = []
    for link in links_with_pipes:
        article_name = link.split('|')[0].split('#')[0]
        if article_name:
            links.append(article_name)
    return links


def _get_count_of_items(links):
    """
    Loops over a list of strings, for string it checks if its in the count
    dictionary, if not the item is added with a count of one, if already
    present, it increments the count by one
    :param links:
    :rtype: dict of string keys with int values
    """
    _link_count = {}
    for link in links:
        if link not in _link_count.keys():
            _link_count[link] = 1
        else:
            _link_count[link] += 1
    return _link_count


def get_count_of_links(_text):
    """
    Gets a count of the number of times in a string, a substring occurs, surrounded
    :param _text:
    :return:
    """
    links = _get_all_linked_articles(_text)
    _link_count = _get_count_of_items(links)
    return _link_count


if __name__ == '__main__':
    _file = open(r'C:\Users\peter.ogden\PycharmProjects\jeph_pynode\backend\fixtures\test_wikipedia_snippet.xml', 'r')
    text = _file.read()
    link_count = get_count_of_links(text)
    print(link_count)
