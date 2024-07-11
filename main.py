class Item:
    def calc_price(self, a, b):
        return a*b


item1 = Item()
item1.name = "Pencil"
item1.price = 50
item1.quantity = 10
item1.calc_price(item1.price, item1.quantity)
print("The total amount is ", item1.calc_price(item1.price, item1.quantity))
