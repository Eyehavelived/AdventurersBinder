from db.db_client import Database
from google.cloud.firestore_v1.base_query import FieldFilter
from helpers.filter import Field
from base_classes.base_document import Document

class Collection:
    db = Database.CLIENT
    def __init__(self, collection_name):
        self.collection_name = collection_name
        self.collection_ref = self.db.collection(self.collection_name) # Creates ref if not yet available

    def create_document_ref(self):
        return self.collection_ref.document()
    
    def get_or_create_document(self, document_id):
        return self.collection_ref.document(document_id)

    def get(self):
        return self.db.collection(self.collection_name)
    
    def filter_for_document_where(self, filter: FieldFilter):
        """
        returns a list of documents(?)
        e.g.: self.filter_collection("domains", Field("sourcebook").equal_to("TCE"))
        """
        return self.collection_ref.where(filter)
        