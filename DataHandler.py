__author__ = 'edzio94'
import web
import json


class DataHandler:
    json = []

    def __init__(self):
        print("Creating DataHandler")
        self.dataBaseResult = 'null'

    def saveJson(self, Values):
        for x in Values:
            self.json.append([])
            for value in Values.values():
                self.json[len(self.json) - 1].append(value)

    def getBooks(self, conn):
        self.dataBaseResult = conn.db.select('book_releases')
        return conn.db.select('book_releases')
