import json
import DataHandler
from DatabaseConnector import Connector
import JsonParser

__author__ = 'lukasz'
import web

urls = (
    '/', 'index', 'getbooks'

)


class index:
    def __init__(self):
        self.conn = Connector()
        self.dataHandler = DataHandler.DataHandler()
        self.list = []
        #        print(self.db)
        self.dataHandler.getBooks(self.conn)

        self.t = {}
        #self.t.update(self.dataHandler.dataBaseResult)
        for x in self.dataHandler.dataBaseResult:
            self.t.update(x)

        print(self.t)
        print(len(self.t))
        parser = JsonParser.JsonParser()
        self.dataHandler.JSON = parser.setJsonFile(self.t)
        print('Koniec')




    def GET(self):
        print(self.dataHandler.dataBaseResult)


    def showData(self):
        print(self.dataHandler.JSON)

get = index()
get.GET()
get.showData()
