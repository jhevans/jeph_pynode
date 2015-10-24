# -*- coding: utf-8 -*-

__author__ = 'Peter.Ogden'
__copyright__ = 'Copyright (C) 2015, Auto Trader UK'

from backend.wikiparse.parser.links_counter import get_count_of_links
from copy import copy

path = r'C:\Users\peter.ogden\PycharmProjects\jeph_pynode\backend\fixtures\test_wikipedia_snippet.xml'

file = open(path, 'r')
snippet = file.read()

list_of_snippets = snippet.split('<page>')
return_item = []

for snippet in list_of_snippets:
    new_page = {}
    new_page['pageid'] = copy(snippet).split('</id>')[0].split('<id>')[-1]
    new_page['name'] = copy(snippet).split('<title>')[-1].split('</title>')[0]
    new_page['linkedArticles'] = get_count_of_links(copy(snippet).split('<text')[-1].split('</text>')[0]).keys()
    return_item.append(new_page)

with open('new_mock_data.py', 'w') as new_file:
    new_file.write(str(return_item))

