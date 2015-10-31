import json

__author__ = 'lukasz'


class JsonParser:

    def __init__(self):
        print("test")
        self.JSON = None




    def getJsonFile(self, valuesArray):
        return self.JSON

    def setJsonFile(self, database):
        return json.dumps(database)
