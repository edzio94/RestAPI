__author__ = 'edzio94'
import web
import json


class DataHandler:
    json = []

    def __init__(self):
        print("Creating DataHandler")
        self.dataBaseResult = 'null'


    def saveJson(self, Values):
        self.jsonFormat = Values

    def getBooks(self, conn):
        self.dataBaseResult = conn.db.select('book_releases')
        return conn.db.select('book_releases')


