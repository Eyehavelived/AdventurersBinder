import firebase_admin
from firebase_admin import credentials, firestore

class Database():
    CREDENTIALS = credentials.Certificate("db/serviceAccountKey.json")
    firebase_admin.initialize_app(CREDENTIALS)
    CLIENT = firestore.client()

    # def get(self, collection_name):
    #     self.CLIENT.collection(collection_name).get()
