import csv


class Item:
    discount_rate = 0.8
    all = []

    def __init__(self, name, price, quantity):
        assert price >= 0, "Price must be greater than or equal to zero"
        assert quantity >= 0, "Quantity must be greater than or equal to zero"

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                item["Name"],
                float(item["Price"]),
                float(item["Quantity"])
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def calc_price(self):
        return self.price * self.quantity

    def calc_discount(self):
        self.price = self.price * Item.discount_rate

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name},{self.price},{self.quantity})"


class Phone(Item):
    def __init__(self, name: str, price: int, quantity=0, broken_phone=0):
        super().__init__(name, price, quantity)
        self.broken_phone = broken_phone
        assert broken_phone >= 0, f"Broken phones must be greater than or equal to 0"


phone1 = Phone("Samsung", 12000, 10, 1)
print(Item.all)
print(Phone.all)
