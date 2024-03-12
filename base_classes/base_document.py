from google.cloud.firestore_v1.document import DocumentReference

class Document:
    def __init__(self, document_ref: DocumentReference, **kwargs) -> None:
        self.document_ref = document_ref
        self.attributes = kwargs

    def get_attributes(self):
        return self.attributes
    
    def set_document(self):
        self.document_ref.set(self.attributes)

    

    