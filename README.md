# OOPs - using python

- [OOPs - using python](#oops---using-python)
  - [Creating a class](#creating-a-class)
  - [Instantiating a class ie creating an object](#instantiating-a-class-ie-creating-an-object)
  - [init method](#init-method)
  - [dict method :](#dict-method-)
  - [repr method :](#repr-method-)
  - [Class Methods](#class-methods)
  - [Static Methods](#static-methods)
  - [Inheritance](#inheritance)
    - [Super Keyword](#super-keyword)

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

## dict method : 
- provide all the attributes present in the particular class or object.
```py
item1 = Item()
print(item1.__dict__)
```

## repr method : 
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

## Static Methods
- In Python, a static method is a method that belongs to a class rather than an instance of the class.
- Unlike instance methods, static methods do not require a reference to the instance (self) or the class (cls) as their first parameter. 
- They are defined using the @staticmethod decorator and can be called on the class itself or on instances of the class.

```py
@staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
```
## Inheritance
- Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class (called a child or derived class) to inherit attributes and methods from another class (called a parent or base class).
- Inheritance promotes code reuse and allows for the creation of a hierarchical relationship between classes.
- In Python, inheritance is implemented by defining a new class that takes an existing class as its base class.

```py
class Phone(Item):
    def __init__(self, name: str, price: int, quantity=0, broken_phone=0):
        super().__init__(name, price, quantity)
        self.broken_phone = broken_phone
        assert broken_phone >= 0, f"Broken phones must be greater than or equal to 0"
```

### Super Keyword
- Super keyword can be used to get the details of attributes and methods from the super/parent class
```py
super().__init__(name, price, quantity)
```

