import uuid
from datetime import datetime

class Item:
    def __init__(self, name, quantity=1, owner="N/A", valuation="Medium", item_id=None, created_at=None):
        self.id = item_id if item_id else str(uuid.uuid4())[:8]
        self.name = name
        self.quantity = quantity
        self.owner = owner
        self.valuation = valuation
        self.created_at = created_at if created_at else datetime.now().strftime("%d-%m-%Y %H:%M")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "quantity": self.quantity,
            "owner": self.owner,
            "valuation": self.valuation,
            "created_at": self.created_at
        }

    @property
    def valuation(self):
        return self._valuation

    @valuation.setter
    def valuation(self, value):
        allowed = ["Low", "Medium", "High"]
        if value.capitalize() not in allowed:
            raise ValueError("invalid value")
        self._valuation = value.capitalize()

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if int(value) < 0:
            raise ValueError("invalid quantity")
        self._quantity = int(value)