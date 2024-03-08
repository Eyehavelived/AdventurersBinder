from db.db_client import Database
from collection.base import Base

class AdventurersBinder():
    DATABASE = Database.CLIENT


if __name__=="__main__":
    binder = AdventurersBinder()