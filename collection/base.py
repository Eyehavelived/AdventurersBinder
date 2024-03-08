from db.db_client import Database
from google.cloud.firestore_v1.base_query import FieldFilter
from helpers.filter import Field

class Base:
    db = Database.CLIENT
    def __init__(self, collection_name, *args, **kwargs):
        self.collection_name = collection_name
        for key in args:
            self.__dict__[key] = None

    def add(self, **kwargs):
        print(kwargs)
        self.db.collection(self.collection_name).add(kwargs)

    def create(self):
        pass

    def get_collection(self, collection_name):
        return self.db.collection(collection_name)
    
    def filter_collection(self, collection_name, filter: FieldFilter):
        """
        e.g.: self.filter_collection("domains", Field("sourcebook").equal_to("TCE"))
        """
        collection_ref = self.get_collection(collection_name)
        return collection_ref.where(filter)
        