from base_classes.base_document import Document
from models.dnd_5e.collections.rarities import Rarities

class Rarity(Document):
    def __init__(self, name) -> None:
        document_ref = Rarities().create_document_ref()
        super().__init__(document_ref, name=name)