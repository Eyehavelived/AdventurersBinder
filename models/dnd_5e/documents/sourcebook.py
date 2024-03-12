from base_classes.base_document import Document
from models.dnd_5e.collections.sourcebooks import Sourcebooks

class Sourcebook(Document):
    def __init__(self, sourcebook_id, name, author, is_homebrew, is_playtest):
        document_ref = Sourcebooks().get_or_create_document(sourcebook_id)
        super.__init__(document_ref, name=name, author=author, is_homebrew=is_homebrew, is_playtest=is_playtest)