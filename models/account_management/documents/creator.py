from base_classes.base_document import Document
from models.account_management.collections.creators import Creators

class Creator(Document):
    def __init__(self, name, users=None) -> None:
        document_ref = Creators().create_document_ref()
        super().__init__(document_ref, username=name, users=users)