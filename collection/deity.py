from collection.base import Base

class Deity(Base):
    def __init__(self):
        super().__init__("deity")
    
    def add(self, name: str, aliases: dict, domains: dict, url: str, sourcebook):
        value = {
            'name': name,
            'aliases': aliases
        }
        return super().add()