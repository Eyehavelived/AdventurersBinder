import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud.firestore_v1.base_query import FieldFilter, BaseCompositeFilter

class Database():
    CREDENTIALS = credentials.Certificate("db/serviceAccountKey.json")
    firebase_admin.initialize_app(CREDENTIALS)
    CLIENT = firestore.client()

    # def get(self, collection_name):
    #     self.CLIENT.collection(collection_name).get()

    class Field:
        """
        Alllows construction of the FieldFilter object in a pseudo-functional way
        """
        def __init__(self, attribute_name: str) -> None:
            self.attribute_name = attribute_name
        
        def less_than(self, value):
            return FieldFilter(self.attribute_name, "<", value)
        
        def less_than_or_equal_to(self, value):
            return FieldFilter(self.attribute_name, "<=", value)
        
        def more_than(self, value):
            return FieldFilter(self.attribute_name, ">", value)
        
        def more_than_or_equal_to(self, value):
            return FieldFilter(self.attribute_name, ">=", value)
        
        def equal_to(self, value):
            return FieldFilter(self.attribute_name, "==", value)
        
        def not_equal_to(self, value):
            return FieldFilter(self.attribute_name, "!=", value)
        
        def array_contains(self, value):
            """
            value can be a single value, or it can be a list of values
            e.g.
                FieldFilterHelper("domain").array_contains("Light")
                OR
                FieldFilterHelper("domain").array_contains(["Light", "Life"])
            Do note that you can have nested arrays, but then the filter will look for exact matches for the nested array.
            e.g. 
                FieldFilterHelper("domain").array_contains([["Light", "Life"], [""]])
            """
            return FieldFilter(self.attribute_name, "array_contains", value)
        
        def is_in(self, value: list):
            return FieldFilter(self.attribute_name, "in", value)
        
        def is_not_in(self, value: list):
            # Sample snippet was not available on the documentation at the time this was written, so I can't guarantee this works
            return FieldFilter(self.attribute_name, "not_in", value)