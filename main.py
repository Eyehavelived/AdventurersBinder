from db.db_client import Database
from models.dnd_5e.documents.rarity import Rarity

class AdventurersBinder():
    DATABASE = Database.CLIENT


if __name__=="__main__":
    # binder = AdventurersBinder()
    print("hi")
    Rarity("mundane").set_document()