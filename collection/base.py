from db.db_client import Database
import json

class Base:
    def __init__(self, collection_name, *args, **kwargs):
        self.collection_name = collection_name
        for key in args:
            self.__dict__[key] = None

    def add(self, **kwargs):
        print(kwargs)
        Database.CLIENT.collection(self.collection_name).add(kwargs)

    def create(self):
        pass