from base_classes.base_collection import Collection

class Users(Collection):
    def __init__(self):
        super().__init__("user")