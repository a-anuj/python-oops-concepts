from item import Item


class Phone(Item):
    def __init__(self, name: str, price: int, quantity=0, broken_phone=0):
        super().__init__(name, price, quantity)
        self.broken_phone = broken_phone
        assert broken_phone >= 0, f"Broken phones must be greater than or equal to 0"