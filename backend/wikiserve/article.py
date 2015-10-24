# -*- coding: utf-8 -*-

__author__ = 'Peter.Ogden'
__copyright__ = 'Copyright (C) 2015, Auto Trader UK'


class Article(object):

    def __init__(self, page_id, wikigraph):
        self.page_id = page_id
        self.graphparent = wikigraph
        self.name = self._get_name(page_id)
        self.related_articles = self._get_related_articles(page_id)

    def _get_name(self, page_id):
        name = self.graphparent.get_name
        return name

    def _get_related_articles(self, page_id):
        related_articles = self.graphparent.get_related_articles
        return related_articles

