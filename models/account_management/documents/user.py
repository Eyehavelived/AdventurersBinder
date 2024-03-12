from base_classes.base_document import Document
from models.account_management.collections.users import Users

class User(Document):
    def __init__(self, username) -> None:
        document_ref = Users().create_document_ref()
        super().__init__(document_ref, username=username, linked_accounts={}, creator_profile=None)

    def link_accounts(self):
        pass

    def add_creator_profile(self):
        pass

        