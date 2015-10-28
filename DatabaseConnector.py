__author__ = 'lukasz'
import web


class Connector:
    def __init__(self):
        self.db = web.database(dbn='mysql', user='root', pw='root', db='releases')
