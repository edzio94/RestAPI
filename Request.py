import DataHandler
from DatabaseConnector import Connector
import JsonParser

__author__ = 'lukasz'
import web

urls = (
    '/','index','getbooks'

)

class index:
    def __init__(self):
        self.conn = Connector()
        self.test = DataHandler.DataHandler()
#        print(self.db)
        self.test.getBooks(self.conn)
        for x in self.test.dataBaseResult:
             print(x.values()) #Prints actual values of dataBaseResuy=lt
        #self.values = JsonParser.getJsonFile(DataHandler.getBooks(self.test))

    def GET(self):
        print(self.test.dataBaseResult)

get = index()
get.GET()


