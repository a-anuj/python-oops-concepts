# OOPs - using python

## Creating a class
- Class can be created by using class keyword
```py
class classname:
    body...
```

## Instantiating a class ie creating an object
```py
item1 = Item("Pen", 30, 10)
```

## init method
- This method is called at default when the class is instantiated
- It has a default parameter named as self which will be the object itself

Example :
```py
def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
```

- Class can be instantiated by providing the name, price, quantity parameters

## __dict__ method : 
- provide all the attributes present in the particular class or object.
```py
item1 = Item()
print(item1.__dict__)
```

## __repr__ method : 
- shows all the instances of a class with specified names
  
```py
def __repr__(self):
        return f"Item({self.name},{self.price},{self.quantity})"
```

## Class Methods

- In Python, a classmethod is a method that is bound to the class and not the instance of the class. It can be called on the class itself, rather than on instances of the class.
- Class method can be identified by the decorator called @classmethod

```py
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
```