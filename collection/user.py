from collection.base import Base

class User(Base):
    def __init__(self, *args, **kwargs):
        super().__init__("user", *args, **kwargs)
    
    def add(self, username):
        values = {
            'username': username,
            'characters': {},
            'creators': {},
            'linked_accounts': {}
        }
        return super().add(values)