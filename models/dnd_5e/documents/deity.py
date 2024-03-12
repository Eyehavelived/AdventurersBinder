from base_classes.base_document import Document
from models.dnd_5e.collections.deities import Deities

class Deity(Document):
    def __init__(self, name, aliases: list, domains: list, url, sourcebook) -> None:
        """
        Domains: list of document references for domains, must have at least 1
        Aliases: list of strings, can be empty
        """
        document_ref = Deities().create_document_ref()
        super().__init__(document_ref, name=name, aliases=aliases, domains=domains, url=url, sourcebook=sourcebook)

        
    



         