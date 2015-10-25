# -*- coding: utf-8 -*-

__author__ = 'Peter.Ogden'
__copyright__ = 'Copyright (C) 2015, Auto Trader UK'

from backend.wikiserve.mock_data import mock_data

class MockWikiGraph(object):

    def __init__(self):
        self.data = mock_data

    def get_name(self, page_id):
        for article in self.data:
            if article['pageid'] == page_id:
                return article['name']

    def get_related_articles(self, page_id):
        for article in self.data:
            if article['pageid'] == page_id:
                return article['linkedArticles']


