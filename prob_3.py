# Problem 3:

# # extend the above application
# # There are extra attributes in laptop i.e gpu, port_count and also it has 30% discount

# # application folder structure
# 1. items.py
# 2. laptop.py
# 3. data/items.csv

# Solution :

class Item:
    
    items = []
    
    def __init__(self, name, price, quantity):
        
        self.name = name
        self.price = price
        self.quantity = quantity
        self.discount_rate = 0.20
        
    def calculate_total_price(self):
        
        total_price = self.price * self.quantity
        print(f"The total price of {self.name} is: {total_price}") 
           
    def apply_discount(self):
        
        print(f"Actual price of {self.name} is:", self.price)
        discount_amount = self.price * self.discount_rate
        self.price = self.price - discount_amount
        print(f"After {self.discount_rate * 100} percent discount on {self.name} new price is: {self.price}")

    @classmethod
    def read_file(cls):
        f = open ("data/items.csv","r")
        data = f.readlines()
        for item in data:
            item = Item(item[0], (item[1]),(item[2]))
            Item.items.append(item)

class Laptop(Item):
    def __init__(self, name, price, quantity, gpu, port_count):
        super().__init__(name, price, quantity)
        self.gpu = gpu 
        self.port_count = port_count
        self.discount_rate = 0.30
        
Item.read_file()

laptop = Laptop("HP", 1000 , 4, "NVIDIA GTX 3080", 4)

laptop.apply_discount()

laptop.calculate_total_price()

item_1 = Item("charger", 300, 1)

item_1.apply_discount()