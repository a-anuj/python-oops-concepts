import csv


class Item:
    discount_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=0):

        assert price >= 0, "Price must be greater than or equal to zero"
        assert quantity >= 0, "Quantity must be greater than or equal to zero"

        self.__name = name
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
                int(item["Quantity"])
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def calc_price(self):
        return self.price * self.quantity

    def calc_discount(self):
        self.price = self.price * Item.discount_rate

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name},{self.price},{self.quantity})"
