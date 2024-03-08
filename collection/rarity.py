from collection.base import Base

class Rarity(Base):
    def __init__(self, *args, **kwargs):
        super().__init__("rarity", *args, **kwargs)