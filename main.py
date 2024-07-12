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

    def calc_price(self):
        return self.price * self.quantity

    def calc_discount(self):
        self.price = self.price * Item.discount_rate

    def __repr__(self):
        return f"Item({self.name},{self.price},{self.quantity})"


Item.instantiate_from_csv()
print(Item.all)
