class Item:
    discount_rate = 0.8

    def __init__(self, name, price, quantity):
        assert price >= 0, "Price must be greater than or equal to zero"
        assert quantity >= 0, "Quantity must be greater than or equal to zero"

        self.name = name
        self.price = price
        self.quantity = quantity

    def calc_price(self):
        return self.price * self.quantity

    def calc_discount(self):
        self.price = self.price * Item.discount_rate


item1 = Item("Pen", 30, 10)
item1.calc_discount()
print("The total discount amount is ", item1.price)
print("The total price is ", item1.calc_price())
