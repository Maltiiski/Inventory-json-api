import uuid
from datetime import datetime

class Item:
    def __init__(self, name, quantity=1, owner="N/A", value="Medium", item_id=None, created_at=None):

        self.name = name
        self.quantity = quantity
        self.owner = owner
        self.value = value